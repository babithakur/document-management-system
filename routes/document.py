from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

document = APIRouter()
templates = Jinja2Templates(directory="templates")

@document.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@document.get("/add_document", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("add_document.html", {"request": request})
