from fastapi import FastAPI
from routes import auth, post


app = FastAPI(title="App", version="1.0.0")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(post.router, prefix="/posts", tags=["Posts"])

@app.get("/")
def root():
    return {"message": "Welcome"}