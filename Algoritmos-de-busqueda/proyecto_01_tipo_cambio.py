# Proyecto 1 · Tipo de cambio del BCN
# Nombre: Mario Andres Antunez Rivera .
# Carné: 6B9A59C2

fechas = ["2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06",
          "2023-10-09", "2023-10-10", "2023-10-11", "2023-10-12", "2023-10-13",
          "2023-10-16", "2023-10-17", "2023-10-18", "2023-10-19", "2023-10-20",
          "2023-10-23", "2023-10-24", "2023-10-25", "2023-10-26", "2023-10-27",
          "2023-10-30", "2023-10-31"]

tasas = [36.4330, 36.4340, 36.4350, 36.4360, 36.4370,
         36.4400, 36.4410, 36.4420, 36.4430, 36.4440,
         36.4470, 36.4480, 36.4490, 36.4500, 36.4510,
         36.4540, 36.4550, 36.4560, 36.4570, 36.4580,
         36.4610, 36.4620]


def busqueda_lineal(lista, buscado):
    posicion = -1
    comparaciones = 0
    i = 0
    while i < len(lista) and posicion == -1:
        comparaciones = comparaciones + 1
        if lista[i] == buscado:
            posicion = i
        i = i + 1
    return posicion, comparaciones


def busqueda_binaria(lista, buscado):
    izq = 0
    der = len(lista) - 1
    posicion = -1
    comparaciones = 0
    while izq <= der and posicion == -1:
        medio = (izq + der) // 2
        comparaciones = comparaciones + 1
        if lista[medio] == buscado:
            posicion = medio
        elif lista[medio] < buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return posicion, comparaciones


fecha = "2023-10-17"
pos_l, comp_l = busqueda_lineal(fechas, fecha)
pos_b, comp_b = busqueda_binaria(fechas, fecha)
print("Tipo de cambio: C$", round(tasas[pos_b], 4), "por US$ 1")
print("Búsqueda lineal : posición", pos_l, "con", comp_l, "comparaciones")
print("Búsqueda binaria: posición", pos_b, "con", comp_b, "comparaciones")