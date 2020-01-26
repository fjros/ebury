import json
from typing import Any


class Deserializer:
    """Default deserializer for controllers to read the appropriate data format
    """

    @classmethod
    def input(cls, data: str) -> Any:
        return JsonDeserializer.data(data)


class JsonDeserializer:
    """Takes JSON string and returns the corresponding data structure
    """

    @classmethod
    def data(cls, data: str) -> Any:
        return json.loads(data)
