from fastapi import FastAPI
from app.api import resume
from app.database.base import Base
from app.database.database import engine
import app.models


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(
    resume.router,
    prefix="/resume",
    tags=["Resume"]
)


@app.get("/")
def root():
    return {
        "message": "AI Career OS"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created.")