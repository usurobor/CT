# reference/python/tsc_controller.py
"""
Reference controller for TSC (v2.1).

This module is deliberately small and importable. In v2.1, it's *reference code*, not a stable API.
Downstream users should copy this folder if they need integration, per README.
"""

from __future__ import annotations
from typing import Optional


def compute_c_from_file(path: str, *, seed: Optional[int] = None) -> float:
    """
    Compute the TSC coefficient C_Σ from an input file.

    Parameters
    ----------
    path : str
        Path to the input artifact (e.g., example Markdown or data file).
    seed : Optional[int]
        Optional RNG seed used by your reference implementation.

    Returns
    -------
    float
        The TSC coefficient C_Σ.

    Notes
    -----
    Replace this stub with a thin adapter that calls your real reference implementation.
    Keep this function stable within v2.1 so tests and the CLI don't churn.
    """
    raise NotImplementedError("Wire your reference implementation here.")