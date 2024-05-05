import json
from functools import wraps
from typing import Type

from aiohttp import web
from pydantic import BaseModel, ValidationError

TypeSchema = Type[BaseModel]


def deserialize_request_handler(schema: TypeSchema):
    def wrapper_handler(func):
        @wraps(func)
        async def wrapper(request: web.Request):
            request_data = await request.json()
            try:
                validate_data = schema(**request_data)
            except ValidationError as e:
                raise web.HTTPBadRequest(body=json.dumps({"error_type": "validation_errors", "error": str(e)}))
            response = await func(request, validate_data.model_dump())
            return response

        return wrapper

    return wrapper_handler
