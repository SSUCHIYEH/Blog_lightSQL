from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import LikeRequestSchema, LikeResponseSchema
from db.database import get_db
from db import db_like
from typing import List

router = APIRouter(
    prefix='/api/v1/likes',
    tags=['likes']
)

@router.post('', response_model=LikeResponseSchema)
def create(request: LikeRequestSchema, db: Session = Depends(get_db)):
    return db_like.create(db=db, request=request)


@router.get("/post/{post_id}", response_model=List[LikeResponseSchema])
def get_post_by_post(post_id: int, db: Session = Depends(get_db)):
    return db_like.get_like_by_post(post_id=post_id, db=db)


@router.get("/owner/{owner_id}", response_model=List[LikeResponseSchema])
def get_post_by_owner(owner_id: int, db: Session = Depends(get_db)):
    return db_like.get_like_by_owner(owner_id=owner_id, db=db)