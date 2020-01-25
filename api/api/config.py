import os


class Configuration:
    """Encapsulate application settings that can be tweaked via env vars
    """

    @property
    def base_uri(self) -> str:
        return os.getenv('BASE_URI', '/api/v1')

    @property
    def fixer_access_key(self) -> str:
        return os.getenv('FIXER_ACCESS_KEY')
