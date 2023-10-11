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
