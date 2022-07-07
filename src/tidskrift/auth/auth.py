import edgedb
from tidskrift.auth.password import verify_password
from tidskrift.db.queries import userquery
from tidskrift.model.api.user import User


async def authenticate_user(db: edgedb.AsyncIOClient, username: str, password: str) -> User | None:
    user, hashed_pw = await userquery.by_username_with_password(db, username)
    if not user:
        return None
    if not verify_password(plain_ws=password, hashed_pw=hashed_pw):
        return None
    return user
