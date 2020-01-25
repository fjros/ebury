import requests
import requests.exceptions


class HttpJson:
    """Send HTTP requests and return JSON responses as dictionaries
    """

    DEFAULT_TIMEOUT = 5

    @classmethod
    def get(cls, endpoint: str, query_params: dict, timeout: int = DEFAULT_TIMEOUT) -> dict:
        """GET JSON endpoint and return response as dict

        :raises `HttpJsonErrorException`: Error response for request
        :raises `HttpJsonTimeoutException`: Timed out before getting response
        """

        try:
            r = requests.get(endpoint, params=query_params, timeout=timeout)
            r.raise_for_status()

        except requests.exceptions.Timeout:
            raise HttpJsonTimeoutException()

        except requests.exceptions.HTTPError as e:
            if e.response is not None:
                raise HttpJsonErrorException(status=str(e.response.status_code))

            raise HttpJsonErrorException()

        except Exception:
            raise

        return r.json()


class HttpJsonErrorException(Exception):
    """Exception raised when an HTTP error response is received
    """

    STATUS_UNKNOWN = 'unknown'

    def __init__(self, status: str = STATUS_UNKNOWN):
        self.status = status


class HttpJsonTimeoutException(Exception):
    """Exception raised when an HTTP request times out
    """

    pass
