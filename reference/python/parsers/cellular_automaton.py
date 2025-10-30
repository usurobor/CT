# reference/python/parsers/cellular_automaton.py
from __future__ import annotations

"""
Parser for cellular automaton examples (Conway's Life).

Pure functional pipeline:
  markdown → frames → grids → H/V/D witnesses → ParsedInput
"""

from dataclasses import dataclass
from typing import Optional, List, Iterable, Tuple
import re

from reference.python.parser_interface import ParsedInput
from reference.python.tsc_controller import (
    VerifyEnv, WitnessFloors, PolicyConfig,
    Metrics, WitnessStatus, OODStatus,
)

# Local import to avoid cycles (parsers.__init__ imports us)
from reference.python.parsers.stub import stub_parser


Grid = List[List[int]]

def cellular_automaton_parser(path: str, seed: Optional[int] = None) -> ParsedInput:
    """
    Pure function: markdown file → ParsedInput for cellular automaton.

    Pipeline:
      1) read_markdown(path) → str
      2) extract_frames(markdown) → List[Grid]
      3) build witness closures over frames
      4) compose VerifyEnv
      5) construct ParsedInput
    """
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except OSError:
        # On any read error, fall back to stub (pure & deterministic)
        return stub_parser(path, seed)

    frames = extract_frames(content)

    # If we couldn’t parse a usable set of frames, keep system behavior stable.
    if not frames:
        return stub_parser(path, seed)

    # ---- Witness closures (pure, close over 'frames') ----

    def sample_index_set(_state, _policy) -> Iterable[int]:
        # Sample all frames; in a larger dataset you might subsample by seed.
        return range(len(frames))

    def compute_metrics(indices: Iterable[int]) -> Metrics:
        # Compute simple H/V/D adjacency coherences in [0,1]; average across frames.
        Hs, Vs, Ds = [], [], []
        for i in indices:
            H, V, D = _adjacency_coherences(frames[i])
            Hs.append(H)
            Vs.append(V)
            Ds.append(D)

        # Simple means (fallback to 0.0 if empty)
        Hm = sum(Hs) / len(Hs) if Hs else 0.0
        Vm = sum(Vs) / len(Vs) if Vs else 0.0
        Dm = sum(Ds) / len(Ds) if Ds else 0.0

        # A conservative aggregate C_Σ (could be a policy-weighted mix in future)
        C = 0.5 * Hm + 0.3 * Vm + 0.2 * Dm
        ci = (max(C - 0.05, 0.0), min(C + 0.05, 1.0))
        return Metrics(C, Hm, Vm, Dm, ci)

    def compute_witnesses(indices: Iterable[int]) -> WitnessStatus:
        # Light-weight health indicators derived from sparsity and stability.
        # (Matches the 5-arg WitnessStatus signature used in the stub.)
        density = _mean_density([frames[i] for i in indices])
        stability = _temporal_stability([frames[i] for i in indices])
        # Derive five small, bounded terms (purely functional heuristics).
        return WitnessStatus(
            0.01 + 0.04 * (1 - abs(0.3 - density)),   # nu
            0.10 + 0.40 * stability,                   # H health
            0.02 + 0.06 * (1 - density),               # L
            0.10 + 0.35 * stability,                   # D health
            0.010 + 0.020 * (1 - stability),           # residual-ish
        )

    def compute_ood(indices: Iterable[int]) -> OODStatus:
        # OOD proxy from density vs. a nominal Life regime around 0.3.
        density = _mean_density([frames[i] for i in indices])
        dist = abs(density - 0.30)  # distance from nominal
        score = max(0.0, 1.0 - 2.0 * dist)  # crude confidence
        return OODStatus(dist, score)

    env = VerifyEnv(
        sample_index_set=sample_index_set,
        compute_metrics=compute_metrics,
        compute_witnesses=compute_witnesses,
        compute_ood=compute_ood,
    )

    floors = WitnessFloors(
        nu_min=1e-3,
        H_min=0.10,
        L_min=1e-3,
        nu_min_D=1e-4,
        H_min_D=0.05,
    )
    cfg = PolicyConfig(Theta=0.80)

    return ParsedInput(env=env, floors=floors, cfg=cfg)


# ------------------ Pure helpers ------------------ #

_FRAME_HEADER_RE = re.compile(r"^\s{0,3}#{3,}\s*frame\b.*$", re.IGNORECASE | re.MULTILINE)

def extract_frames(markdown: str) -> List[Grid]:
    """
    Pure: markdown → list of binary grids.

    Supported forms:
      - Sections starting with "### Frame ..." followed by grid lines
      - Fenced blocks ```life ... ```
      - Fenced blocks ```cells ... ```
      - Bare grid-like runs (3+ lines of [# O . 0 1 ])

    Mapping: '#','O','o','1' → 1; '.', '0', ' ' → 0
    """
    blocks: list[list[str]] = []

    # 1) Pull fenced blocks tagged as life/cells
    for tag in ("life", "cells"):
        blocks.extend(_extract_fenced(markdown, tag))

    # 2) Pull sections under "### Frame" headers
    blocks.extend(_extract_frame_sections(markdown))

    # 3) As a last resort, sniff bare grid runs
    if not blocks:
        blocks.extend(_extract_bare_grids(markdown))

    # Convert to integer grids
    frames: List[Grid] = []
    for raw_lines in blocks:
        grid = _to_grid(raw_lines)
        if grid:
            frames.append(grid)

    # Deduplicate exact duplicates (pure structural set-ish filter)
    unique: list[Grid] = []
    seen: set[Tuple[Tuple[int, ...], ...]] = set()
    for g in frames:
        key = tuple(tuple(row) for row in g)
        if key not in seen:
            unique.append(g)
            seen.add(key)
    return unique


def _extract_fenced(text: str, tag: str) -> list[list[str]]:
    rx = re.compile(rf"```{tag}\s*\n(.*?)\n```", re.IGNORECASE | re.DOTALL)
    blocks: list[list[str]] = []
    for m in rx.finditer(text):
        body = m.group(1)
        lines = [ln.rstrip() for ln in body.splitlines() if ln.strip()]
        if _looks_like_grid(lines):
            blocks.append(lines)
    return blocks


def _extract_frame_sections(text: str) -> list[list[str]]:
    # Find every '### Frame ...' header and collect lines until next header or EOF
    lines = text.splitlines()
    idxs = [i for i, ln in enumerate(lines) if _FRAME_HEADER_RE.match(ln or "")]
    blocks: list[list[str]] = []
    for k, i in enumerate(idxs):
        j = idxs[k + 1] if k + 1 < len(idxs) else len(lines)
        body = [ln.rstrip() for ln in lines[i + 1 : j] if ln.strip()]
        # Keep only grid-like lines
        grid_lines = [ln for ln in body if all(ch in "#Oo.01 " for ch in ln)]
        if _looks_like_grid(grid_lines):
            blocks.append(grid_lines)
    return blocks


def _extract_bare_grids(text: str) -> list[list[str]]:
    lines = [ln.rstrip() for ln in text.splitlines()]
    blocks: list[list[str]] = []
    cur: list[str] = []
    def flush():
        nonlocal cur
        if _looks_like_grid(cur):
            blocks.append(cur)
        cur = []
    for ln in lines:
        if ln and all(ch in "#Oo.01 " for ch in ln):
            cur.append(ln)
        else:
            flush()
    flush()
    return blocks


def _looks_like_grid(lines: list[str]) -> bool:
    if len(lines) < 3:
        return False
    width = max((len(ln) for ln in lines), default=0)
    if width < 3:
        return False
    # At least 10% non-blank cells present somewhere
    total = sum(len(ln) for ln in lines)
    live = sum(sum(1 for ch in ln if ch in "#Oo1") for ln in lines)
    return total > 0 and (live / total) >= 0.05


def _to_grid(lines: list[str]) -> Grid:
    m: dict[str, int] = {"#": 1, "O": 1, "o": 1, "1": 1, ".": 0, "0": 0, " ": 0}
    grid: Grid = []
    width = max(len(ln) for ln in lines)
    for ln in lines:
        row = [m.get(ch, 0) for ch in ln.ljust(width)]
        grid.append(row)
    return grid


def _adjacency_coherences(grid: Grid) -> Tuple[float, float, float]:
    """
    Return (H, V, D) ∈ [0,1]^3 as the fraction of equal-adjacent pairs
    horizontally, vertically, and diagonally (NW-SE + NE-SW average).
    """
    if not grid or not grid[0]:
        return (0.0, 0.0, 0.0)
    h, w = len(grid), len(grid[0])

    # Horizontal
    h_eq = 0
    h_tot = 0
    for r in range(h):
        for c in range(w - 1):
            h_eq += 1 if grid[r][c] == grid[r][c + 1] else 0
            h_tot += 1
    H = h_eq / h_tot if h_tot else 0.0

    # Vertical
    v_eq = 0
    v_tot = 0
    for r in range(h - 1):
        for c in range(w):
            v_eq += 1 if grid[r][c] == grid[r + 1][c] else 0
            v_tot += 1
    V = v_eq / v_tot if v_tot else 0.0

    # Diagonal (NW-SE and NE-SW)
    d_eq = 0
    d_tot = 0
    for r in range(h - 1):
        for c in range(w - 1):
            d_eq += 1 if grid[r][c] == grid[r + 1][c + 1] else 0
            d_tot += 1
    for r in range(h - 1):
        for c in range(1, w):
            d_eq += 1 if grid[r][c] == grid[r + 1][c - 1] else 0
            d_tot += 1
    D = d_eq / d_tot if d_tot else 0.0

    return (H, V, D)


def _mean_density(frames: List[Grid]) -> float:
    tot = 0
    live = 0
    for g in frames:
        for row in g:
            tot += len(row)
            live += sum(row)
    return (live / tot) if tot else 0.0


def _temporal_stability(frames: List[Grid]) -> float:
    # Jaccard similarity of successive frames averaged
    if len(frames) < 2:
        return 1.0
    sims: list[float] = []
    for a, b in zip(frames[:-1], frames[1:]):
        sims.append(_jaccard(a, b))
    return sum(sims) / len(sims)


def _jaccard(a: Grid, b: Grid) -> float:
    if not a or not a[0] or not b or not b[0]:
        return 0.0
    h = min(len(a), len(b))
    w = min(len(a[0]), len(b[0]))
    inter = 0
    union = 0
    for r in range(h):
        for c in range(w):
            av = a[r][c]
            bv = b[r][c]
            inter += 1 if (av == 1 and bv == 1) else 0
            union += 1 if (av == 1 or bv == 1) else 0
    return (inter / union) if union else 1.0
