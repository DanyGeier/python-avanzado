def registrar_persona():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese su cuidad: ")

    with open("persona.txt", "w") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Ciudad: {ciudad}\n")

registrar_persona()

def leer_linea_a_linea():
    print("--- Datos leidos desde persona.txt ---\n")
    with open("persona.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())

leer_linea_a_linea()
