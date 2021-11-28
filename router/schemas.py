from pydantic import BaseModel
from typing import List

class PostRequestSchema(BaseModel):
    title: str
    author: str
    content: str
    ownerID: int

class UserRequestSchema(BaseModel):
    username: str
    email: str
    password: str


class PostResponseSchema(PostRequestSchema):
    id: int
    ownerID: int

    class Config():
        orm_mode = True

class UserResponseSchema(UserRequestSchema):
    id: int
    created_products: List[PostResponseSchema] = []

    class Config:
        orm_mode = True