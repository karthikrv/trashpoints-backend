from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.users import models, schemas

router = APIRouter(prefix='/users', tags=["users"])

@router.post("/", response_model=schemas.UserResponse, status_code=201)
async def create_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
  new_user = models.User(**user_data.model_dump())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user