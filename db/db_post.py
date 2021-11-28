from router.schemas import PostRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbPost
from .posts_feed import posts

def db_feed(db: Session):
    new_post_list = [DbPost(
        title=post["title"],
        author=post["author"],
        content=post["content"],
        ownerID=post["ownerID"]
    ) for post in posts]
    db.query(DbPost).delete()
    db.commit()
    db.add_all(new_post_list)
    db.commit()
    return db.query(DbPost).all()

def create(db: Session, request: PostRequestSchema) -> DbPost:
    new_product = DbPost(
        title=request.title,
        author=request.author,
        content=request.content,
        ownerID=request.ownerID
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all(db: Session) -> list[DbPost]:
    return db.query(DbPost).all()


def get_post_by_id(post_id: int, db: Session):
    return db.query(DbPost).filter(DbPost.id == post_id).first()


def get_post_by_author(
        author: str,
        db: Session):
    return db.query(DbPost).filter(DbPost.author == author).all()
