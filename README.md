# Cuestionario sobre python.

## Preguntas Básicas

### 1

> ¿Qué es Python y por qué es un lenguaje de programación popular?

Es un lenguaje de programación de alto nivel con tipos flexibles e interpretado. Es popular por su amplia variedad de librerías y baja curva de aprendizaje.

### 2
> ¿Cómo se declara una variable en Python?

De la forma: a = 1 o a : int = 1

### 3
> ¿Cómo se crea una lista en Python y cómo se accede a sus elementos?

lista = [0, 1, 2] --> para crear
                              
lista[1] = 1 --> para acceder 

### 4
> ¿Cómo se define una función en Python?

def Función ():
                                        
    cuerpo

### 5
> ¿Qué es un bulce for en Python y cómo se utiliza?

Es un bucle que ejecuta su cuerpo por cada elemento de un iterador.

for elemento in elementos:
                            
    print (elemento)

### 6
> ¿Cómo se utiliza la declaración if en Python para controlar el flujo del programa?

Se evalúa una condición y si esta se cumple se ejecuta el cuerpo del if.

### 7 
> ¿Qué es un diccionario en Python y cómo se utiliza?

Es un conjunto de claves y sus valores.
                                   
a = {clave : valor}
                                                                                             
a[clave] = valor

### 8
> ¿Cómo se manejan las excepciones en Python con try y except?

try:
                                                   
    "código con error"
                                                                                                                
catch
                                                                                                                

    manejar error

### 9
> ¿Qué son los módulos en Python y cómo se importan?

Son código externo que se puede llamar.
                                                                                                                

Import Math

### 10
> ¿Cómo se lee y escribe en archivos usando Python?



Para leer:
``` python

with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
``` 

Para escribir:
``` python

with open('nuevo_archivo.txt', 'w') as archivo:
    archivo.write('Este es un nuevo archivo.\n')
    archivo.write('Aquí puedes escribir más contenido.')

``` 


## Preguntas avanzadas

### 1

> ¿Qué es un decorador en Python y cómo se utiliza?

Es una función que permite modificar el comportamiento de otra función o método.
``` python

@mi_decorador
def saludar():
    print("Hola, mundo!")

saludar()
``` 


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

> ¿Qué es un generador en Python y cual es su ventaja sobre una lista normal?


Es una función que permite generar valores sobre la marcha en lugar de crear una lista completa de valores y almacenarlos en la memoria.
Los generadores se definen utilizando funciones que contienen la palabra clave yield. Cuando la función alcanza una declaración yield, el valor se devuelve y el estado de la función se guarda.
Cuando vuelves a llamar a la función generadora, se reanuda desde donde se quedó, lo que permite la generación incremental de valores.

Algunas de sus ventajas sobre las listas son:

Ahorran memoria ya que los valores se generan uno a la vez cuando son necesarios, en lugar de calcular y almacenar todos los valores de antemano como en una lista.
Los generadores no almacenan todos los valores en la memoria al mismo tiempo. En cambio, solo mantienen un registro del estado actual y la lógica para generar el siguiente valor. Esto es beneficioso cuando trabajas con conjuntos de datos muy grandes que no cabrían en la memoria RAM.
Los generadores pueden utilizarse para representar secuencias infinitas de datos, como secuencias numéricas infinitas o flujos de datos en tiempo real. Esto sería imposible con una lista, ya que requeriría una cantidad infinita de memoria.

### 4

> ¿Qué es el GIL (Global Interpreter Lock) en Python y cómo afecta la concurrencia?

El GIL es un mecanismo interno en Python, la implementación de referencia, que se utiliza para sincronizar y controlar el acceso a los objetos y estructuras de datos. Es un bloqueo de mutex (lock) que asegura que solo un hilo de ejecución (thread) pueda ejecutar código a la vez en un proceso. Esto significa que, aunque Python admite la concurrencia en forma de hilos, debido al GIL, la ejecución de código en múltiples hilos no se realiza verdaderamente de manera simultánea.
El GIL tiene un impacto significativo en la concurrencia y puede llevar a una percepción errónea de que Python no es adecuado para aplicaciones multi-hilo o multi-núcleo que requieren una alta concurrencia.

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

> ¿Qué es un contexto en Python y como se utiliza la declaración with?

Un contexto se refiere a un bloque de código en el que se definen acciones específicas que se deben realizar antes y después de que ese bloque se ejecute.
La declaración with se utiliza para crear un contexto en Python. La sintaxis básica de la declaración with es la siguiente:

``` python
with contexto:
     Código que se ejecutará en el contexto
```

### 7

> ¿Cómo se utiliza *args y **kwargs en Python?

El *args permite pasar un número variable de argumentos posicionales a una función. Los argumentos se pasan como una secuencia de valores y se recogen en una tupla en la función.
``` python

def suma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

resultado = suma(1, 2, 3, 4, 5)
print(resultado)  
``` 

El **kwargs permite pasar un número variable de argumentos de palabra clave a una función. Los argumentos se pasan como pares de clave-valor y se recogen en un diccionario en la función.
``` python

def informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

informacion(nombre='Juan', edad=30, ciudad='Ejemplo')
``` 




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

> ¿Qué son las listas por comprensión (list comprehensions) y como se utilizan en Python?

Con las listas por comprensión, puedes generar una nueva lista aplicando una expresión a cada elemento de una secuencia (como una lista, tupla o rango) o iterando sobre una secuencia mientras aplicas una expresión condicional. La sintaxis básica de una lista por comprensión es la siguiente:

``` python
nueva_lista = [expresión for elemento in secuencia]
```

"expresión" es la expresión que se evalúa y se agrega a la nueva lista para cada elemento en la secuencia.
"elemento" es la variable que representa cada elemento de la secuencia.
"secuencia" es la secuencia de la cual deseas generar la nueva lista.
También puedes agregar una cláusula condicional a la lista por comprensión para filtrar los elementos que se incluyen en la nueva lista. La forma general es:

``` python
nueva_lista = [expresión for elemento in secuencia if condición]
```

### 10

> ¿Cómo se puede implementar un patrón de diseño singleton en Python?


El patrón de diseño Singleton se utiliza para garantizar que una clase tenga una única instancia y proporcionar un punto de acceso global a esa instancia.
En Python, se puede implementar un Singleton utilizando un módulo. Debido a que los módulos en Python se importan solo una vez, la instancia de la clase dentro del módulo se comparte en toda la aplicación. 
``` python

class Singleton:
    def __init__(self):
        self.valor = None

// La instancia única de la clase Singleton se crea cuando se importa el módulo
singleton_instance = Singleton()
``` 

También se puede implementar un Singleton como un decorador que garantice que solo se cree una instancia de la clase y que todas las llamadas a la clase devuelvan la misma instancia. 


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

> ¿Qué es __init__.py y cual es su uso en los paquetes de Python?

__init__.py es un archivo especial utilizado para indicar que un directorio debe tratarse como un paquete Python. 
El archivo __init__.py puede estar presente en un directorio (paquete) y puede estar vacío o contener código Python.
Su principal propósito es establecer que el directorio en el que se encuentra es un paquete válido que puede ser importado como un módulo en un programa Python. 

### 13

> ¿Cómo se puede utilizar la reflexión (reflection) en Python para inspeccionar o modificar el código en tiempo de ejecución?

La función dir(): Puedes utilizar la función dir(objeto) para obtener una lista de los atributos y métodos disponibles en un objeto. Esto es útil para inspeccionar un objeto y entender su estructura.
``` python

python
Copy code
class MiClase:
    def __init__(self):
        self.valor = 42
        
objeto = MiClase()
atributos = dir(objeto)
print(atributos)  # Imprime una lista de atributos y métodos de 'objeto'
``` 

La función vars(): La función vars(objeto) devuelve un diccionario con los atributos y valores del objeto. Esto es especialmente útil para inspeccionar y modificar los atributos de un objeto.

``` python

python
Copy code
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
persona = Persona("Juan", 30)
atributos = vars(persona)
print(atributos)  # Imprime {'nombre': 'Juan', 'edad': 30}
``` 

El módulo inspect: El módulo inspect proporciona funciones para obtener información sobre objetos, como funciones, clases y módulos. Puedes utilizarlo para inspeccionar funciones, obtener información sobre sus argumentos y más.

``` python

python
Copy code
import inspect

def mi_funcion(a, b=0):
    return a + b

firma = inspect.signature(mi_funcion)
parametros = firma.parameters
print(parametros)  # Imprime OrderedDict([('a', <Parameter "a">), ('b', <Parameter "b=0">)])
``` 

Clases y objetos dinámicos: Puedes crear clases y objetos en tiempo de ejecución utilizando la función type() para crear clases dinámicamente o utilizando la función setattr() para agregar atributos a objetos.
``` python

python
Copy code
// Creación de una clase dinámicamente
MiClaseDinamica = type('MiClaseDinamica', (object,), {'atributo': 42})

// Agregar atributos a un objeto en tiempo de ejecución
objeto = MiClase()
setattr(objeto, 'nuevo_atributo', 'Hola, mundo!')
``` 

Importación dinámica de módulos: Puedes importar módulos en tiempo de ejecución utilizando la función importlib.import_module.

``` python

python
Copy code
import importlib

modulo = importlib.import_module('mimodulo')
resultado = modulo.mi_funcion()
``` 


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

> ¿Como se puede utilizar la programación funcional en Python?

Utilizando, por ejemplo, funciones lamda o como ciudadanos de primera clase.

Funciones como ciudadanos de primera clase: En Python, las funciones son ciudadanos de primera clase, lo que significa que puedes asignarlas a variables, pasarlas como argumentos a otras funciones y devolverlas como valores. Esto permite el uso de funciones de orden superior, que son funciones que operan sobre otras funciones.

Funciones lambda: Las funciones lambda son funciones anónimas y pequeñas que se pueden utilizar para definir funciones de manera concisa. Son útiles cuando necesitas una función simple para una operación específica.

### 16

> ¿Cómo se puede utilizar los decoradores para registrar (logging) automáticamente las llamadas a funciones en Python?

``` python

import logging

// Configura el sistema de registro
logging.basicConfig(filename='registro.log', level=logging.INFO)

// Definir un decorador personalizado para el registro
def log_func_calls(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Llamada a {func.__name__} con argumentos {args} y {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

// Aplicar el decorador a una función
@log_func_calls
def suma(a, b):
    return a + b

@log_func_calls
def resta(a, b):
    return a - b

// Llamar a las funciones decoradas
resultado_suma = suma(5, 3)
resultado_resta = resta(10, 2)

// Ver el registro
// El registro se guardará en un archivo llamado "registro.log"
// y contendrá información sobre las llamadas a las funciones
``` 


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

> ¿Como se pueden utilizar las corrutinas con la palabra clave yield para manejar la concurrencia de una manera diferente a los hilos y procesos tradicionales?

Las corrutinas permiten la ejecución asincrónica y cooperativa, lo que significa que un programa puede pausar y reanudar la ejecución en puntos específicos sin la necesidad de hilos o procesos múltiples.
Para utilizar yield, hay que definir una función utilizando la palabra yield. El yield se utiliza para pausar la ejecución en ese punto y devolver un valor al llamador. Cuando se llama a la función, esta no se ejecuta por completo, sino que devuelve un objeto generador que puede ser utilizado para controlar la ejecución de la función.

``` python
def mi_corrutina():
    while True:
        valor = yield
        print(f"Recibido: {valor}")
```


### 19

> ¿Cómo se puede utilizar la biblioteca asyncio para programación asincrónica en Python?

``` python

import asyncio

// Define funciones asincrónicas
async def mi_funcion_asincronica():
    await asyncio.sleep(2)
    print("Función asincrónica completada")

async def funcion1():
    await asyncio.sleep(1)
    print("Función 1 completada")

async def funcion2():
    await asyncio.sleep(2)
    print("Función 2 completada")

// Crea un ciclo de eventos
loop = asyncio.get_event_loop()

// Ejecuta funciones asincrónicas
loop.run_until_complete(mi_funcion_asincronica())

// Ejecuta múltiples funciones asincrónicas al mismo tiempo
async def main():
    await asyncio.gather(funcion1(), funcion2())

loop.run_until_complete(main())

// Cierra el ciclo de eventos
loop.close()

``` 
