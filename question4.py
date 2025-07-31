from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime
from fastapi.responses import JSONResponse

app = FastAPI()

posts_memory = []

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

@app.post("/posts")
async def add_posts(new_posts: List[Post]):
    posts_memory.extend(new_posts)
    return JSONResponse(content=[post.dict() for post in posts_memory], status_code=201)
