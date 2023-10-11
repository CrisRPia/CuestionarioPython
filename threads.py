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
