import re
#Nota:
#Cambiar la forma de los return 1,0 por while y usando conjuntos.
def validadr_id_unico(matriz,identificador):
    """
    Verifica si el ID ya existe en la matriz.
    """
    
    for item in matriz:
        if item[0] == identificador:
            return 0 # ID ya existe
    return 1 #ID es único

def validar_id_estudiantes(dic_Estudiante,id_estudiante):
    for estudiante in dic_Estudiante:
        if estudiante['id'] == id_estudiante:
            print("El ID ya existe.")
            return 0
    if id_estudiante>0:
        return 1
    else:
        print("ID fuera de rango..")
        return 0
    
def validar_promedio(promedio):
    """
    Verifica si el promedio está entre 1 y 10
    Devuelve 1 si el promedio es válido, 0 si no lo es.
    """
    return 1 if 1 <= promedio <= 10 else 0


def validar_horario(horario):
    """
    Verifica si el horario está en el formato 'HH:MM-HH:MM'.
    """
    horario_range = r'^([0-1][0-9]|2[0-3]):([0-5][0-9])-([0-1][0-9]|2[0-3]):([0-5][0-9])$'
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
    Verifica si la fecha está en el formato 'DD-MM-YYYY' mediante el uso de expresiones regulares.
    """
    # Expresión regular para verificar el formato de fecha
    patron = r'^([012][0-9]|3[0-1])-(0[1-9]|1[0-2])-\d{4}$'
    if re.match(patron, fecha):
        # La fecha se encuentra en el formato correcto
        return 1
    else:
        # La fecha no se encuentra en el formato correcto
        return 0
    
def validar_id_curso(matriz_curso,id_curso):
    '''
    Verifica si el ID del curso existe en la matriz de cursos.
    '''
    for curso in matriz_curso:
        if curso[1] == id_curso:
            return 0
    return 1

def validar_id_estudiante(matriz_estudiante, id_estudiante):
    '''
    Verifica si el ID del estudiante existe en la matriz de estudiantes.
    '''
    for estudiante in matriz_estudiante:
        if estudiante[2] == id_estudiante:
            return 0
    return 1

def validar_estado(estado):
    '''
    Valida que el estado del estudiante sea 'Presente' o 'Ausente'.
    '''
    return estado in {'presente', 'ausente'}

