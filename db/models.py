from .database import Base
from sqlalchemy import Column, Integer, String


class DbPost(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)