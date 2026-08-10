class Alumno:

    def __init__(self, nombre, apellido, edad, email, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.curso = curso

    def __str__(self): # troString()
        return (
            f"{self.nombre} {self.apellido} - "
            f"{self.edad} años - "
            f"{self.email} - "
            f"Curso: {self.curso}"
        )