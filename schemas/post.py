from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

class PostCreate(BaseModel):
    text: str = Field(..., max_length=1024)

class PostResponse(BaseModel):
    id: int
    text: str
    user_id: int
    created_at: datetime

class PostCreateResponse(BaseModel):
    postId: int
