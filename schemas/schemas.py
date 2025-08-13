from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

#pydantic models for validating input/output in API endpoints
class PDFDocumentBase(BaseModel):
    title: str
    author: Optional[str] = None
    keywords: Optional[List[str]] = None
    summary: Optional[str] = None
    filename: Optional[str] = None


class PDFDocumentRead(PDFDocumentBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        #set true to make pydantic work with SQLAlchemy ORM objects
        orm_mode = True
