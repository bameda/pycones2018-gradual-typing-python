class Foo:
    def do_something(self, n: int):
        ...


class Bar:
    def run(self, x: Foo):
        x.do_something(0)  # Error: "Foo" has no attribute "od_something"; maybe "do_something"?
