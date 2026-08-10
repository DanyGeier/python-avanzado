import sqlite3

class Database:

    def __init__(self, nombre_db="escuela.db"):
        self.nombre_db = nombre_db

    def conectar(self):
        return sqlite3.connect(self.nombre_db)

    def crear_tabla(self):

        conexion = self.conectar()

        cursor = conexion.cursor()

        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                edad INTEGER,
                email TEXT,
                curso TEXT
            )
            """)

        conexion.commit()
        conexion.close()

    def insertar_alumno(self, alumno):

        conexion = self.conectar()

        cursor = conexion.cursor()

        cursor.execute("""
                INSERT INTO alumnos
                (nombre, apellido, edad, email, curso)
                VALUES (?, ?, ?, ?, ?)
            """, (
                alumno.nombre,
                alumno.apellido,
                alumno.edad,
                alumno.email,
                alumno.curso
            ))

        conexion.commit()
        conexion.close()

        print("Alumno creado")