from typing import Any


class Employee:
    ...


class Manager(Employee):
    ...


def some_func():
    ...


worker = Employee()     # tipo: Employee
worker = Manager()      # OK!: regla 1

boss = Manager()        # tipo: Manager
boss = Employee()       # Error

something: Any = 1      # tipo: Any
worker = something      # OK: regla 2
something = boss        # OK: regla 3
