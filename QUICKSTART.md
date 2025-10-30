# QUICKSTART (v2.1)

This guide assumes Python **3.10+**.

## 1) Install
```bash
python3 -m pip install --upgrade pip
pip install -e ".[dev]"
```

This exposes a `tsc` CLI (via an internal reference package). It does not imply a stable import API.

## 2) Wire your reference implementation

Open `reference/python/tsc_controller.py`

The file contains:
- **Stub entry point:** `compute_c_from_file(path, seed)` at the top (marked `NotImplementedError`)
- **Full controller:** The complete v2.0.0 state machine implementation below

To wire the CLI:
1. Implement a markdown parser to read example files
2. Extract H/V/D observations from frames
3. Build `VerifyEnv`, `WitnessFloors`, and `PolicyConfig`
4. Call the existing `verify_tsc_plus()` function
5. Return the `C_Σ` value from the `Metrics` object

Keep the function signature stable in v2.1.

## 3) Run the CLI
```bash
tsc examples/cellular-automata/glider.md --format text
tsc examples/cellular-automata/glider.md --format json
tsc examples/cellular-automata/random-soup.md --format json --seed 42
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
2. Compute median and MAD; set bounds to median ± 3×MAD (clip to [0,1]).
3. Update assertions in `tests/conformance/` and commit with a short note (N, seeds, machine).

## 6) Developer UX
```bash
make setup      # install dev deps
make lint       # code style
make fmt        # auto-format
make test       # run tests
make quickstart # run glider example
```

## 7) Project structure
```
/spec/              # Normative specifications
/examples/          # Positive/negative control examples
/reference/         # Reference implementation (non-stable API)
/tests/             # Conformance tests
```

See [README.md](README.md) for full navigation guide.