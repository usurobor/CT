# Simple developer UX for v2.1
.PHONY: help setup lint fmt test quickstart linkcheck

help:
	@echo "Common targets:"
	@echo "  setup       - pip install -e .[dev]"
	@echo "  lint        - ruff check ."
	@echo "  fmt         - ruff format . && mdformat ."
	@echo "  test        - pytest"
	@echo "  quickstart  - run the glider example via CLI"
	@echo "  linkcheck   - check Markdown links (requires lychee)"

setup:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

lint:
	ruff check .

fmt:
	ruff format .
	mdformat .

test:
	pytest

quickstart:
	tsc examples/cellular-automata/glider.md --format text || true

linkcheck:
	@command -v lychee >/dev/null 2>&1 \
		&& lychee --verbose --no-progress --max-concurrency 4 --accept 200..299,403,429 -- *.md **/*.md \
		|| (echo "lychee not installed; run link check in GitHub Actions or 'cargo install lychee' locally." && exit 0)