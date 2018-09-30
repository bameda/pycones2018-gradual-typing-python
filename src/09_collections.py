from typing import List, Dict, Set, Tuple


List[str]             # list of str objects
Dict[str, int]        # dictionary from str to int
Set[str]              # set of str objects
Tuple[int, int, int]  # a 3-tuple of ints
Tuple[int, ...]       # a variable length tuple of ints

###########################

from typing import List, Set, Union


list_a: List[float]
list_a = [1, 1.0, 2.0]
list_a = ['a', 1.0, 2.0]  # Error: List item 0 has incompatible type "str"; expected "float"

list_b: List[Union[float, str]] = [1, 1.0, 'a']

set_a: Set[int] = {1, 2, 3}
set_a = {1, 2, 'a'}       # Error: Argument 3 to &#60;set&#62; has incompatible type "str"; expected "int"

###########################

from typing import NamedTuple


class Employee(NamedTuple):
    """Represents an employee."""
    name: str
    id: int = 3

    def __repr__(self) -> str:
        return f'<Employee {self.name}, id={self.id}>'

###########################

from typing import Mapping, MutableMapping, Sequence, MutableSequence


Mapping[str, str]           # a mapping from strings to strings
MutableMapping[str, str]    # a mutable mapping from strings to strings
Sequence[int]               # a sequence of integers
MutableSequence[int]        # a mutable sequence of integers
