.PHONY: fmt build
fmt:
	@black statsnet-python-sdk/
build:
	@poetry build
publish:
	@poetry publish --username __token__ --password ${PYPI_KEY} --dist-dir dist --build