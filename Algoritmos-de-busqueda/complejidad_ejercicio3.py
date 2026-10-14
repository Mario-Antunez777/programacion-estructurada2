import time


def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones = comparaciones + 1
        if lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones


print("Tabla de crecimiento")
tamanos = [1000, 10000, 100000, 1000000, 2000000]

for n in tamanos:
    codigos = list(range(1, n + 1))
    inicio = time.perf_counter()
    pos, comp = busqueda_lineal(codigos, 0)
    fin = time.perf_counter()
    tiempo = fin - inicio
    print("n =", n, "| comparaciones =", comp, "| tiempo =", round(tiempo, 5), "s")
    if n == 1000000:
        prediccion = tiempo * 2
        print("Prediccion para 2000000:", round(prediccion, 5), "s")