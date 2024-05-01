.PHONY: fmt build
fmt:
	black statsnet-python-sdk/
build:
	poetry build