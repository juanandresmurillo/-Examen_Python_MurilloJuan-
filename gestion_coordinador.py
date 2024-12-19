# Funciones del Coordinador

# Función para calcular la nota final de un camper
def evaluar_camper(data, id_camper):
    campers = data.get("campers", [])
    camper = next((c for c in campers if c["id"] == id_camper), None)
    
    if camper is None:
        print(f"Camper con ID {id_camper} no encontrado.")
        return data
    
    # Obtener las notas de los componentes
    teorica = camper.get("teorica", 0)
    practica = camper.get("practica", 0)
    quizzes = camper.get("quizzes", 0)
    trabajos = camper.get("trabajos", 0)
    
    # Ponderación de las notas
    nota_final = (teorica * 0.30) + (practica * 0.60) + (quizzes * 0.10)
    camper["nota_final"] = nota_final
    
    # Determinar si el camper aprueba o no el módulo
    if nota_final >= 60:
        camper["aprobado"] = True
        print(f"Camper {camper['nombre']} ha aprobado el módulo con una nota final de {nota_final:.2f}.")
    else:
        camper["aprobado"] = False
        print(f"Camper {camper['nombre']} no ha aprobado el módulo con una nota final de {nota_final:.2f}.")
    
    return data

# Función para evaluar todos los campers periódicamente
def evaluar_campers_periodicamente(data):
    print("\n--- Evaluación periódica de los campers ---")
    
    for camper in data.get("campers", []):
        print(f"\nEvaluando al camper {camper['nombre']} (ID: {camper['id']})...")
        data = evaluar_camper(data, camper["id"])
    
    # Guardar datos después de la evaluación
    guardar_datos(data)

# Función para aprobar un camper
def aprobar_camper(data, id_camper):
    campers = data.get("campers", [])
    for camper in campers:
        if camper["id"] == id_camper:
            camper["aprobado"] = True
            print(f"Camper {id_camper} aprobado.")
            return data
    print(f"Camper {id_camper} no encontrado.")
    return data

# Función para listar todos los campers
def listar_campers(data):
    campers = data.get("campers", [])
    if campers:
        print("\n--- Lista de Campers ---")
        for camper in campers:
            print(f"ID: {camper['id']}, Nombre: {camper['nombre']}, Edad: {camper['edad']}, Email: {camper['email']}, Ruta Asignada: {camper['ruta_asignada']}")
    else:
        print("No hay campers registrados.")
    return data

# Función para asignar una nota a un camper
def asignar_notas(data, id_camper, nota):
    campers = data.get("campers", [])
    for camper in campers:
        if camper["id"] == id_camper:
            camper["nota"] = nota
            print(f"Nota asignada al camper {id_camper}.")
            return data
    print(f"Camper {id_camper} no encontrado.")
    return data

# Función para reprobar a un camper
def reprobar_camper(data, id_camper):
    campers = data.get("campers", [])
    for camper in campers:
        if camper["id"] == id_camper:
            camper["nota"] = "Reprobado"
            print(f"Camper {id_camper} ha sido reprobado.")
            return data
    print(f"Camper {id_camper} no encontrado.")
    return data

# Función para asignar una nueva ruta a un camper
def asignar_ruta(data, id_camper, nueva_ruta):
    campers = data.get("campers", [])
    for camper in campers:
        if camper["id"] == id_camper:
            camper["ruta_asignada"] = nueva_ruta
            print(f"Ruta asignada al camper {id_camper}: {nueva_ruta}")
            return data
    print(f"Camper {id_camper} no encontrado.")
    return data

# Función para asignar un salón a un camper
def asignar_salon(data, id_camper, nuevo_salon):
    campers = data.get("campers", [])
    for camper in campers:
        if camper["id"] == id_camper:
            camper["salon"] = nuevo_salon
            print(f"Salón asignado al camper {id_camper}: {nuevo_salon}")
            return data
    print(f"Camper {id_camper} no encontrado.")
    return data

# Función para asignar un trainer a un camper
def asignar_trainer(data, id_camper, id_trainer):
    campers = data.get("campers", [])
    trainers = data.get("trainers", [])
    trainer_asignado = None
    for trainer in trainers:
        if trainer["id"] == id_trainer:
            trainer_asignado = trainer
            break
    if not trainer_asignado:
        print(f"Trainer con ID {id_trainer} no encontrado.")
        return data

    for camper in campers:
        if camper["id"] == id_camper:
            camper["trainer_asignado"] = trainer_asignado["nombre"]
            print(f"Trainer {trainer_asignado['nombre']} asignado al camper {id_camper}.")
            return data
    print(f"Camper {id_camper} no encontrado.")
    return data
