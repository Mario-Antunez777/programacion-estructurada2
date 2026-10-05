menu = ("Gallo pinto", "Nacatamal", "Quesillo")
precios = (60.00, 90.00, 70.00)

# precios[0] = 65.00   (da TypeError porque las tuplas no se pueden modificar)

print("Precios originales:", precios)

lista_precios = list(precios)
for i in range(len(lista_precios)):
    lista_precios[i] = round(lista_precios[i] * 1.10, 2)
nuevos_precios = tuple(lista_precios)

print("Precios con aumento:", nuevos_precios)

menu_ampliado = menu + ("Vigorón",)

print("Menú ampliado:", menu_ampliado)
print("Cantidad de platos:", len(menu_ampliado))
print("¿nuevos_precios es tupla?:", type(nuevos_precios) == tuple)