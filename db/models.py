from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbPost(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String, ForeignKey('user.username'))
    content = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates='created_posts')
    created_comments = relationship('DbComment', back_populates='post')
    all_likes = relationship('DbLike', back_populates='post')


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created_posts = relationship('DbPost', back_populates='owner')
    created_Likes = relationship('DbLike', back_populates='owner')
    user_img = Column(String)


class DbLike(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, index=True)
    post = relationship('DbPost', back_populates='all_likes')
    post_id = Column(Integer, ForeignKey('posts.id'))
    owner_img = Column(String, ForeignKey('user.user_img'))
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates='created_Likes')
    content = Column(String)


# comment to owner
# comment to product
# product to comment

class DbComment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('DbPost', back_populates='created_comments')
    owner_name = Column(String, ForeignKey('user.username'))
    content = Column(String)
