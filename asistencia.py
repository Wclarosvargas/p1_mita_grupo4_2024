#Falta desarrollar el CRUD de la matríz asistencias
from validaciones import validar_fecha, validadr_id_unico, validar_id_estudiante, validar_id_curso, validar_estado

"""
asistencias = [
    [102,204,1233,'presente','16-04-2024'],
    [103,405,1232,'ausente','25-12-2024'],
    [105,206,5234,'presente','21-01-2023']
]
"""

def crear_asistencias(matriz_asitencia, matriz_cursos, matriz_estudiantes):
    '''
    Se encargara del ingreso de datos de asistencia de cada estudiante
    Se espera que cree los datos(estado de presente/ausente)
    '''
    id_asistencia_valido = 0
    while id_asistencia_valido == 0:
        print("Ingrese el ID de la asistencia:")
        id_asistencia = int(input())
        if validadr_id_unico(matriz_asitencia, id_asistencia) == 1:
            id_asistencia_valido = 1
        else:
            print("El ID de la asistencia ya existe. Por favor, ingrese un ID diferente.")

    id_curso_valido = 0
    while id_curso_valido == 0:
        print("Ingrese el ID del curso:")
        id_curso = int(input().strip())
        if validar_id_curso(matriz_cursos, id_curso):
            id_curso_valido = 1
        else:
            print("ID del curso no válido. Por favor, ingrese un ID de curso válido.")
    

    id_estudiante_valido = 0
    while id_estudiante_valido == 0:
        print("Ingrese el ID del estudiante: ")
        id_estudiante = int(input().strip())
        if validar_id_estudiante(matriz_estudiantes, id_estudiante):
            id_estudiante_valido = 1
        else:
            print("El ID del estudiante no es válido. Por favor, ingrese un ID de estudiante válido. ")


    estado_valido = 0
    while estado_valido == 0:
        print("Ingrese el estado (presente/ausente):")
        estado = input().strip().lower()
        if validar_estado(estado):
            estado_valido = 1
        else:
            print("Estado inválido. Debe ser 'Presente' o 'Ausente'.")


    fecha_valida = 0
    while fecha_valida == 0:
        print("Ingrese la fecha (Formato DD-MM-YYYY):")
        fecha = input().strip()
        if validar_fecha(fecha):
            fecha_valida = 1
        else:
            print("Fecha inválida. Por favor, ingrese una fecha con formato 'DD-MM-YYYY'.")


    nueva_asistencia = [id_asistencia,id_curso, id_estudiante,estado,fecha]
    matriz_asitencia.append(nueva_asistencia)
    print("Registro de asistencia agregado con éxito.")



def mostrar_asistencia(matriz_asistencia):
    '''
    Muestra todos los registros de la matriz asistencia.
    '''                 

    print(f"| {'ID Asistencia':<15} | {'ID Curso':<10} | {'ID Estudiante':<15} | {'Estado':<10} | {'Fecha':<15} |")
    print("-"*65)

    for registro in matriz_asistencia:
        print(f"| {registro[0]:<15} | {registro[1]:<10} | {registro[2]:<15} | {registro[3]:<10} | {registro[4]:<15} |")


def actualizar_asistencia(matriz_asistencia, matriz_cursos,matriz_estudiantes):
    '''
    Actualiza el estado de una entrada de asistencia existente.
    '''

    bandera = 0
    while bandera == 0:

        print("Ingrese el ID de la asitencia que desea actualizar:")
        id_asistencia = int(input().strip())

        encontrado = 0
        #Busca la asistencia por su ID
        for asistencia in range(len(matriz_asistencia)):
            if matriz_asistencia[asistencia][0] == id_asistencia:
                encontrado = 1
                print("Asistencia encontrada.")
        

                id_curso_valido = 0
                while id_curso_valido == 0:
                    print("Ingrese el ID del curso:")
                    id_curso = int(input().strip())
                    if validar_id_curso(matriz_cursos,id_curso):
                        id_curso_valido = 1
                    else:
                        print("ID del curso no válido. Por favor, ingrese un ID de curso válido.")

                #Validación del ID del estudiante
                id_estudiante_valido = 0
                while id_estudiante_valido == 0:
                    print("Ingrese el ID del estudiante:")
                    id_estudiante = int(input().strip())
                    if validar_id_estudiante(matriz_estudiantes, id_estudiante):
                        id_estudiante_valido = 1
                    else:
                        print("ID del estudiante no válido. Por favor, ingrese un ID de estudiante válido.")

                #Validación del estado
                estado_valido = 0
                while estado_valido == 0:
                    print("Ingrese el estado (presente/ausente):")
                    estado = input().strip().lower()
                    if validar_estado(estado):
                        estado_valido = 1
                    else:
                        print("Estado inválido. Debe ser 'presente' o 'ausente'.")

                #Validación de la fecha
                fecha_valida = 0
                while fecha_valida == 0:
                    print("Ingrese la fecha (formato DD-MM-YYYY):")
                    fecha = input().strip()
                    if validar_fecha(fecha):
                        fecha_valida = 1
                    else:
                        print("Fecha inválida. Por favor, ingrese una fecha con formato 'DD-MM-YYYY'.")

                #Actualización de datos
                matriz_asistencia[asistencia] = [id_asistencia,id_curso,id_estudiante, estado, fecha]
                print("Los datos de la asistencia fueron actualizados exitosamente.")
                return
        
        #Mensaje si no encontró el ID
        if encontrado == 0:
            print("ID de la asistencia no encontrada. Por favor, intente nuevamente.") 



def eliminar_asistencia(matriz_asistencia):
    '''
    Elimina una entrada de asistencia existente por medio de su ID.
    '''
    bandera = 0
    while bandera == 0:
        print("Ingrese el ID de la asistencia que desea eliminar:")
        id_asistencia = int(input().strip())
        encontrado = 0
        indices_a_eliminar = []

        #Busca el estudiante por ID
        for asistencia in range(len(matriz_asistencia)):
            if matriz_asistencia[asistencia][0] == id_asistencia:
                indices_a_eliminar.append(asistencia)
                encontrado = 1
        
        if encontrado == 1:
            #Elimina los índices encontrados
            for indice in reversed(indices_a_eliminar):
                matriz_asistencia.pop(indice)

            print("La asistencia fue eliminada con éxito.")
            bandera = 1
        else:
            print("El registro de asistencia no encontrado.")
    
    return matriz_asistencia









#Pruebas

"""
def mostrar_menu():

    print('Seleccionar una opción:')
    print('(1)registrar')
    print('(2)Leer')
    print('(3)actualizar')
    print('(4)eliminar')
    print('(5)Salir')


def main():

    flag = 0
    matriz_cursos = []
    matriz_estudiantes = [] 

    while flag == 0:
        mostrar_menu()
        accion = int(input().strip())

        if accion == 1:
            crear_asistencias(asistencias,matriz_cursos,matriz_estudiantes)
        elif accion == 2:
            mostrar_asistencia(asistencias)
        elif accion == 3:
            actualizar_asistencia(asistencias,matriz_cursos,matriz_estudiantes)
        elif accion == 4:
            eliminar_asistencia(asistencias)
        elif accion == 5:
            print('Saliendo del programa.....')
            flag = 1
        else:
            print('Opción no válida. Por favor ingrese nuevamente el dígito:')


main()

"""