all: init build

init:
	pip install poetry
	poetry install
build: 
	poetry build
publish:
	poetry publish --username  tanbokan --password  u9YfXRkFhePADyh
publish-test:
	poetry publish -r testpypi
.PHONY: all init build publish
