# Proyecto 3 · ¿Por qué falla la binaria?
# Nombre: Mario Andres Antunez Rivera
# Carné: 6B9A59C2

facturas = [4821, 1307, 9654, 2290, 7716, 3348, 5012, 8875, 1180, 6433, 2957, 7041, 3895, 9210, 5568]
buscados = [8875, 4821, 2290, 7041, 9210, 1180]


def busqueda_lineal(lista, buscado):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones = comparaciones + 1
        if lista[i] == buscado:
            return i, comparaciones
    return -1, comparaciones


def busqueda_binaria(lista, buscado):
    izq = 0
    der = len(lista) - 1
    comparaciones = 0
    while izq <= der:
        medio = (izq + der) // 2
        comparaciones = comparaciones + 1
        if lista[medio] == buscado:
            return medio, comparaciones
        elif lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, comparaciones


def binaria_con_traza(lista, buscado):
    izq = 0
    der = len(lista) - 1
    comparaciones = 0
    while izq <= der:
        medio = (izq + der) // 2
        comparaciones = comparaciones + 1
        print("izq =", izq, " der =", der, " medio =", medio, " lista[medio] =", lista[medio])
        if lista[medio] == buscado:
            return medio, comparaciones
        elif lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, comparaciones


def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def busqueda_segura(lista, buscado):
    if esta_ordenada(lista):
        return busqueda_binaria(lista, buscado)
    else:
        return busqueda_lineal(lista, buscado)


# Paso 3: la binaria sobre la lista desordenada
print("=== BINARIA SOBRE LISTA DESORDENADA ===")
print("Buscado\tReal\tBinaria\tComparaciones\tVeredicto")
print("-------\t----\t-------\t-------------\t---------")
for valor in buscados:
    real, comp_lineal = busqueda_lineal(facturas, valor)
    pos_bin, comp_bin = busqueda_binaria(facturas, valor)
    if pos_bin == real:
        veredicto = "CORRECTO"
    else:
        veredicto = "FALLA"
    print(valor, "\t", real, "\t", pos_bin, "\t", comp_bin, "\t\t", veredicto)

# Paso 4: traza buscando 7041
print()
print("=== TRAZA BUSCANDO 7041 ===")
posicion, comparaciones = binaria_con_traza(facturas, 7041)
print("Posición devuelta:", posicion, " Comparaciones:", comparaciones)

# Paso 6: búsqueda segura
print()
print("=== BÚSQUEDA SEGURA ===")
print("Buscado\tReal\tSegura\tComparaciones\tVeredicto")
print("-------\t----\t------\t-------------\t---------")
for valor in buscados:
    real, comp_lineal = busqueda_lineal(facturas, valor)
    pos_seg, comp_seg = busqueda_segura(facturas, valor)
    if pos_seg == real:
        veredicto = "CORRECTO"
    else:
        veredicto = "FALLA"
    print(valor, "\t", real, "\t", pos_seg, "\t", comp_seg, "\t\t", veredicto)

# Paso 7: copia ordenada
facturas_ordenadas = sorted(facturas)
print()
print("=== BINARIA SOBRE LA COPIA ORDENADA ===")
print("Buscado\tPos. en copia\tPos. real en facturas")
print("-------\t-------------\t---------------------")
for valor in buscados:
    pos_copia, comp = busqueda_binaria(facturas_ordenadas, valor)
    pos_real, comp2 = busqueda_lineal(facturas, valor)
    print(valor, "\t", pos_copia, "\t\t", pos_real)