ruta = ("esteli", "managua", "148", "12", "170.000")

distancia = float(ruta[2])
pasajeros = int(ruta[3])
costo_total = float(ruta[4])

print(ruta[0:2])
print("Distancia:", distancia)
print("Pasajeros:", pasajeros)
print("Costo por kilometro:", costo_total / distancia)
print("ruta de regreso:", ruta[0:2][::-1])
