from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tidskrift.db import init_db
from tidskrift.routers import users, clubs, auth

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for r in [users.router, clubs.router, auth.router]:
    app.include_router(r)


@app.on_event("startup")
async def startup():
    init_db()
