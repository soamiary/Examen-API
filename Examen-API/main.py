from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/ping")
def ping():
    return Response(content="pong", media_type="text/plain")
