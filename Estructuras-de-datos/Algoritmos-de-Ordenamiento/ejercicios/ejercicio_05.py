# La lista ya ordenada solo necesita una pasada: no hay intercambios y la bandera detiene el algoritmo.
# La lista invertida necesita todas las pasadas y un intercambio en cada comparacion.

def ordenar_burbuja(lista):
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    i = 0
    hubo_intercambio = True

    while i < n - 1 and hubo_intercambio:
        hubo_intercambio = False
        for j in range(n - 1 - i):
            comparaciones = comparaciones + 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios = intercambios + 1
                hubo_intercambio = True
        i = i + 1
        print("Pasada", i, ":", lista)

    return comparaciones, intercambios


ordenada = [10, 20, 30, 40, 50, 60]
print("Lista ya ordenada:", ordenada)
comp, inter = ordenar_burbuja(ordenada)
print("Comparaciones:", comp, "| Intercambios:", inter)

print()

invertida = [60, 50, 40, 30, 20, 10]
print("Lista invertida:", invertida)
comp, inter = ordenar_burbuja(invertida)
print("Comparaciones:", comp, "| Intercambios:", inter)