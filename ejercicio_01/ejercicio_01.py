"""
Ejercicio 1. Potencia recursiva

Implementa una función que calcule una potencia mediante multiplicaciones y
llamadas recursivas. Recibe una base numérica y un exponente entero no
negativo.

    def potencia(base, exponente):
        pass

En este ejercicio, cualquier base elevada a cero devuelve 1, incluido
potencia(0, 0).

Ejemplos

    potencia(2, 4)    # 16
    potencia(5, 0)    # 1
    potencia(-2, 3)   # -8
    potencia(0, 5)    # 0

Restricciones

- No utilices ciclos.
- No utilices  ni pow().
- La solución debe ser recursiva.
"""


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuál es el caso base?
#cualquiera que tenga exponente 0 (cualquier numero elevado a 0 es 1)
#
# 2. ¿Qué argumento cambia en cada llamada?
#  el exponente, disminuye en 1 en cada llamada recursiva (exponente - 1)
#
# 3. ¿Qué operación queda pendiente mientras se resuelve la llamada recursiva?
#   la multiplicacion de la base por el resultado de la llamada recursiva (base * potencia(base, exponente - 1))
#
# 4. Escribe las llamadas y los retornos de potencia(3, 3).
# llamadas: 
# potencia(3, 3)--> 3 * potencia(3, 2), 
# potencia(3, 2)--> 3 * potencia(3, 1), 
# potencia(3, 1)--> 3 * potencia(3, 0), 
# potencia(3, 0)--> 1 (caso base)
#
# retornos: 
# potencia(3, 0)--> 1
#potencia(3, 1)--> 3 * 1 = 3
#potencia(3, 2)--> 3 * 3 = 9
#potencia(3, 3)--> 3 * 9 = 27

if __name__ == "__main__":
    print(potencia(2, 4))    # 16
    print(potencia(5, 0))    # 1
    print(potencia(-2, 3))   # -8
    print(potencia(0, 5))    # 0


