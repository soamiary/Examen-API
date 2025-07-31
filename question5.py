from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

posts_memory = []

@app.get("/posts")
async def get_posts():
    return JSONResponse(content=posts_memory, status_code=200)
