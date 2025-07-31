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

@app.put("/posts")
async def put_posts(new_posts: List[Post]):
    for new_post in new_posts:
        for i, stored_post in enumerate(posts_memory):
            if stored_post["title"] == new_post.title:
                if stored_post != new_post.dict():
                    posts_memory[i] = new_post.dict()
                break
        else:
            posts_memory.append(new_post.dict())
    return JSONResponse(content=posts_memory, status_code=200)
