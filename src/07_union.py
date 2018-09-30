from typing import Union


def mul(n: int, m: Union[str, int]):
    return n * m


mul(5, 1)     # -> 5
mul(5, '*')   # -> *****
mul(5, 2.0)   # Error:  Argument 2 to "mul" has incompatible type "float"; expected "Union[str, int]"


from typing import Any, Optional, Union


assert Union[str] == str
assert Union[str, Any] == Any
assert Union[str, str, int] == Union[str, int]
assert Union[int, str] == Union[str, int]
assert Union[Union[int, str], float] == Union[int, str, float]
assert Union[str, int, None] == Optional[Union[str, int]]
