# Cuestionario sobre python.

## Preguntas Básicas

## Preguntas avanzadas

### 1

### 2

> ¿Cómo se implementa la herencia múltiple en python?

``` python
class Class1:
    def m(self):
        print("In Class1") 
       
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
        print("In Class3")  

# Dentro de los paréntesis se ponen las clases base.
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)
        Class1.m(self)
```

[Click para ir a la
fuente](https://www.geeksforgeeks.org/multiple-inheritance-in-python/)

### 3

### 4

### 5

> ¿Cómo se puede implementar la programación orientada a objetos en
> python?

Se implementa mediante el uso de clases, que pueden tener atributos,
herencia, implementar polimorfismo y encapsular lógica y atributos.

``` python
# Clase
class ParentClass():
    # Atributo protegido (protected de c#) implementando encapsulación
    _attribute: str

    multiplier: int

    # Constructor
    def __init__(self, multiplier: int):
        self._attribute = "parent"
        self.multiplier = multiplier

    def two_attribute(self) -> str:
        return self._attribute * self.multiplier

# Clase heredera
class ChildClass(ParentClass):
    def __init__(self, multiplier: int):
        # Solamente cambia el atributo protegido
        self._attribute = "child"
        self.multiplier = multiplier

a: ParentClass = ParentClass(3)

print(a.two_attribute()) # parentparentparent

# Polimorfismo
a = ChildClass(3)

print(a.two_attribute()) # childchildchild

# No tira error, python espera que no se llame al atributo por su sufijo,
# pero no lo checkea.
b = a._attribute 
```

### 6

### 7

### 8

> ¿Cómo se puede hacer profiling de un código de python para analizar su
> rendimiento?

Se puede utilizar cProfile desde la terminal:

``` fish
python -m cProfile OOP.py
```

output:

    [I] cris:cris@cr ~/m/m/cuestionario_python master …2 ./rw
    $ python -m cProfile OOP.py
    parentparentparent
    childchildchild
             13 function calls in 0.000 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 OOP.py:1(<module>)
            2    0.000    0.000    0.000    0.000 OOP.py:12(two_attribute)
            1    0.000    0.000    0.000    0.000 OOP.py:16(ChildClass)
            1    0.000    0.000    0.000    0.000 OOP.py:17(__init__)
            1    0.000    0.000    0.000    0.000 OOP.py:2(ParentClass)
            1    0.000    0.000    0.000    0.000 OOP.py:8(__init__)
            2    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
            2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

### 9

### 10

### 11

> ¿Cómo funciona el recolector de basura en python?

El recolector de basura de python es muy similar al de Javascript y C\#
(y me imagino que al de mayoría de lenguajes de alto nivel, pero sólo
conozco la implementación a bajo nivel de esos dos)

El recolector de basura mantiene un contador de referencias a los
diferentes objetos que se crean a lo largo del programa. Cuando se
asigna un objeto a una variable, su contador aumenta, y cuando se
desasigna, decrementa. Al llegar a cero, el objeto es liberado.

Existen casos en que este método es insuficiente, como las referencias
cíclicas. Como verificarlas es más intensivo en procesamiento que la
liberación por contador, se dividen los objetos a verificar en tres
generaciones. Los objetos de la generación 0 se verifican e intentan
limpiar frecuentemente, y cuando sobreviven recolecciones, se mueven a
las siguientes generaciones. Mientras más avanzada la generación, más
infrecuente la revisión de referencias, ya que se espera que el objeto
tenga una vida más larga.

Por último, se pueden forzar recolecciones mediante el módulo gc.

### 12

### 13

### 14

> ¿Qué son los métodos mágicos de python y cómo se utilizan?

Dunder significa "double under score" (`_`), y lógicamente estos son los
métodos que empiezan y terminan con `__`. Estos métodos pueden definir
funcionalidad particular de un objeto, y la funcionalidad específica que
sobreescriben depende del nombre del método. Se les dice mágicos ya que
pueden modificar el funcionamiento de un objeto de formas inesperadas.

Ejemplo:

``` python
class Nodunder():
    pass


class Dunder():
    def __str__(self) -> str:
        return "dunder"


a: Nodunder = Nodunder()
print(a)  # <__main__.Nodunder object at 0x7f87634fbe50>

b: Dunder = Dunder()
print(b)  # Dunder
```

### 15

### 16

### 17

> ¿Cómo se pueden utilizar los hilos (threads) y los procesos
> (processes) para ejecutar tareas en paralelo?

Threading:

``` python
import threading
import time

# Tarea que lleva bastante tiempo
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    time.sleep(0.001)
    return n * factorial(n - 1)

# Imprime segundo
t = threading.Thread(target=lambda: print(factorial(100)));

# Se inicia la tarea
t.start()

# Imprime primero (amenos que tu pc sea un vegetal)
print("hi mom")

# Se une el hilo actual a la tarea
t.join()
```

Processes:

``` python
from collections.abc import Iterable
import multiprocessing
import time
import pprint
from typing import List

# Misma implementación que antes (ahora con verdadero paralelismo)

# Tarea que lleva bastante tiempo


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    time.sleep(0.001)
    return n * factorial(n - 1)


# Imprime segundo
t = multiprocessing.Process(target=lambda: print(factorial(100)))

# Se inicia la tarea
t.start()

# Imprime primero (a menos que tu pc sea un vegetal)
print("hi mom")

# Se une el hilo actual a la tarea
t.join()

# Implementación que aprovecha el paralelismo
with multiprocessing.Pool() as pool:
    inputs: Iterable[int] = range(50)
    results: List[int] = pool.map(factorial, inputs)
    pprint.pp(results)
```

### 18

### 19
