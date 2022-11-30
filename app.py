from fastapi import FastAPI
from config.db import db
from routes.user import user as userRouter

app = FastAPI(
    title="FastAPI with MongoDB",
    description="Just some description to see..."
)

@app.get('/')
def index():
    return {"msg": "Hello world!"}

app.include_router(userRouter)