class Nodunder():
    pass


class Dunder():
    def __str__(self) -> str:
        return "dunder"


a: Nodunder = Nodunder()
print(a)  # <__main__.Nodunder object at 0x7f87634fbe50>

b: Dunder = Dunder()
print(b)  # Dunder
