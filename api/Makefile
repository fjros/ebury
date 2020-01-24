.PHONY: all coverage pep8 test


test:
	pytest

coverage:
	pytest --cov=api --cov-report html

pep8:
	flake8 --max-line-length 99 --max-complexity 9 api

all: pep8 coverage
