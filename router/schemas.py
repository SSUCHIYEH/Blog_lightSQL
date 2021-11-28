# from pydantic import BaseModel
#
#
# # 處理ProductAPI的HTTP Request
# class PostRequestSchema(BaseModel):
#     title = str
#     author = str
#     content = str
#
#
# # 處理HTTP response資料轉換
# class PostResponseSchema(PostRequestSchema):
#     id: int
#     class Config():
#         orm_mode = True

from pydantic import BaseModel


class PostRequestSchema(BaseModel):
    title: str
    author: str
    content: str


class PostResponseSchema(PostRequestSchema):
    id: int

    class Config():
        orm_mode = True
