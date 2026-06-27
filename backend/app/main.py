from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Career OS"}


@app.get("/health")
def health():
    return {"status": "running"}