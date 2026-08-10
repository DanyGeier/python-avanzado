class Producto:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * porcentaje / 100
        self.precio = self.precio - descuento


    def mostrar(self):
        print(f"Nombre: {self.nombre}\n")
        print(f"Categoria: {self.categoria}\n")
        print(f"Precio: {self.precio}\n")

producto1 = Producto("PC", "Informatica", 222.4)
producto1.mostrar()

producto1.aplicar_descuento(10)
producto1.mostrar()
