import json
from typing import Any


class DictTransformerMixin:
    """Return dict based on 'public' attributes of the underlying object
    """

    def dict(self) -> dict:
        return {
            attr: value
            for attr, value in self.__dict__.items()
            if not attr.startswith('_') and value is not None
        }


class Serializer:
    """Default serializer for controllers to output the appropriate data format
    """

    @classmethod
    def output(cls, data: Any) -> str:
        return JsonSerializer.json(data)


class JsonSerializer:
    """Takes JSON-serializable data and outputs JSON string
    """

    @classmethod
    def json(cls, data: Any) -> str:
        return json.dumps(data)
