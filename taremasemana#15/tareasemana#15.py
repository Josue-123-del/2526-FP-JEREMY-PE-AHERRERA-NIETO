# Tarea: Colecciones de datos en Python
# Estudiante: [Tu Nombre]
# Universidad Estatal Amazónica

def ejecutar_sistema_inventario():
    # 1. CREACIÓN DE LA COLECCIÓN (Diccionario: Producto -> Precio)
    # Un diccionario es ideal porque asocia una clave única con un valor.
    inventario = {
        "Teclado Mecánico": 45.50,
        "Mouse Gamer": 25.00,
        "Monitor 24 pulgadas": 160.00
    }

    print("--- SISTEMA DE GESTIÓN DE INVENTARIO ---")

    # 2. AGREGAR DATOS
    # Añadimos un nuevo elemento al diccionario
    inventario["Audífonos"] = 35.00
    print(f"Se ha agregado un nuevo producto: Audífonos")

    # 3. MOSTRAR LA INFORMACIÓN ALMACENADA
    # Usamos un bucle for para recorrer y mostrar los elementos
    print("\nLista de productos actuales:")
    for producto, precio in inventario.items():
        print(f" * Producto: {producto} | Precio: ${precio:.2f}")

    # 4. OPERACIÓN BÁSICA: BUSCAR Y ELIMINAR
    producto_a_buscar = "Mouse Gamer"

    if producto_a_buscar in inventario:
        print(f"\n--- Búsqueda exitosa ---")
        print(f"El precio de '{producto_a_buscar}' es ${inventario[producto_a_buscar]}")

        # Eliminamos el producto buscado para cumplir con la operación de "eliminar"
        del inventario[producto_a_buscar]
        print(f"Nota: Se ha eliminado '{producto_a_buscar}' del inventario.")
    else:
        print(f"\nEl producto '{producto_a_buscar}' no existe.")

    # Mostrar inventario final para verificar cambios
    print("\nInventario final actualizado:")
    for p, v in inventario.items():
        print(f" - {p}: ${v:.2f}")


if _name_ == "_main_":
    ejecutar_sistema_inventario()
