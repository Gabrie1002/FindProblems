import flask
import flask_restful

import src.config as app_config
import src.setups as setups


def get_app() -> flask.Flask:
    app = flask.Flask(__name__)
    api = flask_restful.Api(app)

    setups.setup_resources(api)

    return app


if __name__ == "__main__":
    app = get_app()
    app.run(
        host=app_config.FlaskConfig.HOST,
        port=app_config.FlaskConfig.PORT,
        debug=app_config.FlaskConfig.DEBUG,
    )