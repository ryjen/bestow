.PHONY: install dist test

all:
	@echo ""
	@echo "test        - run unit tests"
	@echo "install     - install the development build for testing"
	@echo "dist        - build a distribution"
	@echo ""

test:
	@python -m pytest

install:
	@pip install --editable .

dist:
	@python setup.py bdist