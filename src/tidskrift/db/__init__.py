import edgedb

__all__ = "get_db"

_client: edgedb.AsyncIOClient | None = None


def get_db() -> edgedb.AsyncIOClient:
    global _client
    if _client is None:
        _client = edgedb.create_async_client()
    return _client
