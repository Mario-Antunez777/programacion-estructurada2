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


opcion = ""
while opcion != "4":
    print("=== TIPO DE CAMBIO OFICIAL · OCTUBRE 2023 ===")
    print("1. Consultar tipo de cambio de una fecha")
    print("2. Convertir dólares a córdobas")
    print("3. Convertir córdobas a dólares")
    print("4. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        fecha = input("Fecha (AAAA-MM-DD): ")
        pos_l, comp_l = busqueda_lineal(fechas, fecha)
        pos_b, comp_b = busqueda_binaria(fechas, fecha)
        if pos_b == -1:
            print("No hay registro para esa fecha (fin de semana o fuera del período).")
            print("Búsqueda lineal :", comp_l, "comparaciones")
            print("Búsqueda binaria:", comp_b, "comparaciones")
        else:
            print("Tipo de cambio: C$", round(tasas[pos_b], 4), "por US$ 1")
            print("Búsqueda lineal : posición", pos_l, "con", comp_l, "comparaciones")
            print("Búsqueda binaria: posición", pos_b, "con", comp_b, "comparaciones")
        print()

    elif opcion == "2":
        fecha = input("Fecha (AAAA-MM-DD): ")
        dolares = float(input("Monto en dólares: "))
        if dolares <= 0:
            print("El monto debe ser mayor que cero.")
        else:
            pos, comp = busqueda_binaria(fechas, fecha)
            if pos == -1:
                print("No hay registro para esa fecha (fin de semana o fuera del período).")
            else:
                cordobas = dolares * tasas[pos]
                print("US$", round(dolares, 2), "equivalen a C$", round(cordobas, 2))
        print()

    elif opcion == "3":
        fecha = input("Fecha (AAAA-MM-DD): ")
        cordobas = float(input("Monto en córdobas: "))
        if cordobas <= 0:
            print("El monto debe ser mayor que cero.")
        else:
            pos, comp = busqueda_binaria(fechas, fecha)
            if pos == -1:
                print("No hay registro para esa fecha (fin de semana o fuera del período).")
            else:
                dolares = cordobas / tasas[pos]
                print("C$", round(cordobas, 2), "equivalen a US$", round(dolares, 2))
        print()

    elif opcion == "4":
        print("Hasta luego.")

    else:
        print("Opción no válida.")
        print()