from cachetools import TTLCache
from typing import List
from models.post import Post

posts_cache = TTLCache(maxsize=100, ttl=300)

def get_cached_posts(user_id: int) -> List[Post] | None:
    return posts_cache.get(user_id)

def set_cached_posts(user_id: int, posts: List[Post]):
    posts_cache[user_id] = posts