help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make setup       create virtual environment and install dependencies"
	@echo "    make activate    enter virtual environment"
	@echo "    make test        run the test suite"
	@echo "    exit             leave virtual environment"

setup:
	pip install pipenv
	pipenv install --dev --three

activate:
	pipenv shell -c

lint:
	pipenv run pylint badging tests/*
	pipenv run mypy badging tests/*
	pipenv run black badging --check
	pipenv run black tests --check

build-ci: lint test

test: export PYTHONPATH=.
test: export DJANGO_SETTINGS_MODULE=badging.badging.settings
test:
	pipenv run -- py.test tests -s -v
