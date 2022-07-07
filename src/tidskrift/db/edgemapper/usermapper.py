import edgedb

from tidskrift.model.api import user


def to_user(obj: edgedb.Object) -> user.User:
    return user.User(
        external_id=obj.external_id,
        username=obj.username,
        first_name=obj.first_name,
        last_name=obj.last_name,
        email=obj.email,
        created_at=obj.created_at,
        last_login_at=obj.last_login_at,
    )
