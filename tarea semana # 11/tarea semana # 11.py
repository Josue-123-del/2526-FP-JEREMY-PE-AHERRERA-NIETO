def main():
    # Crear una matriz de tamaño 5x5
    filas = 5
    columnas = 5
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Solicitar al usuario ingresar los valores
    print("=" * 50)
    print("INGRESO DE DATOS PARA MATRIZ 5x5")
    print("=" * 50)

    for fila in range(filas):
        for columna in range(columnas):
            while True:
                try:
                    valor = float(input(f"Ingrese el valor para posición [{fila}][{columna}]: "))
                    matriz[fila][columna] = valor
                    break
                except ValueError:
                    print("Error: Por favor, ingrese un número válido.")

    # Mostrar la matriz ingresada
    print("\n" + "=" * 50)
    print("MATRIZ INGRESADA:")
    print("=" * 50)

    # Mostrar encabezado de columnas
    print("       ", end="")
    for columna in range(columnas):
        print(f"Col{columna}     ", end="")
    print("\n" + "-" * 50)

    # Mostrar cada fila con su encabezado
    for fila in range(filas):
        print(f"Fila{fila}", end=" | ")
        for columna in range(columnas):
            valor = matriz[fila][columna]
            # Formatear el número para alinearlo correctamente
            if isinstance(valor, float) and valor == int(valor):
                print(f"{int(valor):>6} ", end="")
            else:
                print(f"{valor:>6.2f} ", end="")
        print()

    print("=" * 50)
    print("¡Proceso completado exitosamente!")
    print("=" * 50)


if _name_ == "_main_":
    main()