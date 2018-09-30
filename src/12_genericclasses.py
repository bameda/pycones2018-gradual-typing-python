from typing import Generic, List, TypeVar


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


stacki = Stack[int]()
stacki.push(1)
stacki.push('n')        # Error:  Argument 1 to "push" of "Stack" has incompatible type "str"; expected "int"
