from fastapi import FastAPI
from tidskrift.db import init_db
from tidskrift.routers import users

app = FastAPI()

for r in [users.router]:
    app.include_router(r)


@app.on_event("startup")
async def setup():
    init_db()
