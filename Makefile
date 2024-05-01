.PHONY: fmt build publish bump-patch-version bump-minor-version bump-major-version
fmt:
	@black statsnet-python-sdk/
build:
	@poetry build
publish:
	@poetry publish --username __token__ --password ${PYPI_KEY} --dist-dir dist --build
tag-current-version:
	@git tag -a $(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)
bump-patch-version:
	@poetry version patch && $(MAKE) tag-current-version
bump-minor-version:
	@poetry version minor && $(MAKE) tag-current-version
bump-major-version:
	@poetry version major && $(MAKE) tag-current-version