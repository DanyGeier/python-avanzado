def promedio(*argumentos):
    print("----------> ", argumentos)

    return sum(argumentos) / len(argumentos)

print(f"El promedio de esta lista es: {promedio(2, 4, 8, 10, 12, 33)}")
print(f"El promedio de esta lista es: {promedio(3, 5, 9, 15, 20, 35)}")
print(f"El promedio de esta lista es: {promedio(23, 24, 14, 19)}")