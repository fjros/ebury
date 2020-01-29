import json
from typing import Any


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
