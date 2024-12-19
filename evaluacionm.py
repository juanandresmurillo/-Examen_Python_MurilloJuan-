def registrar_notas(datos, id_camper, id_ruta, nota_teorica, nota_practica, nota_quiz):
    # Buscar el camper
    camper = next((c for c in datos["campers"] if c["id"] == id_camper), None)
    if not camper:
        print("El ID del camper no existe.")
        return datos

    # Buscar la ruta
    ruta = next((r for r in datos["rutas"] if r["id"] == id_ruta), None)
    if not ruta:
        print("El ID de la ruta no existe.")
        return datos

    # Calcular la nota final
    nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quiz * 0.1)
    print(f"Nota final calculada: {nota_final:.2f}")

    # Actualizar el estado del camper
    if nota_final >= 60:
        camper["estado"] = "Cursando"
        print("¡Camper aprobado para continuar con la ruta!")
    else:
        camper["riesgo"] = True
        print("El camper no aprobó el módulo y está en riesgo.")

    # Guardar evaluación
    evaluacion = {
        "id_camper": camper["id"],
        "id_ruta": ruta["id"],
        "nota_teorica": nota_teorica,
        "nota_practica": nota_practica,
        "nota_quiz": nota_quiz,
        "nota_final": nota_final
    }
    datos["evaluaciones"].append(evaluacion)
    return datos


def evaluar_camper(datos):
    for evaluacion in datos["evaluaciones"]:
        print(f"Camper {evaluacion['id_camper']}: Nota Final: {evaluacion['nota_final']:.2f}")