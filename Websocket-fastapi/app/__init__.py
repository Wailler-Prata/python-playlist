from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import app_routes


app = FastAPI(docs_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(app_routes)