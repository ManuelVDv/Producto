import mysql.connector

from MySql.Persona import Persona
from MySql.Estudiante import Estudiante
from MySql.Profesor import Profesor

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="registrodb"
)

cursor = conn.cursor()

def registrar_persona():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    tipo = input("Tipo (E para Estudiante, P para Profesor): ").strip().upper()

    if tipo == "E":
        programa = input("Programa de estudio: ")
        persona = Estudiante(nombre, edad, programa)
    elif tipo == "P":
        materia = input("Materia que enseña: ")
        persona = Profesor(nombre, edad, materia)
    else:
        print("Tipo no válido.")
        return

    # Registrar la persona en la base de datos
    nombre_persona = persona.get_nombre()
    edad_persona = persona.get_edad()
    if isinstance(persona, Estudiante):
        programa = persona.get_programa()
        sql = "INSERT INTO personas (nombre, edad, programa) VALUES (%s, %s, %s)"
        val = (nombre_persona, edad_persona, programa)
    elif isinstance(persona, Profesor):
        materia = persona.get_materia()
        sql = "INSERT INTO personas (nombre, edad, materia) VALUES (%s, %s, %s)"
        val = (nombre_persona, edad_persona, materia)
    cursor.execute(sql, val)

    # Registrar el usuario en la tabla usuarios
    sql_usuario = "INSERT INTO usuarios (nombre, contrasena) VALUES (%s, %s)"
    val_usuario = (usuario, contrasena)
    cursor.execute(sql_usuario, val_usuario)

    conn.commit()
    print("Persona registrada con éxito.")


# Función para iniciar sesión
def iniciar_sesion():
    nombre = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    cursor.execute("SELECT * FROM usuarios WHERE nombre = %s AND contrasena = %s", (nombre, contrasena))
    usuario = cursor.fetchone()

    if usuario:
        print("Ingreso exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")


while True:
    print("Opciones:")
    print("1. Registrar Persona")
    print("2. Iniciar Sesión")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        registrar_persona()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")


cursor.close()
conn.close()
