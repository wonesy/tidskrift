import json
import os
import edgedb
import pytest
import pytest_asyncio

from tidskrift.db import EdgedbCredentials, get_db, init_db


@pytest_asyncio.fixture
async def testdb(event_loop) -> edgedb.AsyncIOClient:
    credentials_file = os.getenv("EDGEDB_CREDENTIALS_FILE")

    try:
        with open(credentials_file, "r") as f:
            credentials: dict = json.load(f)

        edgedbcreds = EdgedbCredentials(
            user=credentials["user"],
            password=credentials["password"],
            port=credentials["port"],
            database=credentials["database"],
            tls_cert_data=credentials.get("tls_cert_data"),
            tls_ca=credentials.get("tls_ca"),
            tls_security=credentials.get("tls_security"),
        )
    except TypeError:
        edgedbcreds = None

    init_db(edgedbcreds)
    return get_db()
