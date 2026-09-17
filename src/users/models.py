from sqlalchemy import Boolean, Column, DateTime, String, func
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True, unique=True)
    email = Column(String(255), nullable=True, unique=True)
    name = Column(String(255))
    phone = Column(String(20), nullable=True, unique=True)
    password_hash = Column(String, nullable=True)
    email_verified = Column(DateTime, nullable=True)
    image = Column(String, nullable=True)
    role = Column(String, nullable=False)
    auth_provider = Column(String, nullable=False)
    auth_provider_id = Column(String, nullable=True)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())