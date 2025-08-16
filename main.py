from fastapi import FastAPI
from pathlib import Path
from dms.routes.routes import router as routes_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent  
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.mount("/uploads", StaticFiles(directory=BASE_DIR / "uploaded_pdfs"), name="uploads")
app.include_router(routes_router)