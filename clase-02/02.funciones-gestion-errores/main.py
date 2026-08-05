print("Funciones y Gestión de errores")

""" 
Anatomia de las funciones 

# ! Defininiendo una función

def nombre_función(parametro1, parametro2, parametro3):
    instruccion1 
    instruccion2
    instrucion3
    
# ! Ejecutar, invocar o llamar
nombre_función(argumento1, argumento2, argumento3)
"""

print('# ! Función sin parámetros')

def saludar():
    print("Hola")


saludar()
saludar()
saludar()

print('# ! Función con parámetros')

def bienvenido(nombre):
    print("Bienvenido", nombre)

bienvenido("Ana")
bienvenido("Juana")
bienvenido("Rigoberto")
bienvenido("")

print('# ! Funciones que tienen retorno')

def resta(a, b):
    resultado = a - b
    return resultado

resultado = resta(10, 4)
print(resultado) # 6
resultado = resta(16, 3)
print(resultado) # 13

