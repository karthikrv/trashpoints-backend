from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.users import models, schemas
from src.users import service as user_service
from src.users.dependencies import (create_consumer_details,
                                    resolve_consumer_details,
                                    resolve_user_org_details,
                                    verify_internal_secret)
from src.users.schemas import AuthRequest, ConsumerCreate, ProvisionRequest

router = APIRouter(prefix='/users', tags=["users"])

@router.post("/", response_model=schemas.UserResponse, status_code=201)
async def create_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
  new_user = models.User(**user_data.model_dump())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@router.post("/resolve", status_code=200)
async def verify_google(user_org_details: dict = Depends(resolve_user_org_details)):
    return {
        "status": "success",
        "data": user_org_details
      }

@router.post("/resolve-consumer", status_code=200)
async def verify_consumer(user_consumer_details: dict = Depends(resolve_consumer_details)):
  if not user_consumer_details:
    return { "isAuthorised" : False, "user" : None }
  return { "isAuthorised" : True, "user" : user_consumer_details }

@router.post("/signup-consumer", status_code=201)
async def create_new_consumer_details(new_user : dict = Depends(create_consumer_details)):
  return { "status" : "success", "user" : new_user }

@router.post("/provision", response_model=schemas.UserResponse, status_code=201)
async def provision_user(data: schemas.ProvisionRequest, db: Session = Depends(get_db), _: None = Depends(verify_internal_secret)):
  return user_service.create_provisioned_user(db=db, data=data)