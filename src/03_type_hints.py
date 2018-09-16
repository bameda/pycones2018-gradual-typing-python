#######################
from typing import Union

def func(a: int, b: Union[bool, int]) -> bool:
    print('Soy la 1')
    return True

func(1, True)
func(2, 3)
func(4, 5.0)

#######################

a: complex
a = 2j
a = 1.0
a = 1

b: float
b = 2j
b = 1.0
b = 1

c: int
c = 2j
c = 1.0
c = 1

#######################

from typing import List

l: List[int] = []
l = [1, 2, 3]
l = [1, 2, 3.4]
l = None
l = ['str', 2]

s: bytearray

#######################

from typing import List, Set

list_a: List[float]
list_a = ['a', 1.0, 2.0]    # Error: List item 0 has incompatible type "str"; expected "float"
list_a = [1, 1.0, 2.0]

list_b: List[Union[float, str]]
list_b = [1, 1.0, 'a']

set_a: Set[int] = {1, 2, 3}
set_a = {1, 2, 'a'} # Error: Argument 3 to <set> has incompatible type "str"; expected "int"

#######################

from typing import NamedTuple

class Employee(NamedTuple):
    """Represents an employee."""
    name: str
    id: int = 3

    def __repr__(self) -> str:
        return f'<Employee {self.name}, id={self.id}>'

e = Employee('Guido')
assert e.id == 3

#######################

class Foo:
    def bar(self):
        pass

f = Foo()
f.baz()     # Error: "Foo" has no attribute "baz"

#######################

from __future__ import annotations
from typing import Union

class Tree:
    def __init__(self, left: Union[Tree, None], right: Union[Tree, None]) -> None:
        #       (self, left: `Tree`, right: `Tree`) -> None:
        self.left = left
        self.right = right

t = Tree(Tree(None, None), Tree(None, None))

#######################

from typing import Union

def mul(n : int, m : Union[str, int]):
    return n * m

mul(5, 1)   # -> 5
mul(5, '*') # -> *****
mul(5, 2.0) # Error:  Argument 2 to "mul" has incompatible type "float"; expected "Union[str, int]"

aux: Union[str, None] = 'a'
aux = None
aux = 'bbbb'
aux = 1 # Error  Incompatible types in assignment (expression has type "int", variable has type "Optional[str]")

#######################
from typing import Any, Optional, Union

assert Union[str] == str
assert Union[Union[int, str], float] == Union[int, str, float]
assert Union[str, str, int] == Union[str, int]
assert Union[int, str] == Union[str, int]
assert Union[str, int, None] == Optional[Union[str, int]]

d: Union[str, Any] = 'combo'
d = 1
d = None
d = 1.2

#######################

from typing import Optional

z: Optional[str] = None
z = 'text'

y: Union[str, None] = z
w: Union[int, None] = z
#######################
from typing import Tuple, List

AnyStr = TypeVar('AnyStr', str, bytes)

def concat(x: AnyStr, y: AnyStr) -> AnyStr:
  return x + y

concat('aaa', 'bbb')
concat(b'aaa', b'bbb')
concat('aaa', b'bbb') # Error: Value of type variable "AnyStr" of "concat" cannot be "object"

#######################
from typing import TypeVar, Generic

Z = TypeVar('Z')

class Stack(Generic[Z]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[Z] = []

    def push(self, item: Z) -> None:
        self.items.append(item)

    def pop(self) -> Z:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

stacki = Stack[int]()
stacki.push(1)
stacki.push('n')
#######################
