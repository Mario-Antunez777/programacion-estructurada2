def busqueda_lineal(lista, objetivo):
    i = 0
    while i < len(lista):
        if lista[i] == objetivo:
            return i
        i = i + 1
    return -1


print("Inventario agotado")
existencias = [12, 7, 0, 25, 0, 3]
posicion = busqueda_lineal(existencias, 0)

if posicion != -1:
    print("El primer producto agotado esta en la posicion", posicion)
else:
    print("No hay productos agotados")