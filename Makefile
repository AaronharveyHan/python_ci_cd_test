.PHONY: install test lint format

install:
	pip install -r requirements.txt

test:
	pytest -v

test-cov:
	pytest --cov=src --cov-report=term-missing -v

lint:
	flake8 src/ tests/
	black --check src/ tests/

format:
	black src/ tests/
