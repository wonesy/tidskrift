from tidskrift import auth
from tidskrift.db.queries import userquery
from tidskrift.model.api.user import NewUser


async def test_user_queries_create_delete_get(testdb):
    nu = NewUser(
        username="test-un",
        password="test-pw",
        email="test-email",
        first_name="test-fn",
        last_name="test-ln",
    )
    created = await userquery.new(testdb, nu)
    await userquery.delete(testdb, created.username)
    fetched = await userquery.by_username(testdb, created.username)

    assert created.username == nu.username
    assert fetched is None


async def test_user_queries_create_delete_get_with_null_values(testdb):
    nu = NewUser(
        username="test-un",
        password="test-pw",
    )
    created = await userquery.new(testdb, nu)
    await userquery.delete(testdb, created.username)
    fetched = await userquery.by_username(testdb, created.username)

    assert created.username == nu.username
    assert fetched is None


async def test_user_queries_password(testdb):
    plain_pw = "test-pq"
    nu = NewUser(
        username="test-un",
        password=auth.hash_password(plain_pw),
        email="test-email",
        first_name="test-fn",
        last_name="test-ln",
    )
    created = await userquery.new(testdb, nu)
    fetched, pw = await userquery.by_username_with_password(testdb, nu.username)

    assert created == fetched
    assert pw != plain_pw
    assert auth.verify_password(plain_pw, pw)
    await userquery.delete(testdb, created.username)
