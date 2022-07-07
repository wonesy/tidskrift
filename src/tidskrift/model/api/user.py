import datetime
import uuid
from pydantic import BaseModel

from tidskrift.db.edgemapper.query_builder_mixin import QueryBuilderMixin


class User(BaseModel):
    external_id: uuid.UUID
    username: str
    first_name: str | None
    last_name: str | None
    email: str | None
    created_at: datetime.datetime
    last_login_at: datetime.datetime | None


class NewUser(BaseModel, QueryBuilderMixin):
    username: str
    password: str
    first_name: str | None
    last_name: str | None
    email: str | None
