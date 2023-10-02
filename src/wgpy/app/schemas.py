from pydantic import BaseModel


class BodyModel(BaseModel):
    arg1: str


class ResponseModel(BaseModel):
    arg1: str
