from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.database import Base

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True), nullable=False)
    role = Column(String(10), nullable=False)        # user | assistant
    content = Column(Text, nullable=False)
    agent_used = Column(String(50), nullable=True)   # which agent responded
    created_at = Column(DateTime, default=datetime.utcnow)