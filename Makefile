.PHONY: fmt build publish bump-patch-version bump-minor-version bump-major-version
fmt:
	@black statsnet-python-sdk/
build:
	@poetry build
publish:
	@poetry publish --username __token__ --password ${PYPI_KEY} --dist-dir dist --build
bump-patch-version:
	@poetry version patch
bump-minor-version:
	@poetry version minor
bump-major-version:
	@poetry version major