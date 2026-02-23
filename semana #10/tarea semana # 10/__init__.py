# Tarea: Matriz y creación de cuenta en GitHub
# Parte 1: Programa con matriz

# 1. Declarar una matriz de 3x3 con números enteros
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

# 2. Recorrer la matriz con un ciclo (anidado)
# 3. Imprimir todos los valores de la matriz en pantalla
print("Valores de la matriz:")

for i in range(3):        # Recorre las filas
    for j in range(3):    # Recorre las columnas
        print(matriz[i][j])
