import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH", "firebase-credentials.json")
AUTH_SECRET = os.getenv("AUTH_SECRET")
TRASHPOINT_INTERNAL_API_SECRET=os.getenv("TRASHPOINT_INTERNAL_API_SECRET")