from pydantic import BaseModel
from typing import List

class CommentRequestSchema(BaseModel):
    product_id: int
    owner_name: str
    content: str

class LikeRequestSchema(BaseModel):
    post_id: int
    owner_img: str
    owner_id: int
    content: str

class PostRequestSchema(BaseModel):
    title: str
    author: str
    content: str
    owner_id: int

class UserRequestSchema(BaseModel):
    username: str
    email: str
    password: str


class OnlyUserResponseSchema(UserRequestSchema):
    pass

    class Config:
        orm_mode = True


class OnlyPostResponseSchema(PostRequestSchema):
    pass

    class Config:
        orm_mode = True

class CommentResponseSchema(CommentRequestSchema):
    id: int
    product_id: int
    owner_id: int
    product: OnlyPostResponseSchema

    class Config:
        orm_mode = True

class LikeResponseSchema(LikeRequestSchema):
    id: int
    product_id: int
    owner_id: int
    product: OnlyPostResponseSchema
    owner: OnlyUserResponseSchema

    class Config:
        orm_mode = True

class PostResponseSchema(PostRequestSchema):
    id: int
    owner_id: int
    all_likes: List[LikeResponseSchema] = []
    created_comments: List[CommentResponseSchema] = []

    class Config:
        orm_mode = True

class UserResponseSchema(UserRequestSchema):
    id: int
    created_products: List[PostResponseSchema] = []
    created_Likes: List[LikeResponseSchema] = []

    class Config:
        orm_mode = True

