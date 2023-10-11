# Clase
class ParentClass():
    # Atributo protegido (protected de c#) implementando encapsulación
    _attribute: str

    multiplier: int

    def __init__(self, multiplier: int):
        self._attribute = "parent"
        self.multiplier = multiplier

    def two_attribute(self) -> str:
        return self._attribute * self.multiplier

# Clase heredera
class ChildClass(ParentClass):
    def __init__(self, multiplier: int):
        self._attribute = "child"
        self.multiplier = multiplier

a: ParentClass = ParentClass(3)

print(a.two_attribute()) # parentparentparent

a = ChildClass(3)

print(a.two_attribute()) # childchildchild

# No tira error, python espera que no se llame al atributo por su sufijo,
# pero no lo checkea.
b = a._attribute 
