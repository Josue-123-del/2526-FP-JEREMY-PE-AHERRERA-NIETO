def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

precio = 10
cantidad = 3

resultado = calcular_total(precio, cantidad)

print("===== CALCULO DE COMPRA =====")
print("Precio del producto:", precio)
print("Cantidad comprada:", cantidad)
print("Total a pagar:", resultado)
