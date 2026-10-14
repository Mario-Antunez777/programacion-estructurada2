def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones = comparaciones + 1
        if lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones


print("Calcular sin ejecutar")
n = 8000
print("Mejor caso:", 1, "comparaciones")
print("Caso promedio:", (n + 1) / 2, "comparaciones")
print("Peor caso:", n, "comparaciones")
print()

print("Comprobacion con pruebas")
codigos = list(range(1, n + 1))

pos, comp = busqueda_lineal(codigos, 1)
print("Mejor caso:", comp, "comparaciones")

pos, comp = busqueda_lineal(codigos, 0)
print("Peor caso:", comp, "comparaciones")

total = 0
for valor in codigos:
    pos, comp = busqueda_lineal(codigos, valor)
    total = total + comp
print("Caso promedio:", total / n, "comparaciones")
