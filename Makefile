all: init build

init:
	pip install poetry
	poetry install
build: 
	poetry build
publish:
	poetry publish
publish-test:
	poetry publish -r testpypi
.PHONY: all init build publish
