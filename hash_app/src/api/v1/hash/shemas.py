from pydantic import BaseModel


class HashRequestSchema(BaseModel):
    string: str
