from datetime import timedelta
import edgedb
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from tidskrift.auth.auth import authenticate_user

from tidskrift.auth.tokens import ACCESS_TOKEN_EXPIRE_MINUTES, Tokens, create_tokens
from tidskrift.db import get_db


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Tokens)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: edgedb.AsyncIOClient = Depends(get_db)
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return create_tokens(data={"sub": user.username}, expires_delta=access_token_expires)
