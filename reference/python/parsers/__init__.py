# reference/python/parsers/__init__.py
from __future__ import annotations

"""
Parser registry using functional pattern matching.

To add a new parser:
1) Create parsers/my_parser.py with is_my_format() and my_parser()
2) Import them here
3) Add to PARSERS list (order matters - first match wins)
"""

from typing import Callable, Tuple
from reference.python.parser_interface import Parser

# Type: (predicate, parser_function)
ParserEntry = Tuple[Callable[[str], bool], Parser]

# Import parsers (each provides predicate + function)
from reference.python.parsers.cellular_automaton import (
    is_cellular_automaton,
    cellular_automaton_parser,
)
from reference.python.parsers.stub import is_stub, stub_parser


# Parser dispatch table (order matters - first match wins)
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
    return stub_parser