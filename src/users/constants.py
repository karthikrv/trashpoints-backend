from enum import StrEnum


class RoleEnum(StrEnum):
    CONSUMER = "citizen"
    PARTNER = "collector"
    ADMIN = "admin"

class AuthProviderEnum(StrEnum):
    FIREBASE = "firebase"
    GOOGLE = "google"
    CREDENTIALS = "credentials"