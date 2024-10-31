import re
#Nota:
#Cambiar la forma de los return 1,0 por while y usando conjuntos.
def validadr_id_unico(matriz,identificador):
    """
    Verifica si el ID ya existe en la matriz.
    """
    ids_existentes = {item[0] for item in matriz}
    return 0 if identificador in ids_existentes else 1


    

def validar_id_estudiantes(dic_Estudiante,id_estudiante):
    ids_exitentes = {estudiante['id'] for estudiante in dic_Estudiante}
    if id_estudiante in ids_exitentes:
        print('El ID ya existe.')
        return 0
    if id_estudiante > 0:
        for estudiante in dic_Estudiante:
            if estudiante['id'] == id_estudiante:
                return 0
    if id_estudiante>0:
        return 1
    else:
        print('ID fuera de rango.')
        return 0
    
def validar_promedio(promedio):
    """
    Verifica si el promedio está entre 1 y 10
    Devuelve 1 si el promedio es válido, 0 si no lo es.
    """
    return 1 if 1 <= promedio <= 10 and promedio is int else 0


def validar_horario(horario):
    """
    Verifica si el horario está en el formato 'HH:MM-HH:MM'.
    """
    horario_range = r'^([0-1][0-9]|2[0-3]):([0-5][0-9])-([0-1][0-9]|2[0-3]):([0-5][0-9])$'
    if re.match(horario_range, horario):
        return 1
    return 0

def validar_id_profesor(conjunto,id_profesor):
    '''
    Verifica si el id del profesor existe
    '''
    if id_profesor in conjunto:
        return 1
    else:
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
    ids_existentes = {curso[0] for curso in matriz_curso}
    if id_curso in ids_existentes:
        return 1
    else:
        return 0
    


def validar_estado(estado):
    '''
    Valida que el estado del estudiante sea 'Presente' o 'Ausente'.
    '''
    return estado in {'presente', 'ausente'}

