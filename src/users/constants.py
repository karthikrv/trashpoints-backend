from enum import StrEnum


class RoleEnum(StrEnum):
    CONSUMER = "consumer"
    PARTNER = "partner"
    ADMIN = "admin"

class AuthProviderEnum(StrEnum):
    FIREBASE = "firebase"
    GOOGLE = "google"
    CREDENTIALS = "credentials"