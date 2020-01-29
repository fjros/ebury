import json
from abc import ABC
from abc import abstractmethod
from typing import Any


class Transformer(ABC):
    """Base class for data serialization/deserialization
    """

    @classmethod
    @abstractmethod
    def serialize(cls, data: Any) -> str:
        pass

    @classmethod
    @abstractmethod
    def deserialize(cls, data: str) -> Any:
        pass


class JsonTransformer(Transformer):
    """Generic JSON serializer/deserializer
    """

    @classmethod
    def serialize(cls, data: Any) -> str:
        return json.dumps(data)

    @classmethod
    def deserialize(cls, data: str) -> Any:
        return json.loads(data)
