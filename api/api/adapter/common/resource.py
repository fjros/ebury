class ToDictMixin:
    """Return dict based on 'public' attributes of the underlying object
    """

    def dict(self) -> dict:
        return {
            attr: value
            for attr, value in self.__dict__.items()
            if not attr.startswith('_') and value is not None
        }
