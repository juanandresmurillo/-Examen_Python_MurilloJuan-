# modules/gestion_usuarios.py

def registrar_camper(data):
    # Garantizamos que 'campers' sea una lista, incluso si no existe en 'data'
    if "campers" not in data or not isinstance(data["campers"], list):
        data["campers"] = []

    nuevo_camper = {}

    print("\n--- Registro de Camper ---")
    nuevo_camper["id"] = input("Ingrese el ID del camper: ")
    nuevo_camper["nombre"] = input("Ingrese el nombre del camper: ")
    nuevo_camper["edad"] = int(input("Ingrese la edad del camper: "))
    nuevo_camper["email"] = input("Ingrese el email del camper: ")
    nuevo_camper["telefono"] = input("Ingrese el teléfono del camper: ")
    nuevo_camper["ruta_asignada"] = input("Ingrese la ruta asignada: ")
    nuevo_camper["salon"] = input("Ingrese el salón asignado: ")

    # Agregar el nuevo camper a la lista
    data["campers"].append(nuevo_camper)

    print("Registro de Camper completado.")
    return data

def registrar_trainer(data):
    # Aseguramos que 'trainers' sea una lista
    if "trainers" not in data or not isinstance(data["trainers"], list):
        data["trainers"] = []

    nuevo_trainer = {}

    print("\n--- Registro de Trainer ---")
    nuevo_trainer["id"] = input("Ingrese el ID del trainer: ")
    nuevo_trainer["nombre"] = input("Ingrese el nombre del trainer: ")
    nuevo_trainer["email"] = input("Ingrese el email del trainer: ")
    nuevo_trainer["telefono"] = input("Ingrese el teléfono del trainer: ")
    nuevo_trainer["ruta_asignada"] = input("Ingrese la ruta asignada del trainer: ")
    nuevo_trainer["horario_asignado"] = input("Ingrese el horario asignado: ")

    # Agregar el nuevo trainer a la lista
    data["trainers"].append(nuevo_trainer)

    print("Registro de Trainer completado.")
    return data
