from pydantic import BaseModel


class Message(BaseModel):
    message: str


class User(BaseModel):
    usuario: str
