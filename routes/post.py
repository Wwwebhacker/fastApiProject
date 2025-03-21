from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse
from schemas.post import PostCreate, PostCreateResponse, PostResponse
from services import auth_service, post_service
from database import get_db
from utils.token_handler import get_current_user
from utils.cache import get_cached_posts, set_cached_posts

router = APIRouter()

@router.post("/", response_model=PostCreateResponse)
def add_post(post_data: PostCreate, current_user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    new_post = post_service.create_post(db, post_data, current_user.id)
    set_cached_posts(current_user.id, post_service.get_posts(db, current_user.id))
    return {"postId":new_post.id}

@router.get("/", response_model=list[PostResponse])
def get_posts(current_user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    cached_posts = get_cached_posts(current_user.id)
    if cached_posts:
        return cached_posts
    posts = post_service.get_posts(db, current_user.id)
    set_cached_posts(current_user.id, posts)
    return posts

@router.delete("/{post_id}")
def delete_post(post_id: int, current_user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    if not post_service.delete_post(db, post_id, current_user.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found or unauthorized")
    set_cached_posts(current_user.id, post_service.get_posts(db, current_user.id))
    return {"message": "Post deleted successfully"}