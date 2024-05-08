.PHONY: fmt build publish
fmt:
	@black statsnet_python_sdk/
build:
	@poetry build
publish:
	@poetry publish --username __token__ --password ${PYPI_KEY} --dist-dir dist --build
generate-models:
	@datamodel-codegen --input-file-type openapi --output ./statsnet_python_sdk/models.py --output-model-type typing.TypedDict --input ${SWAGGER_PATH}