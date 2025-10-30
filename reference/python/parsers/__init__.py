# reference/python/parsers/__init__.py
from __future__ import annotations

"""
Parser registry using functional pattern matching.

Add new parsers by:
1) Creating a pure function: (str, Optional[int]) → ParsedInput
2) Adding a predicate to PARSERS (first match wins)
"""

from typing import Callable, Optional, Tuple
from pathlib import Path
from reference.python.parser_interface import Parser, ParsedInput

# Type: (predicate, parser_function)
ParserEntry = Tuple[Callable[[str], bool], Parser]


def _peek_text(path: str, n: int = 1500) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(n)
    except FileNotFoundError:
        return ""
    except OSError:
        return ""


def is_cellular_automaton(path: str) -> bool:
    """
    Predicate: file likely contains cellular automaton frames.

    Heuristics (kept narrow so stub remains default where unsure):
    - Contains '### Frame' headings (markdown style), OR
    - Contains a fenced block tagged 'life' or 'cells', OR
    - Has ≥3 consecutive lines comprised of '#', 'O', '.', '0', '1', and spaces.
    """
    text = _peek_text(path).lower()
    if "### frame" in text or "```life" in text or "```cells" in text:
        return True

    # Lightweight structural sniff (three lines of grid-ish characters)
    lines = [ln.strip().lower() for ln in text.splitlines()[:200]]
    gridish = 0
    for ln in lines:
        if ln and all(ch in "#o.01 " for ch in ln):
            gridish += 1
            if gridish >= 3:
                return True
        else:
            gridish = 0
    return False


def is_stub(_path: str) -> bool:
    """Fallback: always true."""
    return True

# Import parser functions (at end to avoid import order issues)
from reference.python.parsers.stub import stub_parser  # noqa: E402
from reference.python.parsers.cellular_automaton import cellular_automaton_parser  # noqa: E402

# Parser dispatch table (order matters - first match wins)
# Add new parsers here: (predicate, parser_fn)
# Example: (is_time_series, time_series_parser)
PARSERS: list[ParserEntry] = [
    (is_cellular_automaton, cellular_automaton_parser),
    (is_stub, stub_parser),  # Always last (catch-all)
]

def select_parser(path: str) -> Parser:
    """
    Select parser via pattern matching on file content.

    Pure function: dispatches based on predicates.
    """
    for predicate, parser_fn in PARSERS:
        if predicate(path):
            return parser_fn
    # Should never reach (is_stub is catch-all)
    return lambda p, s: stub_parser(p, s)


