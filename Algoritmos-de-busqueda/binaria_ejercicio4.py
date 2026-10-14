def busqueda_binaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    posicion = -1
    # Correccion 1: antes decia izq < der, ahora izq <= der
    while izq <= der and posicion == -1:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            posicion = medio
        elif lista[medio] < objetivo:
            # Correccion 2: antes decia izq = medio, ahora izq = medio + 1
            izq = medio + 1
        else:
            der = medio - 1
    return posicion


expedientes = [1203, 1250, 1318, 1342, 1409, 1477, 1501, 1566, 1620, 1688, 1735]
print(busqueda_binaria(expedientes, 1620))
print(busqueda_binaria(expedientes, 1300))