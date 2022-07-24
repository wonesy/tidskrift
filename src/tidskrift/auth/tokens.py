from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "0c49397f5a7db56ca3c83510e4df7ad272711685b8e6e600cae4b1856bd22055"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120


class Tokens(BaseModel):
    access_token: str
    refresh_token: str


class TokenData(BaseModel):
    username: str | None = None


def create_tokens(data: dict, expires_delta: timedelta | None = None) -> Tokens:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return Tokens(access_token=encoded_jwt, refresh_token="")
