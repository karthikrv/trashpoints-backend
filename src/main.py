from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.firebase import get_firebase_app
from src.users.router import router

app = FastAPI()
get_firebase_app()

origins=[
    'http://localhost:3000',
  ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
