def contar(lista, objetivo):
    cantidad = 0
    for i in range(len(lista)):
        if lista[i] == objetivo:
            cantidad = cantidad + 1
    return cantidad


print("Contar ocurrencias")
notas = [78, 92, 65, 92, 88]
print("El 92 aparece", contar(notas, 92), "veces")
print("El 100 aparece", contar(notas, 100), "veces")