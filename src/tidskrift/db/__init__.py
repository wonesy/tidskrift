from dataclasses import dataclass
import edgedb

__all__ = ("get_db", "EdgedbCredentials")

_client: edgedb.AsyncIOClient | None = None


@dataclass
class EdgedbCredentials:
    password: str
    user: str
    database: str
    tls_cert_data: str | None = None
    tls_ca: str | None = None
    tls_security: str | None = None
    host: str = "localhost"
    port: int = 5656

    def __str__(self) -> str:
        return f"""EdgedbCredentials(
            user={self.user},
            password=****,
            database={self.database},
            host={self.host},
            port={self.port}
        """

    @property
    def dsn(self) -> str:
        return f"edgedb://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


def init_db(credentials: EdgedbCredentials | None = None):
    global _client
    dsn = credentials.dsn if credentials else None
    tls_ca = credentials.tls_ca if credentials else None
    tls_security = credentials.tls_security if credentials else None
    _client = edgedb.create_async_client(dsn=dsn, tls_ca=tls_ca, tls_security=tls_security)


def get_db() -> edgedb.AsyncIOClient:
    global _client
    assert _client, "Database connection is uninitialized"
    return _client
