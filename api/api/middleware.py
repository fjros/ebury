import falcon

from api.binding.database import SessionManagerBinding


class SessionManagerMiddleware:
    """Falcon middleware that manages a database session per request
    """

    def __init__(self):
        self._manager = SessionManagerBinding.get()

    def process_request(self, request: falcon.Request, response: falcon.Response):
        """Attach a scoped database session to this request
        """

        request.context.session = self._manager.open()

    def process_response(self, request, response, resource, req_succeeded):
        """Close the associated scoped session
        """

        self._manager.close()
