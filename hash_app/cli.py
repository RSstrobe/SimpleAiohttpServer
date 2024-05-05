import click

from src.core.config import settings
from src.main import run_server


@click.command("run_server")
@click.option('--host', prompt='Application host',
              help='Application host.', type=str, default=settings.app_host)
@click.option('--port', prompt='Application port',
              help='Application port.', type=int, default=settings.app_post)
def run(host: str, port: int):
    """Run the server"""
    run_server(host, port)


if __name__ == "__main__":
    run()
