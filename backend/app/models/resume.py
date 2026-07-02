from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer,
                     ForeignKey("users.id"))

    file_name = Column(String)

    file_path = Column(String)

    uploaded_at = Column(DateTime(timezone=True),
                         server_default=func.now())