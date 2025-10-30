# reference/python/parsers/stub.py
from __future__ import annotations

"""Stub parser returning fixed values (for CLI testing)."""

from typing import Optional, Iterable
from reference.python.parser_interface import ParsedInput
from reference.python.tsc_controller import (
    VerifyEnv, WitnessFloors, PolicyConfig,
    Metrics, WitnessStatus, OODStatus,
)


def stub_parser(path: str, seed: Optional[int] = None) -> ParsedInput:
    """
    Pure function: path → fixed ParsedInput.

    Returns high coherence for 'glider', low for others.
    """

    # Determine expected coherence from filename
    name = path.lower()
    c = 0.996 if "glider" in name or "lwss" in name else 0.24

    # ---- Pure helper functions (closures over c) ----
    def sample_index_set(_state, _policy) -> Iterable[int]:
        return range(10)

    def compute_metrics(_indices) -> Metrics:
        # (C_Σ, H, V, D, CI) signature as used in the reference codebase
        return Metrics(c, c, c, c, (c - 0.01, c + 0.01))

    def compute_witnesses(_indices) -> WitnessStatus:
        # Example stable values within reasonable ranges
        return WitnessStatus(0.02, 0.25, 0.06, 0.22, 0.015)

    def compute_ood(_indices) -> OODStatus:
        return OODStatus(0.10, 0.95)

    # ---- Compose immutable environment ----
    env = VerifyEnv(
        sample_index_set=sample_index_set,
        compute_metrics=compute_metrics,
        compute_witnesses=compute_witnesses,
        compute_ood=compute_ood,
    )

    floors = WitnessFloors(
        nu_min=1e-3,
        H_min=0.1,
        L_min=1e-3,
        nu_min_D=1e-4,
        H_min_D=0.05,
    )

    cfg = PolicyConfig()

    return ParsedInput(env=env, floors=floors, cfg=cfg)
