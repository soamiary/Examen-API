from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# Ton handler personnalisé pour les erreurs 404
@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        html_404 = """
        <html>
            <head><title>404 NOT FOUND</title></head>
            <body>
                <h1>404 NOT FOUND</h1>
            </body>
        </html>
        """
        return HTMLResponse(content=html_404, status_code=404)
    # Pour les autres erreurs, renvoyer l'exception par défaut
    return await app.default_exception_handler(request, exc)
