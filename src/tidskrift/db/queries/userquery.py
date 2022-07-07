from typing import Tuple
import edgedb
from tidskrift.db.edgemapper import usermapper
from tidskrift.model.api.user import NewUser, User
from tidskrift.util import filtertools


async def all(db: edgedb.AsyncIOClient) -> list[User]:
    resultset = await db.query(
        """
        select User {
            external_id,
            username,
            first_name,
            last_name,
            email,
            created_at,
            last_login_at
        }
    """
    )

    return list(map(lambda o: usermapper.to_user(o), resultset))


async def by_username(db: edgedb.AsyncIOClient, username: str) -> User | None:
    resultset = await db.query(
        """
        select User {
            external_id,
            username,
            first_name,
            last_name,
            email,
            created_at,
            last_login_at
        }
        filter .username = <str>$username

    """,
        username=username,
    )

    if not resultset:
        return None

    return usermapper.to_user(resultset[0])


async def by_username_with_password(
    db: edgedb.AsyncIOClient, username: str
) -> Tuple[User | None, str]:
    resultset = await db.query(
        """
        select User {
            external_id,
            username,
            password,
            first_name,
            last_name,
            email,
            created_at,
            last_login_at
        }
        filter .username = <str>$username

    """,
        username=username,
    )

    if not resultset:
        return None, ""

    return usermapper.to_user(resultset[0]), resultset[0].password


async def new(db: edgedb.AsyncIOClient, new_user: NewUser) -> User:
    resultset = await db.query(
        """
        with NewUser := (
            """
        + new_user.build_insert_query("User")
        + """
        )
        select NewUser {
            external_id,
            username,
            password,
            first_name,
            last_name,
            email,
            created_at,
            last_login_at
        }
    """,
        **filtertools.nonones(new_user.dict()),
    )

    return usermapper.to_user(resultset[0])


async def delete(db: edgedb.AsyncIOClient, username: str) -> None:
    await db.query(
        """
        delete User
        filter .username = <str>$username
    """,
        username=username,
    )


async def delete_all(db: edgedb.AsyncIOClient, test_mode: bool = False):
    if test_mode is False:
        return
    await db.query("delete User")


async def upsert(db: edgedb.AsyncIOClient):
    pass
