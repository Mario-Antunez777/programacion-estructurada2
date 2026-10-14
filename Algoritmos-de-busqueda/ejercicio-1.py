def busqueda_lineal(lista, objetivo):
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice
    return -1


print("Traza a mano")
lista1 = [4, 15, 8, 15, 23]
print("Buscando 15:", busqueda_lineal(lista1, 15))
print("Buscando 23:", busqueda_lineal(lista1, 23))
print("Buscando 7:", busqueda_lineal(lista1, 7))
print()