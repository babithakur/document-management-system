from fastapi import APIRouter
from fastapi import FastAPI, Request, UploadFile, File, Form, Depends, HTTPException, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from dms.utils.pdf_utils import extract_pdf_metadata
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_400_BAD_REQUEST
from dms.dependencies.dependencies import get_session
from dms.models.models import PDFDocument
from sqlalchemy.future import select
from pathlib import Path
from sqlalchemy import and_
import os

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/add_document", response_class=HTMLResponse)
async def add_doc_page(request: Request, success: str = None):
    return templates.TemplateResponse(
        "add_document.html",
        {"request": request, "success": success}
    )


@router.post("/add_document", response_class=HTMLResponse)
async def upload_document(
    request: Request,
    title: str = Form(...),
    file: UploadFile = File(...),
    session: AsyncSession = Depends(get_session),
):
    #title validation
    if not title.strip():
       return templates.TemplateResponse(
            "add_document.html",
            {"request": request, "error": "Please enter the document title."},
            status_code=400,
        )

    #pdf file type validation
    if file.content_type != "application/pdf":
        return templates.TemplateResponse(
            "add_document.html",
            {"request": request, "error": "Only PDF files are allowed."},
            status_code=400,
        )
    #saving file to upload directory
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        contents = await file.read()
        f.write(contents)

    #extracting metadata from saved PDF
    metadata = extract_pdf_metadata(file_location)

    #using extracted title if missing, else fall back to form title
    doc_title = metadata.get("title") or title

    #adding into database
    new_doc = PDFDocument(
        title=doc_title,
        author=metadata.get("author"),
        keywords=metadata.get("keywords"),
        summary=metadata.get("summary"),
        created_at=metadata.get("created_at"),
        filename=file.filename,
    )

    session.add(new_doc)
    await session.commit()
    await session.refresh(new_doc)

    #success response
    context = {"request": request, "message": "Document uploaded successfully", "document": new_doc}
    return RedirectResponse(url="/add_document?success=Document uploaded successfully.", status_code=303)

@router.get("/list_documents", response_class=HTMLResponse)
async def list_documents(
    request: Request,
    session: AsyncSession = Depends(get_session),
    author: str = Query(None),
    keyword: str = Query(None),
    date_from: str = Query(None),
    date_to: str = Query(None),
):
    query = select(PDFDocument)
    filters = []

    if author:
        filters.append(PDFDocument.author.ilike(f"%{author}%"))

    if keyword:
        filters.append(PDFDocument.keywords.any(keyword))  

    if date_from:
        try:
            date_from_parsed = datetime.strptime(date_from, "%Y-%m-%d")
            filters.append(PDFDocument.created_at >= date_from_parsed)
        except ValueError:
            pass  

    if date_to:
        try:
            date_to_parsed = datetime.strptime(date_to, "%Y-%m-%d")
            filters.append(PDFDocument.created_at <= date_to_parsed)
        except ValueError:
            pass

    if filters:
        query = query.where(and_(*filters))

    result = await session.execute(query)
    pdfs = result.scalars().all()

    return templates.TemplateResponse("list_documents.html", {
        "request": request,
        "pdfs": pdfs,
        "filters": {
            "author": author or "",
            "keyword": keyword or "",
            "date_from": date_from or "",
            "date_to": date_to or ""
        }
    })