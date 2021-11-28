# from .database import Base
# from sqlalchemy import Column, Integer, String
#
#
# # class DbProduct(Base):
# #     __tablename__ = 'product'
# #     id = Column(Integer, primary_key=True, index=True)
# #     name = Column(String)
# #     price = Column(Integer)
# #     image = Column(String)
# #     description = Column(String)
# #     currency = Column(String)
# #     countInStock = Column(Integer)
# #     category = Column(String)
#
# class DbBlog(Base):
#     __tablename__ = 'blog'
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     author = Column(String)
#     content = Column(String)

from .database import Base
from sqlalchemy import Column, Integer, String


class DbPost(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)