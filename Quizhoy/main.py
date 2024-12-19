import json
from modules.gestion_usuarios import registrar_camper as registrar_camper_usuario

import hashlib

# Cargar y guardar datos
def cargar_datos(nombre_archivo="campuslands.json"):
    try:
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error al leer el archivo de datos.")
        return None

def guardar_datos(datos, nombre_archivo="campuslands.json"):
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Función de registro de usuario
def registrar_usuario(usuarios):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya existe.")
        return usuarios

    contrasena = input("Ingrese su contraseña: ")
    hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

    usuarios[nombre_usuario] = {"contrasena": hash_contrasena}
    print("Usuario registrado exitosamente.")
    return usuarios

# Función de inicio de sesión
def iniciar_sesion(usuarios):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario not in usuarios:
        print("Usuario no encontrado.")
        return False

    contrasena = input("Ingrese su contraseña: ")
    hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

    if usuarios[nombre_usuario]["contrasena"] == hash_contrasena:
        print("Inicio de sesión exitoso.")
        return True
    else:
        print("Contraseña incorrecta.")
        return False

# Función de autenticación usuario
def menu_autenticacion(data):
    usuarios = data.get("usuarios", {})
    while True:
        print("\n--- Menú de Autenticación ---")
        print("1. Usuario Nuevo")
        print("2. Usuario Registrado")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuarios = registrar_usuario(usuarios)
            data["usuarios"] = usuarios
            guardar_datos(data)
        elif opcion == "2":
            if iniciar_sesion(usuarios):
                return True
            else:
                print("Error en la autenticación.")
        elif opcion == "3":
            return False
        else:
            print("Opción inválida. Intente nuevamente.")
            # Función de autenticación usuario
def menu_autenticacion_admin(data):
    usuarios = data.get("usuarios", {})
    while True:
        print("\n--- Menú de Autenticación ---")
        print("1. Usuario ADMIN")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            if iniciar_sesion(usuarios):
                return True
            else:
                print("Error en la autenticación.")
        elif opcion == "2":
            return False
        else:
            print("Opción inválida. Intente nuevamente.")


# Menú de Camper
def menu_usuario(data):
    id_camper = input("Ingrese su ID de Camper: ")
    
    # Buscar camper por ID
    camper = next((c for c in data["campers"] if c["id"] == id_camper), None)

    if camper is None:
        print("Camper no encontrado.")
        return data

    while True:
        print("\n--- Menú Camper ---")
        print("1. Completar datos personales")
        print("2. Ver estado")
        print("3. Ver notas")
        print("4. Ver ruta")
        print("5. Ver salón")
        print("6. Ver profesor")
        print("7. Volver al login")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            data = registrar_camper_usuario(data)
            guardar_datos(data)
        elif opcion == "2":
            estado = camper.get('aprobado', False)  # Por defecto, False si no tiene 'aprobado'
            print(f"Estado del camper con ID {id_camper}: {'Aprobado' if estado else 'Pendiente'}")
        elif opcion == "3":
            print(f"Notas del camper con ID {id_camper}: {camper.get('nota', 'No asignada')}")
        elif opcion == "4":
            print(f"Ruta asignada al camper con ID {id_camper}: {camper.get('ruta_asignada', 'No asignada')}")
        elif opcion == "5":
            print(f"Salón asignado al camper con ID {id_camper}: {camper.get('salon', 'No asignado')}")
        elif opcion == "6":
            print(f"Profesor asignado al camper con ID {id_camper}: {camper.get('trainer_asignado', 'No asignado')}")
        elif opcion == "7":
            return data
        elif opcion == "8":
            break
        else:
            print("Opción inválida.")
    return data

# Menú de Admin
def menu_Admin(data):
    while True:
        print("\n--- Menú Admin ---")
        print("---Que haras hoy admin?---")
        print("1. Registro y Gestión de Usuarios:")
        print("2. Seguimiento del Historial de Usuarios")
        print("3. Personalización de Servicios:")
        print("4. Gestión de la Fidelización de Clientes:")
        print("8. Salir")
        
        
# Menú principal
def menu_principal(data):
    while True:
        print("\n--- Menú Principal Movistar---")
        print("1. Usuario")
        print("2. Admin")
        print("3. Salir")

        opcion = input("Seleccione un tipo de usuario: ")

        if opcion == "1":
            if menu_autenticacion(data):
                data = menu_usuario(data)
                guardar_datos(data)
        elif opcion == "2":
            if menu_autenticacion_admin(data):
                data = menu_Admin(data)
                guardar_datos(data)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")


