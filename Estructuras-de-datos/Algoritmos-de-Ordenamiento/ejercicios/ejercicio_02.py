def ordenar_burbuja_descendente(lista):
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    i = 0
    hubo_intercambio = True

    while i < n - 1 and hubo_intercambio:
        hubo_intercambio = False
        for j in range(n - 1 - i):
            comparaciones = comparaciones + 1
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios = intercambios + 1
                hubo_intercambio = True
        i = i + 1
        print("Pasada", i, ":", lista)

    return comparaciones, intercambios


temperaturas = [34, 36, 33, 37, 35, 32, 36]
print("Temperaturas en °C:", temperaturas)
comp, inter = ordenar_burbuja_descendente(temperaturas)
print("De mayor a menor:", temperaturas)
print("Comparaciones:", comp, "| Intercambios:", inter)