temp_managua = (31, 33, 32, 34, 30, 29, 32)
temp_esteli = (24, 26, 25, 23, 27, 25, 24)

def resumen(datos):
    minima = min(datos)
    maxima = max(datos)
    promedio = sum(datos) / len(datos)
    return (minima, maxima, promedio)

minima, maxima, promedio = resumen(temp_managua)
print("Managua -> mínima:", minima, "°C, máxima:", maxima, "°C, promedio:", round(promedio, 1), "°C")

minima, maxima, promedio = resumen(temp_esteli)
print("Estelí -> mínima:", minima, "°C, máxima:", maxima, "°C, promedio:", round(promedio, 1), "°C")