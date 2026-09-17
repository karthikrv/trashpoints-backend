from datetime import datetime

from pydantic import BaseModel, EmailStr

from src.users.constants import AuthProviderEnum, RoleEnum


class UserCreate(BaseModel):
  name: str
  email: EmailStr | None = None
  phone: str | None = None
  role: RoleEnum
  auth_provider: AuthProviderEnum
  auth_provider_id: str | None = None

class UserResponse(BaseModel):
  id: str
  name: str
  email: EmailStr | None = None
  phone: str | None = None
  role: RoleEnum
  auth_provider: AuthProviderEnum
  auth_provider_id: str | None = None

  class config:
    from_attributes = True
