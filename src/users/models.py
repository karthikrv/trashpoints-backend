import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, func
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
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
    kiosk_id = Column(String(255), ForeignKey("kiosk.id"),nullable=True)
    
    assigned_kiosk = relationship("Kiosk", back_populates='partners')
    dropped_events = relationship("DropOffEvent", foreign_keys="DropOffEvent.depositor_id", back_populates="dropped_by")
    collected_events = relationship("DropOffEvent", foreign_keys="DropOffEvent.collector_id", back_populates="collected_by")
    transactions = relationship("PointTransaction", back_populates="depositor")
    redemptions = relationship("Redemption", back_populates="depositor")