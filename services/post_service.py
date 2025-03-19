from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from models.models import User
from models.models import Post
from schemas.user import UserCreate
from schemas.post import PostCreate




def create_post(db: Session, post_data: PostCreate, user_id: int):
    db_post = Post(text=post_data.text, user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int, user_id: int):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False
