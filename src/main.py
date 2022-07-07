from fastapi import FastAPI
from tidskrift.routers import users

app = FastAPI()

for r in [users.router]:
    app.include_router(r)
