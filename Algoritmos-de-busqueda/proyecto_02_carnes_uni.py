# Proyecto 2 · Consulta de estudiantes por carné UNI
# Nombre: Mario Andres Antunez Rivera
# Carné: 6B9A59C2


carnes = ["2023-0118U", "2023-0274U", "2023-0391U", "2023-0456U", "2023-0582U",
          "2023-0647U", "2023-0733U", "2023-0819U", "2023-0905U", "2023-1042U",
          "2024-0063U", "2024-0127U", "2024-0215U", "2024-0298U", "2024-0344U",
          "2024-0410U", "2024-0487U", "2024-0535U", "2024-0619U", "2024-0702U",
          "2024-0788U", "2024-0861U", "2025-0034U", "2025-0109U", "2025-0186U",
          "2025-0252U", "2025-0329U", "2025-0413U", "2025-0497U", "2025-0560U"]

nombres = ["María José Rivas Zeledón", "Carlos Andrés Mairena López",
           "Ana Gabriela Espinoza Rugama", "Luis Fernando Obando Castillo",
           "Kevin Josué Blandón Pérez", "Fernanda Isabel Rocha Gutiérrez",
           "José Daniel Talavera Ruiz", "Valeria Sofía Centeno Aráuz",
           "Bryan Alexander Chavarría Mendoza", "Katherine Lucía Herrera Picado",
           "Jorge Luis Moncada Úbeda", "Daniela Alejandra Somarriba Cruz",
           "Eduardo Josué Castellón Vega", "Mariela Auxiliadora Lanuza Torres",
           "Óscar Danilo Pineda Hernández", "Ximena Carolina Galeano Molina",
           "Francisco Javier Ortega Zamora", "Heydi Massiel Matamoros Sáenz",
           "Ernesto Rafael Dávila Membreño", "Gissell Marcela Arana Quintero",
           "Axel Mauricio Jarquín Salgado", "Scarleth Yahoska Romero Huete",
           "Josué David Sequeira Bermúdez", "Camila Fernanda Urbina Narváez",
           "Héctor Manuel Ponce Largaespada", "Yaritza Lisseth Morales Duarte",
           "Marvin Antonio Sandino Flores", "Nohelia Patricia Cerda Valle",
           "Wilber Josué Vílchez Martínez", "Andrea Belén Guevara Mejía"]

carreras = ["Ingeniería en Sistemas", "Ingeniería Civil", "Ingeniería Industrial",
            "Ingeniería Eléctrica", "Ingeniería en Computación", "Arquitectura",
            "Ingeniería en Sistemas", "Ingeniería Química", "Ingeniería Mecánica",
            "Ingeniería Electrónica", "Ingeniería Agrícola", "Ingeniería en Sistemas",
            "Ingeniería Civil", "Ingeniería Industrial", "Ingeniería Eléctrica",
            "Ingeniería en Computación", "Arquitectura", "Ingeniería en Sistemas",
            "Ingeniería Química", "Ingeniería Civil", "Ingeniería Mecánica",
            "Ingeniería Electrónica", "Ingeniería en Sistemas", "Ingeniería Industrial",
            "Ingeniería Agrícola", "Ingeniería en Computación", "Ingeniería Civil",
            "Ingeniería en Sistemas", "Ingeniería Eléctrica", "Arquitectura"]



def carne_valido(carne):
    if len(carne) != 10:
        return False
    if not carne[0:4].isdigit():
        return False
    if carne[4] != "-":
        return False
    if not carne[5:9].isdigit():
        return False
    if carne[9] != "U":
        return False
    return True


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


def buscar_nombre(lista, buscado):
    posicion = -1
    comparaciones = 0
    i = 0
    while i < len(lista) and posicion == -1:
        comparaciones = comparaciones + 1
        if lista[i].lower() == buscado.lower():
            posicion = i
        i = i + 1
    return posicion, comparaciones


def buscar_todos(lista, buscado):
    posiciones = []
    comparaciones = 0
    i = 0
    while i < len(lista):
        comparaciones = comparaciones + 1
        if lista[i] == buscado:
            posiciones.append(i)
        i = i + 1
    return posiciones, comparaciones


opcion = ""
while opcion != "4":
    print("=== REGISTRO ACADÉMICO UNI · CONSULTA ===")
    print("1. Buscar por carné")
    print("2. Buscar por nombre completo")
    print("3. Listar estudiantes de una carrera")
    print("4. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        carne = input("Carné: ").strip()
        if carne_valido(carne) == False:
            print("Formato inválido. Ejemplo de carné: 2024-0153U")
        else:
            pos_b, comp_b = busqueda_binaria(carnes, carne)
            pos_l, comp_l = busqueda_lineal(carnes, carne)
            if pos_b == -1:
                print("No existe un estudiante con ese carné.")
                print("Búsqueda lineal : " + str(comp_l) + " comparaciones")
                print("Búsqueda binaria: " + str(comp_b) + " comparaciones")
            else:
                print("Estudiante:", nombres[pos_b])
                print("Carrera   :", carreras[pos_b])
                print("Búsqueda lineal : posición " + str(pos_l) + ", " + str(comp_l) + " comparaciones")
                print("Búsqueda binaria: posición " + str(pos_b) + ", " + str(comp_b) + " comparaciones")
        print()

    elif opcion == "2":
        nombre = input("Nombre completo: ").strip()
        pos, comp = buscar_nombre(nombres, nombre)
        if pos == -1:
            print("No existe un estudiante con ese nombre.")
            print("Búsqueda lineal: " + str(comp) + " comparaciones")
        else:
            print("Carné   :", carnes[pos])
            print("Carrera :", carreras[pos])
            print("Búsqueda lineal: posición " + str(pos) + ", " + str(comp) + " comparaciones")
        print()

    elif opcion == "3":
        carrera = input("Carrera: ").strip()
        posiciones, comp = buscar_todos(carreras, carrera)
        if len(posiciones) == 0:
            print("No hay estudiantes en esa carrera.")
            print("Total: 0 estudiantes · " + str(comp) + " comparaciones")
        else:
            i = 0
            while i < len(posiciones):
                p = posiciones[i]
                print("  " + carnes[p] + "  " + nombres[p])
                i = i + 1
            print("Total: " + str(len(posiciones)) + " estudiantes · " + str(comp) + " comparaciones")
        print()

    elif opcion == "4":
        print("Hasta luego.")

    else:
        print("Opción no válida.")
        print()