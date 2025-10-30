# reference/cli/tsc.py
from __future__ import annotations

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

try:
    # v2.1: reference-only import; no stable public API commitment.
    from reference.python.tsc_controller import compute_c_from_file
except Exception:  # pragma: no cover - import fallback path
    compute_c_from_file = None

console = Console()


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument("input_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--format",
    "out_format",
    type=click.Choice(["text", "json"], case_sensitive=False),
    default="text",
    show_default=True,
    help="Output format.",
)
@click.option(
    "--seed",
    type=int,
    default=None,
    show_default=False,
    help="Optional RNG seed (if your implementation uses one).",
)
def main(input_path: Path, out_format: str, seed: int | None) -> None:
    """
    TSC CLI (v2.1): run the reference TSC computation on INPUT_PATH.

    INPUT_PATH can point to an example (*.md) or a data file understood by the reference.
    """
    if compute_c_from_file is None:
        console.print(
            "[bold red]Error:[/bold red] TSC reference implementation not wired yet.\n"
            "Please implement [bold]reference/python/tsc_controller.py::compute_c_from_file[/bold] "
            "or copy your reference code into [bold]reference/python/[/bold].\n"
            "See QUICKSTART.md for details.",
            highlight=False,
        )
        sys.exit(2)

    try:
        if seed is None:
            c_value: float = compute_c_from_file(str(input_path))
        else:
            c_value = compute_c_from_file(str(input_path), seed=seed)
    except NotImplementedError:
        console.print(
            "[bold red]NotImplementedError:[/bold red] compute_c_from_file() is a stub.\n"
            "Wire up the reference algorithm in [bold]tsc_controller.py[/bold].",
            highlight=False,
        )
        sys.exit(2)

    payload = {"path": str(input_path), "c": float(c_value), "seed": seed}

    if out_format.lower() == "json":
        console.print_json(data=payload)
    else:
        table = Table(show_header=True, header_style="bold")
        table.add_column("Path")
        table.add_column("C_Σ")
        table.add_column("Seed")
        table.add_row(payload["path"], f"{payload['c']:.6f}", str(payload["seed"]))
        console.print(table)


if __name__ == "__main__":
    main()
