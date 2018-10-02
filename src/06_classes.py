class Foo:
    def do_something(self, i: int):
        ...


class Bar:
    def run(self, x: Foo):
        x.od_something(1.0)  # Error: "Foo" has no attribute "od_something"; maybe "do_something"?
