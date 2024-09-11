
def validadr_id_unico(matriz,id):
    """
    Verifica si el ID del estudiante ya existe en la matriz.
    """
    
    for estudiante in matriz:
        if estudiante[0] == id:
            return 0 # ID ya existe
    return 1 #ID es único
    
def validar_promedio(promedio):
    """
    Verifica si el promedio está entre 1 y 10
    Devuelve 1 si el promedio es válido, 0 si no lo es.
    """
    return 1 if 1 <= promedio <= 10 else 0