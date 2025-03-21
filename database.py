from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.user import User
from models.post import Post
from models.base import Base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, echo=True)
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
