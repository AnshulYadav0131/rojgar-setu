from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

# ─── USER SCHEMAS ───────────────────────────────────────

class UserRegister(BaseModel):
    full_name: str
    phone: str
    password: str
    role: str
    city: Optional[str] = None
    district: Optional[str] = None
    skills: Optional[str] = None

class UserLogin(BaseModel):
    phone: str
    password: str

class UserOut(BaseModel):
    id: str
    full_name: str
    phone: str
    role: str
    city: Optional[str] = None
    district: Optional[str] = None
    skills: Optional[str] = None
    is_available: bool
    created_at: datetime

    @field_validator('id', mode='before')
    def convert_id(cls, v):
        return str(v)

    class Config:
        from_attributes = True

# ─── JOB SCHEMAS ────────────────────────────────────────

class JobCreate(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    district: Optional[str] = None
    daily_pay: Optional[int] = None
    category_id: Optional[str] = None

class JobOut(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    district: Optional[str] = None
    daily_pay: Optional[int] = None
    status: str
    employer_id: str
    created_at: datetime

    @field_validator('id', 'employer_id', mode='before')
    def convert_uuids(cls, v):
        return str(v)

    class Config:
        from_attributes = True

# ─── APPLICATION SCHEMAS ────────────────────────────────

class ApplicationCreate(BaseModel):
    job_id: str

class ApplicationOut(BaseModel):
    id: str
    job_id: str
    worker_id: str
    status: str
    applied_at: datetime

    @field_validator('id', 'job_id', 'worker_id', mode='before')
    def convert_uuids(cls, v):
        return str(v)

    class Config:
        from_attributes = True

# ─── TOKEN SCHEMA ───────────────────────────────────────

class Token(BaseModel):
    access_token: str
    token_type: str