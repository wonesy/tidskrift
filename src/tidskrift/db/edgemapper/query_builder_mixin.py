from typing import Protocol, Type
from pydantic import BaseModel


_type2edgetype: dict[Type, str] = {str: "str"}


class HasDictProtocol(Protocol):
    def dict(self) -> dict:
        pass


class QueryBuilderMixin:
    def build_insert_query(self: HasDictProtocol, object_name: str | None = None) -> str:
        name = object_name if object_name else self.__class__.__name__

        fields: list[str] = []
        for k, v in self.dict().items():
            if v:
                fields.append(f"\t{k} := <{_type2edgetype[type(v)]}>${k}")

        return "\n".join([f"insert {name} {{", ",\n".join(fields), "}"])
