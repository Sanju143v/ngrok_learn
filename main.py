from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI User API")

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

app.include_router(user_routes.router)
