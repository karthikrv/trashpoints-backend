from enum import StrEnum


class KioskStatusEnum(StrEnum):
  OPEN = "open"
  CLOSED = "closed"
  MAINTENANCE = "maintenance"

class DropOffStatusEnum(StrEnum): 
  OPEN = "open"
  COMPLETED = "completed"
  CANCELLED = "cancelled"

class TransactionTypeEnum(StrEnum): 
  EARN = "earn"
  REDEEM = "redeem"
  ADJUSTMENT = "adjustment"
  EXPIRE = "expire"

class RedemptionStatusEnum(StrEnum): 
  PENDING = "pending"
  COMPLETED = "completed"
  FAILED = "failed"

class RedemptionTypeEnum(StrEnum): 
  VOUCHER = "voucher"
  TAX_CREDIT = "tax_credit"

class WasteTypeEnum(StrEnum): 
  DRY = "dry"
  WET = "wet"
  E_WASTE = "e_waste"