.PHONY: all coverage pep8 test


test: dbdowngrade dbupgrade
	pytest

coverage: dbdowngrade dbupgrade
	pytest --cov=api --cov-report html

pep8:
	flake8 --max-line-length 99 --max-complexity 9 api

dbupgrade:
	alembic upgrade head

dbdowngrade:
	alembic downgrade base

all: pep8 coverage
