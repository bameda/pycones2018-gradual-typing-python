from typing import List, ClassVar

a = 3.4             # implicit (float)
b: float = 3.4      # explicit
l: List[int] = []   # explicit


class MyClass:
    an_string: str = 'Gazpachito'
    a_number: int
    a_bool: ClassVar[bool] = True

    def __init__(self):
        self.other_string: str = 'Espeto'


s = MyClass()
s.an_string = 1   # Error: Incompatible types in assignment (expression has type "int", variable has type "str")
MyClass.a_bool = True
s.a_bool = True  #  Cannot assign to class variable "some_bool" via instance
