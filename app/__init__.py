from flask import Flask
from config import config
# from flask_cors import CORS
# import create_response


def create_app(config_name):
    app = Flask(__name__)
    print(f"app-init: {__name__}")
    print("app-init:", __name__ == "__main__")

    app.config.from_object(config[config_name])
    # CORS(app)

    from .apiv1 import api as apiv1_blueprint
    app.register_blueprint(apiv1_blueprint, url_prefix="/v1")

    return app
