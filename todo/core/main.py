from fastapi import FastAPI
from app.routers import todo
from app.routers.db import engine
from app.models import model

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(todo.router)

# random
