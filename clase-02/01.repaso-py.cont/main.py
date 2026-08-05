""" 
Crear un programa en python que simule el registro de una compra

El programa debe:

1. Pedir al usuario su nombre (almacenarlo en una variable) -> input()
2. Pedir el producto que desea comprar. -> input()
3. Pedir el precio unitario. -> input()
4. Pedir la cantidad.
5. Guardar los datos de la compra en un diccionario.
6. Calcular el subtotal.
7. Si el subtotal es mayor o igual a $50.000, aplicar un 10% de descuento
8. Mostrar un resumen de la compra.
9. Informar si el cliente obtuvo descuento

# -------------- #
Nombre: Ana
Producto: Teclado
Precio: 35000
Cantidad: 2

=========== RESUMEN DE COMPRA ============

Cliente: Ana
Producto: Teclado
Precio unitario: $35000
Cantidad: 2
Subtotal: $70000
Descuento: 10% si supera los $50000

Obtuviste un descuento
"""


print('# ! Colecciones')


"""
list -> [10, 20, 30] -> Ordenada y mutable (array de javascript)
tuple -> (10, 20, 30) -> Ordenada e inmutable
set -> {10, 20, 30} -> No admite duplicados
dict -> {"nombre": "Ana"} -> Clave -> valor (objeto de javascript)
"""

"""
--- # ! estructuras de control
if
if / else
if / elif / else
--- # ! estructuras de repetición
for
while
---
break
continue
"""

# Prueba de escritorio -> 2 y con 5
# numeor -> 2 -> No se va a imprimir 
# numero -> 5 -> Se imprime el valor
for numero in range(1, 11):

    if numero % 2 == 0:
        print('par -> ', numero)
        continue

    print(numero)

# Aplicación de Datos personales
# Pedir al usuario

# -> nombre
# -> edad
# -> Altura

# Mostrar el tipo de dato ingresado

"""
print()
input()
type()
len()
int()
float()
str()
bool()
range()
sum()
min()
max()
"""

def datos_personales():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura: "))

    return {
        "nombre": nombre,
        "edad": edad,
        "altura": altura
    }

usuario = datos_personales()

def mostrar_datos(usuario):
    print("====== DATOS PERSONALES DEL USUARIO ======\n")
    print(f"Nombre: {usuario['nombre']} \nTipo de dato: {type(usuario['nombre'])}")
    print(f"Edad: {usuario['edad']} \nTipo de dato: {type(usuario['edad'])}")
    print(f"Altura: {usuario['altura']} \nTipo de dato: {type(usuario['altura'])}")

mostrar_datos(usuario)

## Ejercicio 2: Crear un array (lista) de notas

# notas = [2, 4] con 5 o 6 notas

# Calcular

# * Cantidad de notas
# * Suma
# * Nota minima
# * Nota maxima
# * Promedio

def calcular_notas():
    notas = [2, 4, 5, 6, 9, 10]
    cantidad_notas = len(notas)
    suma = sum(notas)
    nota_minima = min(notas)
    nota_maxima = max(notas)
    promedio = suma / cantidad_notas

    print("===== NOTAS =====\n ")
    print("Cantidad de notas: ", cantidad_notas)
    print("Suma de notas: ", suma)
    print("Nota mínima: ", nota_minima)
    print("Nota máxima: ", nota_maxima)
    print("Promedio de notas: ", promedio)

calcular_notas()

## Ejercicio 3: Longitud de una palabra

# 1. Pedir una palabra
# 2. La cantidad de caracteres

def longitud_palabra():
    palabra = input("Ingrese una palabra: ")

def calculo_longitud()
    cantidad_letras = len(palabra)

longitud_palabra()

## Ejercicio 4: Conversor de edad
# Pedir la edad de una persona y mostrar su edad dentro de 10 años.

## Ejercicio 5: Numeros del 1 al 10
# Mostrar los números del 1 al 10 utilizando una función integrada

