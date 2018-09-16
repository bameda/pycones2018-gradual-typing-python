class Employee:
    pass


class Manager(Employee):
    pass


def some_func():
    pass


worker = Employee()     # tipo: Employee
worker = Manager()      # OK!: regla 1

boss = Manager()        # tipo: Manager
boss = Employee()       # Error

something = some_func() # tipo: Any
worker = something      # OK: regla 2
something = boss        # OK: regla 3
