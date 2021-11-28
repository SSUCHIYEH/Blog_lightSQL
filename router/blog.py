from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import PostRequestSchema, PostResponseSchema
from db.database import get_db
from db import db_post
from typing import List

router = APIRouter(
    prefix='/api/v1/posts',
    tags=['posts']
)


@router.post('', response_model=PostResponseSchema)
def create(request: PostRequestSchema, db: Session = Depends(get_db)):
    return db_post.create(db=db, request=request)


@router.get('/all', response_model=List[PostResponseSchema])
def get_all_post(db: Session = Depends(get_db)):
    return db_post.db_feed(db)


@router.get('/id/{post_id}}', response_model=PostResponseSchema)
def get_post_by_id(post_id: str, db: Session = Depends(get_db)):
    return db_post.get_post_by_id(post_id=post_id, db=db)


@router.get("/{author}", response_model=List[PostResponseSchema])
def get_post_by_author(author: str, db: Session = Depends(get_db)):
    return db_post.get_post_by_author(author=author, db=db)

