from fastapi import FastAPI
from pathlib import Path
from dms.routes.routes import router as routes_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent  # this gives /home/babi/Desktop/document_app/dms
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(routes_router)