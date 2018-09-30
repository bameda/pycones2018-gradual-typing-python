from typing import List, ClassVar

a = 3.4             # implicit (float)
b: float = 3.4      # explicit
l: List[int] = []   # explicit


class MyClass:
    s: str = 'Gazpachito'
    n: int
    b: ClassVar[bool] = True

    def __init__(self):
        self.o: str = 'Espeto'


s = MyClass()
s.s = 1             # Error: Incompatible types in assignment (expression has type "int", variable has type "str")
s.o = 2.0           # Error: Incompatible types in assignment (expression has type "float", variable has type "str")
MyClass.b = True
s.b = True          #  Cannot assign to class variable "some_bool" via instance
