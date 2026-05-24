from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models, schemas, auth

router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserRegister, db: Session = Depends(get_db)):
    # Check if phone already exists
    existing = db.query(models.User).filter(models.User.phone == user.phone).first()
    if existing:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    # Create new user
    new_user = models.User(
        full_name=user.full_name,
        phone=user.phone,
        password_hash=auth.hash_password(user.password),
        role=user.role,
        city=user.city,
        district=user.district,
        skills=user.skills
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    new_user.id = str(new_user.id)
    return new_user

@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    # Find user by phone
    db_user = db.query(models.User).filter(models.User.phone == user.phone).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid phone or password")

    # Check password
    if not auth.verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid phone or password")

    # Create token
    access_token = auth.create_access_token(data={"sub": db_user.phone})
    return {"access_token": access_token, "token_type": "bearer"}