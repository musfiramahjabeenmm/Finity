from sqlalchemy import Column, String, DateTime, Date, Boolean, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from pgvector.sqlalchemy import Vector
import uuid
from datetime import datetime
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True), nullable=False)
    date = Column(Date, nullable=False)
    description = Column(Text, nullable=True)
    amount = Column(Numeric(15, 2), nullable=False)
    type = Column(String(10), nullable=False)        # debit | credit
    category = Column(String(100), nullable=True)
    vendor = Column(String(255), nullable=True)
    gst_applicable = Column(Boolean, default=False)
    hsn_code = Column(String(10), nullable=True)
    embedding = Column(Vector(1536), nullable=True)  # for RAG
    created_at = Column(DateTime, default=datetime.utcnow)