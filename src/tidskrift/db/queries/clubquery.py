import json
import uuid
import edgedb

from tidskrift.model.api.clubs import Club


async def all(db: edgedb.AsyncIOClient) -> list[Club]:
    resultset = await db.query_json("""select Club""")
    return [Club(**result) for result in json.loads(resultset)]
