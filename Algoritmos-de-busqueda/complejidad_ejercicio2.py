def busqueda_inversa(lista, objetivo):
    comparaciones = 0
    i = len(lista) - 1
    while i >= 0:
        comparaciones = comparaciones + 1
        if lista[i] == objetivo:
            return i, comparaciones
        i = i - 1
    return -1, comparaciones


print("Buscar desde el final")
n = 1000
codigos = list(range(1, n + 1))

pos, comp = busqueda_inversa(codigos, 1000)
print("Mejor caso:", comp, "comparaciones")

pos, comp = busqueda_inversa(codigos, 0)
print("Peor caso:", comp, "comparaciones")

total = 0
for valor in codigos:
    pos, comp = busqueda_inversa(codigos, valor)
    total = total + comp
print("Caso promedio:", total / n, "comparaciones")