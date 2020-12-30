.PHONY: install dist test

all:
	@echo ""
	@echo "test        - run unit tests"
	@echo "install     - install the development build for testing"
	@echo "dist        - build a distribution"
	@echo "clean       - clean a build"
	@echo ""

test:
	@python -m pytest

lint:
	@python -m pylint bestow

clean:
	@find . -type d -name "__pycache__" | grep -v "site-packages" | xargs rm -rf
	@find . -type f -name "*.pyc" | grep -v "site-packages" | xargs rm -f

install:
	@pip install --editable .

dist:
	@python setup.py bdist