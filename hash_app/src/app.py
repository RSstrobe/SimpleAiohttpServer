from aiohttp import web

from src.api import probes
from src.api.v1.hash import handlers


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_route("GET", "/healthcheck", probes.healthcheck_handler)
    app.router.add_route("POST", "/hash", handlers.hash_handler)

    return app
