# QUICKSTART (v2.1)

This guide assumes Python **3.10+**.

## 1) Install

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

This exposes a `tsc` CLI (via an internal reference package). It does not imply a stable import API.

## 2) Wire your reference implementation

Open:

```
reference/python/tsc_controller.py
```

Replace the `NotImplementedError` in `compute_c_from_file(path: str, seed: Optional[int]) -> float`
with a thin adapter around your reference implementation. Keep the signature stable in v2.1.

If you need more helpers, add them under `reference/python/` and import them here.

## 3) Run the CLI

```bash
tsc path/to/example.md --format text
tsc path/to/example.md --format json
tsc path/to/random-soup.md --format json --seed 42
```

If you see a "reference not wired" message, finish step 2.

## 4) Run tests

```bash
pytest
```

- `test_glider.py` and `test_random_soup.py` include executable contracts for the TSC
  coefficient C_Σ. They are marked `xfail` until your reference is wired. Remove `xfail`
  and tighten bands after calibration (see below).

## 5) Calibrate tolerance bands (once)

1. Run ≥200 trials per case (vary seeds, or sampling windows).
1. Compute median and MAD; set bounds to median ± 3×MAD (clip to [0,1]).
1. Update assertions in `tests/conformance/` and commit with a short note (N, seeds, machine).

## 6) Developer UX

```bash
make setup     # install dev deps
make lint      # code style
make fmt       # auto-format
make test      # run tests
make quickstart
```

## 7) Migration notes (core → spec)

When renaming:

```bash
git mv core spec

find . -name "*.md" -exec sed -i 's|core/|spec/|g' {} +
```

CI's link check will catch any missed links.
