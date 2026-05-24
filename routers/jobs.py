from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from auth import get_current_user
import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.JobOut)
def create_job(
    job: schemas.JobCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "employer":
        raise HTTPException(status_code=403, detail="Only employers can post jobs")

    new_job = models.Job(
        employer_id=current_user.id,
        title=job.title,
        description=job.description,
        location=job.location,
        district=job.district,
        daily_pay=job.daily_pay,
        category_id=job.category_id
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.get("/", response_model=List[schemas.JobOut])
def get_jobs(
    district: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Job).filter(models.Job.status == "open")
    if district:
        query = query.filter(models.Job.district == district)
    return query.order_by(models.Job.created_at.desc()).all()

@router.get("/{job_id}", response_model=schemas.JobOut)
def get_job(job_id: str, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/{job_id}/apply", response_model=schemas.ApplicationOut)
def apply_job(
    job_id: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "worker":
        raise HTTPException(status_code=403, detail="Only workers can apply for jobs")

    already_applied = db.query(models.Application).filter(
        models.Application.job_id == job_id,
        models.Application.worker_id == current_user.id
    ).first()
    if already_applied:
        raise HTTPException(status_code=400, detail="You have already applied for this job")

    application = models.Application(
        job_id=job_id,
        worker_id=current_user.id
    )
    db.add(application)
    db.commit()
    db.refresh(application)
    return application

@router.get("/{job_id}/applicants", response_model=List[schemas.ApplicationOut])
def get_applicants(
    job_id: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if str(job.employer_id) != str(current_user.id):
        raise HTTPException(status_code=403, detail="Not your job")

    return db.query(models.Application).filter(models.Application.job_id == job_id).all()