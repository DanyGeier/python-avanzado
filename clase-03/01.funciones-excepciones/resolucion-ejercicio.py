def promedio(*argumentos):
    print("----------> ", argumentos)

    return sum(argumentos) / len(argumentos)

print(f"El promedio de esta lista es: {promedio(2, 4, 8, 10, 12, 33)}")
print(f"El promedio de esta lista es: {promedio(3, 5, 9, 15, 20, 35)}")
print(f"El promedio de esta lista es: {promedio(23, 24, 14, 19)}")

## -------------------------------------------------------
## -------------------------------------------------------

nombre = input("Ingresar nombre: ")
edad = int(input("Ingresar edad: "))
ciudad = input("Ingresar ciudad: ")
profesion = input("Ingresar profesión: ")

def crear_perfiles(**usuarios):
    print(usuarios)
    
crear_perfiles(
    nombre = nombre,
    edad = edad,
    ciudad = ciudad,
    profesion = profesion
)

notas= []
for i in range(3):
    notas.append(int(input(f"Ingresar nota {i+1}:")))
def calcular_promedio(*notas):
    return sum(notas)/len(notas)
print(calcular_promedio(*notas))