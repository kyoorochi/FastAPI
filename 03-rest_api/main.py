from fastapi import FastAPI
from routes.users import router as user_router
from routes.items import router as item_router
import uvicorn

app = FastAPI()

app.include_router(user_router) # Django -> settings.py, urls.py
app.include_router(item_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True) # python main.py