import edgedb
from fastapi import APIRouter, Depends

from tidskrift.db import get_db
from tidskrift.db.queries import clubquery
from tidskrift.model.api.clubs import Club


router = APIRouter(prefix="/clubs", tags=["clubs"])


@router.get("/", response_model=list[Club])
async def get_all_clubs(db: edgedb.AsyncIOClient = Depends(get_db)):
    return await clubquery.all(db)
