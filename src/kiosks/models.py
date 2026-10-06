import uuid

from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String, func)
from sqlalchemy.orm import relationship

from src.database import Base


class Kiosk(Base):
  __tablename__ = 'kiosk'

  id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
  name = Column(String(255), nullable=False)
  address = Column(String(255), nullable=True)
  latitude = Column(Float, nullable=False)
  longitude = Column(Float, nullable=False)
  opening_time = Column(String(255), nullable=False)
  closing_time = Column(String(255), nullable=False)
  status = Column(String(255), nullable=False, default="open")
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

  partners = relationship("User", back_populates="assigned_kiosk")
  drop_off_events = relationship("DropOffEvent", back_populates="dropped_at")

class DropOffEvent(Base):
  __tablename__ = 'drop_off_event'

  id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
  total_points = Column(Integer, nullable=True)
  kiosk_id = Column(String(255), ForeignKey("kiosk.id"), nullable=False)
  collector_id = Column(String(255), ForeignKey("user.id"), nullable=False)
  depositor_id = Column(String(255), ForeignKey("user.id"), nullable=False)
  status = Column(String(255), nullable=False, default="open")
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

  dropped_at = relationship("Kiosk", back_populates="drop_off_events")
  dropped_by = relationship("User", foreign_keys=[depositor_id], back_populates="dropped_events")
  collected_by = relationship("User", foreign_keys=[collector_id], back_populates="collected_events")
  dropped_items = relationship("DropOffEventItem", back_populates="drop_off_event")
  transactions = relationship("PointTransaction", back_populates="drop_off_event")

class DropOffEventItem(Base):
  __tablename__ = 'drop_off_event_item'

  id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
  waste_type = Column(String(255), nullable=False)
  points = Column(Integer, nullable=True)
  weight = Column(Float, nullable=True)
  drop_off_event_id = Column(String(255), ForeignKey("drop_off_event.id"), nullable=False)
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

  drop_off_event = relationship("DropOffEvent", back_populates="dropped_items")

class PointTransaction(Base):
  __tablename__ = 'point_transaction'

  id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
  depositor_id = Column(String(255), ForeignKey("user.id"), nullable=False)
  type = Column(String(255), nullable=False)
  points = Column(Integer, nullable=False)
  drop_off_event_id = Column(String(255), ForeignKey("drop_off_event.id"), nullable=True, unique=True)
  redemption_id = Column(String(255), ForeignKey("redemption.id"), nullable=True, unique=True)
  description = Column(String(255), nullable=True)
  created_at = Column(DateTime, server_default=func.now())

  drop_off_event = relationship("DropOffEvent", back_populates="transactions")
  depositor = relationship("User", back_populates="transactions")
  redemption = relationship("Redemption", back_populates='transactions')

class Redemption(Base):
  __tablename__ = 'redemption'

  id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
  depositor_id = Column(String(255), ForeignKey("user.id"), nullable=False)
  points = Column(Integer, nullable=False)
  type = Column(String(255), nullable=False)
  status = Column(String(255), nullable=False, default="pending")
  redeemed_at = Column(DateTime, nullable=True)
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

  depositor = relationship("User", back_populates="redemptions")
  transactions = relationship("PointTransaction", back_populates="redemption")
