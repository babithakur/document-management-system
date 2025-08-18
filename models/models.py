from sqlalchemy import Column, Integer, Text, TIMESTAMP, text, ARRAY, Float
from sqlalchemy.orm import declarative_base

#SQLAlchemy models (i.e., table definitions)
Base = declarative_base()

class PDFDocument(Base):
    __tablename__ = "pdf_documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    author = Column(Text)
    keywords = Column(ARRAY(Text))
    summary = Column(Text)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Kathmandu'"))
    filename = Column(Text)
    embedding = Column(ARRAY(Float), nullable=True)


