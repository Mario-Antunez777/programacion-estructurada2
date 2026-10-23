# Practica comparativa de algoritmos de busqueda
# Version A: busqueda binaria
# Version B: busqueda por interpolacion
# Version C: busqueda con diccionario
#
# La lista NO esta repartida de forma uniforme:
# tiene numeros pares y el ultimo valor es gigante (10**12).
# Es el peor caso para la interpolacion.

import time

TAMANIOS = [1000, 100000, 1000000]
REPETICIONES = 10


# Version A: busqueda binaria
def busqueda_binaria(lista, valor):
    bajo = 0
    alto = len(lista) - 1
    comparaciones = 0

    while bajo <= alto:
        medio = (bajo + alto) // 2
        comparaciones = comparaciones + 1
        if lista[medio] == valor:
            return medio, comparaciones
        elif lista[medio] < valor:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1, comparaciones


# Version B: busqueda por interpolacion
def busqueda_interpolacion(lista, valor):
    bajo = 0
    alto = len(lista) - 1
    comparaciones = 0

    while bajo <= alto and lista[bajo] <= valor and valor <= lista[alto]:
        # evita dividir entre cero
        if lista[alto] == lista[bajo]:
            comparaciones = comparaciones + 1
            if lista[bajo] == valor:
                return bajo, comparaciones
            return -1, comparaciones

        pos = bajo + (valor - lista[bajo]) * (alto - bajo) // (lista[alto] - lista[bajo])

        comparaciones = comparaciones + 1
        if lista[pos] == valor:
            return pos, comparaciones
        elif lista[pos] < valor:
            bajo = pos + 1
        else:
            alto = pos - 1

    return -1, comparaciones


# Version C: busqueda con diccionario
def construir_indice(lista):
    indice = {}
    for posicion in range(len(lista)):
        indice[lista[posicion]] = posicion
    return indice


def busqueda_dict(indice, valor):
    if valor in indice:
        return indice[valor], 1
    return -1, 1


# Medicion
def medir(funcion, estructura, valor):
    inicio = time.perf_counter()
    for i in range(REPETICIONES):
        posicion, comparaciones = funcion(estructura, valor)
    fin = time.perf_counter()
    promedio = (fin - inicio) / REPETICIONES * 1000000
    return posicion, comparaciones, promedio


def crear_lista(n):
    # n-1 numeros pares y al final un valor muy grande
    lista = []
    for i in range(n - 1):
        lista.append(2 * i)
    lista.append(10 ** 12)
    return lista


def ejecutar_prueba(n):
    lista = crear_lista(n)

    inicio = time.perf_counter()
    indice = construir_indice(lista)
    costo_indice = (time.perf_counter() - inicio) * 1000

    print("")
    print("=== n =", n, "elementos ===")
    print("Costo de construir el dict (una vez):", round(costo_indice, 2), "ms")

    casos = [
        ("Inicio", lista[0]),
        ("Centro", lista[n // 2]),
        ("Final", lista[n - 1]),
        ("Inexistente", lista[n // 2] + 1)
    ]

    for caso in casos:
        nombre = caso[0]
        valor = caso[1]
        print("")
        print("Caso:", nombre, "| Valor:", valor)

        pos, comp, tiempo = medir(busqueda_binaria, lista, valor)
        print("  A Binaria    pos:", pos, "comp:", comp, "tiempo (us):", round(tiempo, 3))

        pos, comp, tiempo = medir(busqueda_interpolacion, lista, valor)
        print("  B Interpol.  pos:", pos, "comp:", comp, "tiempo (us):", round(tiempo, 3))

        pos, comp, tiempo = medir(busqueda_dict, indice, valor)
        print("  C dict       pos:", pos, "comp:", comp, "tiempo (us):", round(tiempo, 3))


def main():
    print("Comparativa: binaria vs interpolacion vs dict")
    print("Cada tiempo es el promedio de", REPETICIONES, "repeticiones.")
    for n in TAMANIOS:
        ejecutar_prueba(n)


main()