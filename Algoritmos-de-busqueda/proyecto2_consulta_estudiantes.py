# Proyecto 2 · Consulta de estudiantes por carné UNI
# Nombre: Mario Andres Antunez Rivera
# Carné: 6B9A59C2

# Listas paralelas: la posición i de cada lista pertenece al mismo estudiante.
# Los carnés están ordenados de menor a mayor (necesario para la búsqueda binaria).
carnes = ["2023-0101U", "2023-0215U", "2023-0342U", "2023-0478U", "2023-0560U",
          "2023-0633U", "2023-0719U", "2023-0824U", "2023-0950U", "2023-1037U"]

nombres = ["Ana Lucía Pérez", "Carlos Martínez", "María José Gómez", "José Luis Rodríguez",
           "Sofía Hernández", "Luis Fernando Castro", "Karla Vanessa Rivas",
           "Juan Carlos Mendoza", "Daniela Sánchez", "Pedro Antonio Flores"]

carreras = ["Ing. en Computación", "Ing. Civil", "Ing. en Sistemas", "Ing. Industrial",
            "Ing. en Computación", "Arquitectura", "Ing. Eléctrica",
            "Ing. en Sistemas", "Ing. Química", "Ing. Mecánica"]

promedios = [88.5, 76.0, 91.2, 82.4, 95.0, 70.8, 85.3, 79.6, 90.1, 73.9]


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


def mostrar_estudiante(pos):
    print("Carné   :", carnes[pos])
    print("Nombre  :", nombres[pos])
    print("Carrera :", carreras[pos])
    print("Promedio:", promedios[pos])


opcion = ""
while opcion != "4":
    print("=== CONSULTA DE ESTUDIANTES · UNI ===")
    print("1. Consultar estudiante por carné")
    print("2. Listar todos los estudiantes")
    print("3. Ver promedio general")
    print("4. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        carne = input("Carné (AAAA-NNNNU): ").strip().upper()
        pos_l, comp_l = busqueda_lineal(carnes, carne)
        pos_b, comp_b = busqueda_binaria(carnes, carne)
        if pos_b == -1:
            print("No existe un estudiante con ese carné.")
            print("Búsqueda lineal :", comp_l, "comparaciones")
            print("Búsqueda binaria:", comp_b, "comparaciones")
        else:
            mostrar_estudiante(pos_b)
            print("Búsqueda lineal : posición", pos_l, "con", comp_l, "comparaciones")
            print("Búsqueda binaria: posición", pos_b, "con", comp_b, "comparaciones")
        print()

    elif opcion == "2":
        i = 0
        while i < len(carnes):
            print(carnes[i], "|", nombres[i], "|", carreras[i], "|", promedios[i])
            i = i + 1
        print()

    elif opcion == "3":
        suma = 0
        i = 0
        while i < len(promedios):
            suma = suma + promedios[i]
            i = i + 1
        print("Promedio general:", round(suma / len(promedios), 2))
        print()

    elif opcion == "4":
        print("Hasta luego.")

    else:
        print("Opción no válida.")
        print()