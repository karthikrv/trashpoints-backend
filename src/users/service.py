import json

from fastapi import HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session

from src.users.constants import AuthProviderEnum, RoleEnum
from src.users.models import User
from src.users.schemas import ConsumerCreate


def get_current_user_details(db: Session, user_info:dict) -> User:
  user_data = db.query(User).filter(User.auth_provider_id == user_info["sub"], 
                                    or_(User.role == RoleEnum.ADMIN, User.role == RoleEnum.PARTNER) ).first()
  if not user_data:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found - Access Denied")
  return user_data

def get_current_consumer_details(db: Session, user_info:dict) -> User:
  user_data = db.query(User).filter(User.auth_provider_id == user_info["uid"], 
                                    User.auth_provider == AuthProviderEnum.FIREBASE, 
                                    User.role == RoleEnum.CONSUMER ).first()
  return user_data

def create_new_consumer(requestBody: ConsumerCreate, db: Session, user_info: dict) -> User:
  new_user = User(
    name = requestBody.name,
    auth_provider = AuthProviderEnum.FIREBASE,
    auth_provider_id = user_info["uid"],
    phone = user_info["phone_number"],
    role = RoleEnum.CONSUMER
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user