.PHONY: install install-dev lint format test strip-notebooks check-notebooks

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pre-commit install

lint:
	ruff check src scripts tests

format:
	black src scripts tests

test:
	pytest

strip-notebooks:
	python scripts/strip_notebook_outputs.py

check-notebooks:
	python scripts/strip_notebook_outputs.py --check
