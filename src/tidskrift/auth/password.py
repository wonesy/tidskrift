from passlib.context import CryptContext


pw_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_pw: str, hashed_pw: str) -> bool:
    return pw_ctx.verify(plain_pw, hashed_pw)


def hash_password(plain_pw: str) -> str:
    return pw_ctx.hash(plain_pw)
