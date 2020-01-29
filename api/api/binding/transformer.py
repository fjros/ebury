from api.adapter.common.transformer import JsonTransformer
from api.adapter.common.transformer import Transformer


class TransformerBinding:
    """Return concrete implementation of the `Transformer` abstract class
    """

    @classmethod
    def get(cls) -> Transformer:
        return JsonTransformer()
