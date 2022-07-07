import edgedb
from fastapi import APIRouter, Depends, HTTPException, status
from tidskrift import auth
from tidskrift.db import get_db

from tidskrift.model.api.user import NewUser, User
from tidskrift.db.queries import userquery


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[User])
async def get_all_users(db: edgedb.AsyncIOClient = Depends(get_db)):
    return await userquery.all(db)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_new_user(new_user: NewUser, db: edgedb.AsyncIOClient = Depends(get_db)):
    new_user.password = auth.hash_password(new_user.password)
    try:
        return await userquery.new(db, new_user)
    except edgedb.errors.ConstraintViolationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": f"username {new_user.username} already exists"},
        )


@router.get("/{username}", response_model=User)
async def get_user_by_username(username: str, db: edgedb.AsyncIOClient = Depends(get_db)):
    user = await userquery.by_username(db, username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"unable to find user with username '{username}'",
        )

    return user


@router.put("/{username}", response_model=User)
async def upsert_user(username: str, db: edgedb.AsyncIOClient = Depends(get_db)):
    pass


@router.delete("/{username}")
async def delete_user(username: str, db: edgedb.AsyncIOClient = Depends(get_db)):
    await userquery.delete(db, username)
