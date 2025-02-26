# Dada una matriz que representa un almacén donde cada celda contiene un
# objeto Producto con atributos nombre, precio y cantidad, escribe un
# algoritmo que encuentre la ubicación (fila, columna) de un producto en
# una lisa de 30 productos buscar específico por su nombre.
# Solución: Recorre la matriz buscando el Producto cuyo nombre coincida
# con el buscado. Devuelve la posición de la celda.

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f'Producto("{self.nombre}", {self.precio}, {self.cantidad})'


# Función para encontrar la ubicación del producto en la matriz
def buscar_producto(matriz, producto):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna].nombre == producto:
                return (fila + 1, columna + 1)
    return None


def imprimir_matriz(matriz):
    for i in matriz:
        print(i)


def main():
    # Crear la matriz de productos
    matriz_productos = [
        [Producto("Producto 1", 100, 10), Producto("Producto 2", 200, 20), Producto("Producto 3", 300, 30)],
        [Producto("Producto 4", 400, 40), Producto("Producto 5", 500, 50), Producto("Producto 6", 600, 60)],
        [Producto("Producto 7", 700, 70), Producto("Producto 8", 800, 80), Producto("Producto 9", 900, 90)]
    ]

    print("Matriz de productos:")
    imprimir_matriz(matriz_productos)

    # Nombre del producto a buscar
    producto = "Producto 6"
    ubicacion = buscar_producto(matriz_productos, producto)

    if ubicacion:
        print(f"\nEl {producto} se encuentra en la fila {ubicacion[0]} y columna {ubicacion[1]}.")
    else:
        print(f"\nEl {producto} no se encuentra en la matriz.")


if __name__ == "__main__":
    main()
