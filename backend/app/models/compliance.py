from sqlalchemy import Column, String, DateTime, Date, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.database import Base

class ComplianceAlert(Base):
    __tablename__ = "compliance_alerts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True), nullable=False)
    alert_type = Column(String(50), nullable=True)   # GST | TDS | HSN | PF | ESI
    message = Column(Text, nullable=True)
    due_date = Column(Date, nullable=True)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)