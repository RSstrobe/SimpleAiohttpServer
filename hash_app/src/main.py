import logging

from aiohttp import web
from aiohttp_swagger import setup_swagger

from src.app import create_app
from src.core.config import settings


def run_server(host: str = settings.app_host, port: int = settings.app_port):
    """Run the server"""
    app = create_app()
    setup_swagger(
        app=app, swagger_url="/api/openapi",
        ui_version=3, swagger_validator_url='//online.swagger.io/validator',
        description="Swagger Hash App API", api_version="1.0.0",
    )
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
