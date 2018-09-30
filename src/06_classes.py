class Foo:
    def do_something(self):
        ...


class Bar:
    def run(self, x: Foo):
        x.od_something()  # Error: "Foo" has no attribute "od_something"; maybe "do_something"?
