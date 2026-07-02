from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.base import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(Integer,
                       ForeignKey("resumes.id"))

    skill_name = Column(String)