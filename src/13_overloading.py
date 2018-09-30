# flake8: noqa

from typing import overload


@overload
def func(i: int) -> int: ...
@overload
def func(f: float, s: str) -> bytes: ...

def func(i, f, s):
    s:bool = True
    return s


func(1, 2)
