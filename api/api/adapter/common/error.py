from typing import List

from falcon.http_error import HTTPError


class HTTPErrorResponse(HTTPError):
    """Generic HTTP error response
    """

    def __init__(self, status: str, errors: List[dict]):
        super().__init__(status)
        self.status = status
        self.errors = {'errors': errors}

    def to_dict(self, obj_type=dict):
        super().to_dict(obj_type)
        return self.errors
