import uuid
from pydantic import BaseModel

from tidskrift.model.api.user import User


class Club(BaseModel):
    external_id: uuid.UUID
    name: str
    # creator: User
    # members: list[User]
