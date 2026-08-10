from database import Database
from alumno import Alumno

db = Database()

db.crear_tabla()

alumno = Alumno(
    "Ana",
    "Gomez",
    25,
    "ana@gmail.com",
    "Python"
)

db.insertar_alumno(alumno)