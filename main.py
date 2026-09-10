from flask import redirect
from flask_cors import CORS
from flask_openapi3.models.info import Info
from flask_openapi3.openapi import OpenAPI


def create_app(database_uri: str | None = None) -> OpenAPI:
    app = OpenAPI(__name__, info=Info(title="DealHunter API", version="0.1.0"))

    if database_uri is not None:
        app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vault.db"

    CORS(app)

    @app.route("/")
    def root() -> str:
        return "Hello World"

    @app.route("/docs")
    def docs_redirect():
        return redirect("/openapi/swagger", code=302)

    return app
