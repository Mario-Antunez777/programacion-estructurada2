def contar_lineal(lista, objetivo):
    revisiones = 0
    i = 0
    encontrado = False
    while i < len(lista) and not encontrado:
        revisiones = revisiones + 1
        if lista[i] == objetivo:
            encontrado = True
        i = i + 1
    return revisiones


def contar_binaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    revisiones = 0
    encontrado = False
    while izq <= der and not encontrado:
        medio = (izq + der) // 2
        revisiones = revisiones + 1
        if lista[medio] == objetivo:
            encontrado = True
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return revisiones


tamanos = [2000, 4000, 8000, 16000, 32000]

for n in tamanos:
    lista = list(range(n))
    objetivo = n
    lin = contar_lineal(lista, objetivo)
    bina = contar_binaria(lista, objetivo)
    print("n =", n, "| lineal:", lin, "| binaria:", bina)
#Cada vez que n se duplica, la búsqueda lineal también hace el
#doble de revisiones (2000, 4000, 8000...), pero la binaria solo
#sube 1 revisión (11, 12, 13, 14, 15).