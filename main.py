from fastapi import FastAPI
from src.routes.api import summarization
from src.routes.api import translation

app = FastAPI()
app.include_router(summarization.router)
app.include_router(translation.router)


@app.get("/")
def root():
    return {"res": "FastAPI is up and running!"}
