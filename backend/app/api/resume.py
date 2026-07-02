from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends
)
from sqlalchemy.orm import Session
from pathlib import Path
from app.database.database import get_db
from app.models.resume import Resume
import shutil
import uuid

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Check duplicate
    existing = db.query(Resume).filter(
        Resume.file_name == file.filename,
        Resume.user_id == 1
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="File already exists."
        )

    # Generate unique filename
    file_id = uuid.uuid4()
    extension = file.filename.split(".")[-1]
    filename = f"{file_id}.{extension}"
    file_path = UPLOAD_DIR / filename

    # Save file
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="File upload failed."
        )

    # Save metadata
    resume = Resume(
        user_id=1,
        file_name=file.filename,
        file_path=str(file_path)
    )

    try:
        db.add(resume)
        db.commit()
        db.refresh(resume)

    except Exception as e:
        db.rollback()
        print("DATABASE ERROR:", e)

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume.id
    }