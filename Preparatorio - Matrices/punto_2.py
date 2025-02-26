# Dada una matriz de objetos Producto en una tienda, donde cada Producto
# tiene un atributo cantidad, escribe un algoritmo que sume todas las
# cantidades para determinar el inventario total de la tienda.
# Solución: Itera a través de cada celda de la matriz sumando el valor del
# atributo cantidad de cada objeto

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f'Producto("{self.nombre}", Precio: {self.precio}, Cantidad: {self.cantidad})'


# Función para calcular el inventario total
def calcular_inventario_total(matriz):
    inventario_total = 0

    for fila in matriz:
        for producto in fila:
            inventario_total += producto.cantidad
    return inventario_total


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

    # Calcular el inventario total
    inventario_total = calcular_inventario_total(matriz_productos)
    print(f"\nInventario total de la tienda: {inventario_total}")


if __name__ == "__main__":
    main()
