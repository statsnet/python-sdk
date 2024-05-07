.PHONY: fmt build publish bump-patch-version bump-minor-version bump-major-version tag-current-version
fmt:
	@black statsnet_python_sdk/
build:
	@poetry build
publish:
	@poetry publish --username __token__ --password ${PYPI_KEY} --dist-dir dist --build