from typing import Any, List


def foo(a: int, b: float, c: List[bool] = [], *d: Any, **e: str) -> bool:
    pass


foo.__annotations__
# Out:  {'a': int,
#       'b': float,
#       'c': typing.List[bool],
#       'd': typing.Any,
#       'e': str,
#       'return': bool}
