print("Clase 05 - Paradigma orientado a objetos")

# Molde Persona
class Persona:

    # Método constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

persona1 = Persona("Juan", 25)
persona2 = Persona("Ana", 30)

persona1.presentarse()
persona2.presentarse()

print("------------------------------------")

# Enunciado.
# 1. Crear una clase (molde) producto
# 2. Tiene que tener un constructor para inicializar el nombre, categoria y precio del producto
# 3. aplicar_descuento -> Tiene que tener el comportamiento parap oder aplicar descuento. Producto con 10% de descuento
# descuento = precio * porcentaje / 100 
# precio = precio - descuento
# 4. mostrar -> Otro comportamiento que va a mostrar en la consola El nombre del producto, la categoria y el precio.
