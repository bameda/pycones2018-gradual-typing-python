from typing import TypeVar


AnyStr = TypeVar('AnyStr', str, bytes)  # can be str or bytes


def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y


concat('aaa', 'bbb')
concat(b'aaa', b'bbb')
concat('aaa', b'bbb')   # Error: Value of type variable "AnyStr" of "concat" cannot be "object"
