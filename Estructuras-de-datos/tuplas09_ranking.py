estudiantes = ("Ana", "Luis", "Carla", "José", "Marta")
notas_grupo = (78, 92, 85, 66, 95)

ranking = sorted(zip(notas_grupo, estudiantes), reverse=True)

for posicion, par in enumerate(ranking, start=1):
    nota, nombre = par
    print(str(posicion) + ".", nombre, "-", nota)