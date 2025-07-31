from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def not_found(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return HTMLResponse("<h1>404 NOT FOUND</h1>", status_code=404)
    raise exc  
