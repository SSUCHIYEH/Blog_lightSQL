from pydantic import BaseModel


class PostRequestSchema(BaseModel):
    title: str
    author: str
    content: str


class PostResponseSchema(PostRequestSchema):
    id: int

    class Config():
        orm_mode = True
