# Crear matriz de asientos (3 filas x 4 columnas)
# 0 = asiento libre
# 1 = asiento reservado

asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Pedir datos al usuario
print("=== RESERVA DE ASIENTOS ===")
f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

# Marcar asiento como reservado
asientos[f][c] = 1

# Mostrar el estado de la sala
print("\nEstado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
