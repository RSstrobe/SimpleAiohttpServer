from aiohttp import web

from src.api.utils.validator import deserialize_request_handler
from src.api.v1.hash.shemas import HashRequestSchema
from src.core.deps import get_hash_service
from src.services.hash_service import HashService


@deserialize_request_handler(schema=HashRequestSchema)
async def hash_handler(
        _: web.Request, data: dict, hash_service: HashService = get_hash_service()
) -> web.Response:
    """
    ---
    description: This end-point allow to hash a string.
    tags:
    - Hash
    consumes:
    - application/json
    produces:
    - application/json
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              string:
                type: string
                items:
                  type: string
                example: may
            required:
              - string
          example:
            {"string": "may"}
    responses:
        "200":
            description: successful operation
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    hash_string:
                      type: string
                      example: 7a9feafae8e47af12864465eabd67466193c3b1bec30de84752c2e227c769410
        "400":
            description: validation_errors
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error_type:
                      type: string
                      example: validation_errors
                    error:
                      type: string
    """
    response = hash_service.hash_string(data["string"])
    return web.json_response(
        {"hash_string": response}
    )
