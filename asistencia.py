#Falta desarrollar el CRUD de la matríz asistencias
from validaciones import validar_fecha, validar_id_unico_asistencia

asistencias = [
    [102,204,'Presente', '16-04-2024'],
    [103,405,'Ausente','25-12-2024'],
    [105,206,'Presente','21-01-2023']
]

def crear_asistencias(matriz):
    '''
    Se encargara del ingreso de datos de asistencia de cada estudiante
    Se espera que cree los datos(estado de presente/ausente)
    '''

    id_valido = 0
    while id_valido == 0:
        print("Ingrese el ID asistencia") 
        id = int(input())
        if 