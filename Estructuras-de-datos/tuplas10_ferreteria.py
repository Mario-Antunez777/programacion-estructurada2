# ---------- Parte A: catálogo ----------
catalogo = (
    ("P01", "Martillo", 250.00),
    ("P02", "Clavos 2 pulg (lb)", 45.00),
    ("P03", "Cinta métrica 5 m", 180.00),
    ("P04", "Brocha 3 pulg", 95.00),
    ("P05", "Lija #100", 15.00)
)

def buscar_producto(codigo):
    for producto in catalogo:
        if producto[0] == codigo:
            return producto
    return None

print(buscar_producto("P03"))
print(buscar_producto("P09"))

# ---------- Parte B: factura ----------
pedido = (("P03", 2), ("P01", 1), ("P05", 4), ("P09", 3))

def calcular_factura(pedido):
    subtotal = 0
    for codigo, cantidad in pedido:
        producto = buscar_producto(codigo)
        if producto == None:
            print("Código", codigo, "no existe")
        else:
            nombre = producto[1]
            precio = producto[2]
            importe = precio * cantidad
            subtotal = subtotal + importe
            print(nombre + ":", cantidad, "x C$", format(precio, ".2f"), "= C$", format(importe, ".2f"))
    iva = subtotal * 0.15
    total = subtotal + iva
    return (subtotal, iva, total)

subtotal, iva, total = calcular_factura(pedido)

print("Subtotal: C$", format(subtotal, ".2f"))
print("IVA (15%): C$", format(iva, ".2f"))
print("Total: C$", format(total, ".2f"))

