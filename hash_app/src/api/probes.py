from aiohttp import web


async def healthcheck_handler(_: web.Request) -> web.Response:
    """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Health check
    produces:
    - application/json
    responses:
        "200":
            description: successful operation.
            content:
              application/json:
                schema:
                  type: object
    """
    return web.json_response(data={}, status=web.HTTPOk.status_code)
