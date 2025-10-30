# Simple developer UX for v2.1
.PHONY: help setup lint fmt test quickstart linkcheck

# Detect Python command
PYTHON := $(shell command -v python3.11 2>/dev/null || command -v python3 2>/dev/null || command -v python 2>/dev/null)
PIP := $(PYTHON) -m pip

help:
	@echo "Common targets:"
	@echo "  setup       - pip install -e .[dev]"
	@echo "  lint        - ruff check ."
	@echo "  fmt         - ruff format . && mdformat ."
	@echo "  test        - pytest"
	@echo "  quickstart  - run the glider example via CLI"
	@echo "  linkcheck   - check Markdown links (requires lychee)"

setup:
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

lint:
	$(PYTHON) -m ruff check .

fmt:
	$(PYTHON) -m ruff format .
	$(PYTHON) -m mdformat . --exclude spec/tsc-operational.md

test:
	$(PYTHON) -m pytest

quickstart:
	$(PYTHON) -m reference.cli.tsc examples/cellular-automata/glider.md --format text || true

linkcheck:
	@command -v lychee >/dev/null 2>&1 \
		&& lychee --verbose --no-progress --max-concurrency 4 --accept 200..299,403,429 -- *.md **/*.md \
		|| (echo "lychee not installed; run link check in GitHub Actions or 'cargo install lychee' locally." && exit 0)