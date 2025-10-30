# tests/conformance/test_random_soup.py
from pathlib import Path

import pytest
from click.testing import CliRunner

from reference.cli.tsc import main as tsc_main

EXAMPLE = Path("examples/cellular-automata/random-soup.md")

pytestmark = pytest.mark.filterwarnings("ignore::DeprecationWarning")


@pytest.mark.xfail(reason="Reference algorithm not wired; remove xfail when ready.", strict=True)
@pytest.mark.parametrize("seed", [1, 2, 3, 4, 5])
def test_random_soup_c_in_range(seed: int):
    if not EXAMPLE.exists():
        pytest.skip(f"Missing example: {EXAMPLE}")

    runner = CliRunner()
    result = runner.invoke(tsc_main, [str(EXAMPLE), "--format", "json", "--seed", str(seed)])
    assert result.exit_code == 0, result.output

    import json

    payload = json.loads(result.output)
    c = float(payload["c"])

    assert 0.22 <= c <= 0.27
