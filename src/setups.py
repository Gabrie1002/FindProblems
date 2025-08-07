import flask_restful

from src.api import v1_resources


def setup_resources(api: flask_restful.Api):
    for resource, path in v1_resources.items():
        api.add_resource(resource, "/v1" + path)