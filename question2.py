from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/home", response_class=HTMLResponse)
async def home():
    html_page = """
    <html>
        <head>
            <title>Accueil</title>
        </head>
        <body>
            <h1>Welcome home!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_page, status_code=200)
