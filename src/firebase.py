from pathlib import Path

import firebase_admin
from firebase_admin import auth, credentials

from src.config import FIREBASE_CREDENTIALS_PATH

_firebase_app = None
 
def get_firebase_app():
    global _firebase_app
 
    if _firebase_app is not None:
        return _firebase_app
 
    cred_path = Path(FIREBASE_CREDENTIALS_PATH)
 
    if not cred_path.exists():
        raise FileNotFoundError(
            f"Firebase credentials file not found: {cred_path}"
        )
 
    cred = credentials.Certificate(str(cred_path))
    _firebase_app = firebase_admin.initialize_app(cred)
 
    return _firebase_app