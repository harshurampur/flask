from flask import Flask, request

from .config import app_config
from flask import render_template


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    req = "unknown"

    @app.route('/', methods=["GET", "POST"])
    def index():
        """
        example endpoint
        """
        if request.form:
            print(request.form["product_name"])

        return render_template("home.html")
    return app, req
