# Se tiene un matriz con n productos y se requiere saber cuántos productos
# están en oferta. Solución cree una matriz cuadrada e incremente la
# cantidad que productos en ofertas y muestre el total

# Definición de la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad, en_oferta):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.en_oferta = en_oferta

    def __repr__(self):
        return f'Producto("{self.nombre}", {self.precio}, {self.cantidad}, {"En oferta" if self.en_oferta else "No en oferta"})'

# Función para contar los productos en oferta
def contar_productos_en_oferta(matriz):
    total_ofertas = 0
    for fila in matriz:
        for producto in fila:
            if producto.en_oferta:
                total_ofertas += 1
    return total_ofertas

# Función para imprimir la matriz de productos
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    # Crear la matriz de productos
    matriz_productos = [
        [Producto("Producto 1", 100, 10, True), Producto("Producto 2", 200, 20, False), Producto("Producto 3", 300, 30, True)],
        [Producto("Producto 4", 400, 40, False), Producto("Producto 5", 500, 50, True), Producto("Producto 6", 600, 60, False)],
        [Producto("Producto 7", 700, 70, True), Producto("Producto 8", 800, 80, False), Producto("Producto 9", 900, 90, True)]
    ]

    print("Matriz de productos:")
    imprimir_matriz(matriz_productos)

    # Contar los productos en oferta
    total_ofertas = contar_productos_en_oferta(matriz_productos)
    print(f"\nTotal de productos en oferta: {total_ofertas}")

if __name__ == "__main__":
    main()