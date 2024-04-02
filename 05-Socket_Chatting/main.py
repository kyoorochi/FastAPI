from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sockets import router as socket_router
from pathlib import Path

app = FastAPI()
app.include_router(socket_router)

# 경로, HTML Response

@app.get('/')
def index():
    index_html = Path('index.html').read_text()
    return HTMLResponse(index_html)

# uvicorn main:app --reload