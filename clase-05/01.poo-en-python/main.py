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

print("# ------------------------------ Clase Cuenta")
print("Propiedades -> Atributos privados --> Para crear un atributo privado coloco '__' delante del atributo")

class Cuenta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # El atributo saldo es privado

    # Update
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
    # Update
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")
    # Read -> Getter
    def consultar_saldo(self):
        return self.__saldo

cuenta = Cuenta("Juan", 10000)
print(cuenta.titular)
cuenta.depositar(5000)
cuenta.retirar(3000)

print(cuenta.consultar_saldo())

print("-------------------------------- Trabajando con Herencia")
# La clase Padre -> Vehiculo (La generica)
# La clase Auto y Moto

# La clase Padre -> va a tener el atributo 'marca'
# La clase Padre -> el método avanzar -> print("El vehiculo avanza...")

# La clase hija -> Auto -> Método tocar_bocina
# La clase hija -> Moto -> Método hacer_willy

# Averiguar como hacer herencia y como crear una clase abstracta. (Googlear buscando la solución)

from abc import ABC, abstractmethod

class Vehiculo(ABC):

    def __init__(self, marca):
        self.marca = marca

    @abstractmethod
    def avanzar(self):
        print("El vehiculo avanza...")

class Auto(Vehiculo):

    def avanzar(self):
        super().avanzar()

    def tocar_bocina(self):
        print("BEEP BEEP")

class Moto(Vehiculo):

    def avanzar(self):
        super().avanzar()

    def hacer_willy(self):
        print("Levanta la rueda delantera...")

vehiculo1 = Auto("Toyota")
vehiculo2 = Moto("Honda")

vehiculo1.avanzar()
vehiculo1.tocar_bocina()

vehiculo2.avanzar()
vehiculo2.hacer_willy()

print(Auto.__bases__)
print(Moto.__bases__) # Padres directos
print(Auto.__mro__) # orden completo en el que python busca atributos y métodos