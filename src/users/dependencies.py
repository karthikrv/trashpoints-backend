from fastapi import Depends, Header, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth
from google.auth.transport import requests
from google.oauth2 import id_token
from sqlalchemy.orm import Session

from src.config import GOOGLE_CLIENT_ID, TRASHPOINT_INTERNAL_API_SECRET
from src.database import get_db
from src.users import service as user_service
from src.users.schemas import AuthRequest, ConsumerCreate

security = HTTPBearer()

def verify_google_token(auth_request: AuthRequest) -> dict:
    try:
        user_info = id_token.verify_oauth2_token(
                            auth_request.token, 
                            requests.Request(), 
                            GOOGLE_CLIENT_ID
                          )
        user_info["isAuthorised"] = True
        print("Decoded Google token:", user_info)
        return user_info
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid Token"
        )

def resolve_user_org_details(auth_request: AuthRequest, db: Session = Depends(get_db)) -> dict:
    user_info = verify_google_token(auth_request)
    return user_service.get_current_user_details(db=db, user_info=user_info)

def verify_firebase_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    token = credentials.credentials
    try:
        decoded_token = auth.verify_id_token(token)
        print("FIREBASE UID:", decoded_token.get("uid"))
        return decoded_token
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

def resolve_consumer_details( db: Session = Depends(get_db), user_info : dict = Depends(verify_firebase_token)) -> dict:
    return user_service.get_current_consumer_details(db=db, user_info=user_info)

def create_consumer_details( userDetails: ConsumerCreate, db: Session = Depends(get_db), user_info : dict = Depends(verify_firebase_token)) -> dict:
    return user_service.create_new_consumer(requestBody=userDetails ,db=db, user_info=user_info)

def verify_internal_secret(x_internal_secret: str = Header(...)) -> None:
    print("Received secret:", repr(x_internal_secret))
    print("Expected secret:", repr(TRASHPOINT_INTERNAL_API_SECRET))
    if x_internal_secret != TRASHPOINT_INTERNAL_API_SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")