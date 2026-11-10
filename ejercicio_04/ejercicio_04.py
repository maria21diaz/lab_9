"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if codigos[medio] == objetivo:
        return medio
    elif codigos[medio] < objetivo:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)
    else:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
#   La búsqueda termina cuando se encuentra el objetivo en el indice medio (codigos[medio]==objetivo) o cuando el rango de búsqueda se 
#   reduce a un punto donde izquierda > derecha, lo que indica que el objetivo no está presente en la lista.
#
# 2. ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
# porque  el elemento en la posicion medio ya fue comparada con el objetivo y se confirmo que no es el objetivo, por lo que no tiene sentido incluirlo nuevamente en la búsqueda.
#
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
#    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |    0      |    6    |   3   | ir a la izquierda (codigos[3] = 415 > 300)
#       2    |    0      |    2    |   1   | ir a la derechea (codigos[1] = 205 < 300)
#       3    |    2      |    2    |   2   | ir a la izquierda (codigos[2] = 310 > 300)
#       4    |    2      |    1    |   —   | retornar -1 (izquierda > derecha)
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de
#    contar_desde_limite()?  
#    La función contar_desde_limite() reduce el problema de elemento en elemento (complejidad lineal (O(n))), mientras que la función 
# buscar_codigo() reduce el problema a la mitad en cada llamada (complejidad logarítmica (O(log n))). 
# Esto significa que buscar_codigo() es mucho más eficiente para listas grandes, ya que descarta grandes porciones de la lista en cada paso.


if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0
