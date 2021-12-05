from fastapi import HTTPException, status
from router.schemas import LikeRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbLike

def create(db: Session, request: LikeRequestSchema) -> DbLike:
    new_like = DbLike(
        post_id=request.post_id,
        owner_id=request.owner_id,
        owner_img=request.owner_img,
        content=request.content,
    )
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like


def get_like_by_id(like_id: int, db: Session) -> DbLike:
    like = db.query(DbLike).filter(DbLike.id == like_id).first()
    if not like:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Like with id = {id} not found')
    return like

def get_like_by_post(post_id: int, db: Session) -> list[DbLike]:
    like = db.query(DbLike).filter(DbLike.post_id == post_id).first()
    if not like:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Like with id = {id} not found')
    return like

def get_like_by_owner(owner_id: int, db: Session) -> list[DbLike]:
    like = db.query(DbLike).filter(DbLike.owner_id == owner_id).first()
    if not like:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Like with id = {id} not found')
    return like