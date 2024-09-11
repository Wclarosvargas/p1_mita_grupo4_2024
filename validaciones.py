import re


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


#Validaciones de la matriz clase

def validar_id_unico_clase(matriz,id):
    '''
    Verifica si el Id de la clase ya existe
    '''
    for clase in matriz:
        if clase[0] == id:
            return 0 #ID ya existe
    return 1 # Id es único


def validar_horario(horario):
    """
    Verifica si el horario está en el formato 'HH:MM-HH:MM'.
    """
    horario_range = r"^([01]\d|2[0-3]):([0-5]\d)-([01]\d|2[0-3]):([0-5]\d)$"
    if re.match(horario_range, horario):
        return 1
    return 0

def validar_id_profesor(matriz,id):
    '''
    Verifica si el id del profesor existe
    '''
    for profe in matriz:
        if profe[0] == id:
            return 1
    return 0

def validar_fecha(fecha):
    """
    Verifica si la fecha está en el formato 'YYYY-MM-DD' mediante el uso de expresiones regulares.
    """
    # Expresión regular para verificar el formato de fecha
    patron = r'^\d{2}-\d{2}-\d{4}$'
    if re.match(patron, fecha):
        # La fecha se encuentra en el formato correcto
        return 1
    else:
        # La fecha no se encuentra en el formato correcto
        return 0
    

#funciones abocados a validaciones para la matriz asistencias

def validar_id_unico_asistencia(matriz,id):
    '''
    Verifica si el ID  de asistencia no se encuentra repetido
    '''
    for asistencia in matriz:
        if asistencia[0] == id:
            return 0 # ID ya existe 
        return 1 # ID único
    