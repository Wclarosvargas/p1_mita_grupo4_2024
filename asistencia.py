#Falta desarrollar el CRUD de la matríz asistencias
from validaciones import validar_fecha, validadr_id_unico, validar_id_estudiantes, validar_id_curso, validar_estado

#-----------------------------------------------------------------------------------------------------------------------------------
def cargar_matriz_asistencias(archivo,modo):
    matriz_asistencias = []
    try:
        with open(archivo,modo, encoding="UTF-8") as file:
            while True:
                linea = file.readline()
                if not linea :
                    break
                asistencia = linea.strip().split(',')
                matriz_asistencias.append([int(asistencia[0]), int(asistencia[1]), int(asistencia[2]), asistencia[3], asistencia[4]])
    except FileNotFoundError:
        print("Archivo de asistencias no fue encontrado.")
    except Exception as e:
        print(f"Ocurrio un error :{e}")
    return matriz_asistencias
    

#------------------------------------------------------------------------------------------------------------------------------------
def guardar_asistencias(matriz_asistencias, archivo,modo):
    try:
        with open(archivo,modo, encoding='UTF-8') as file:
            for asistencia in matriz_asistencias:
                linea = ','.join(map(str,asistencia))
                file.write(linea + '\n')
        print('Asistencia guardado exitosamente')
    except Exception as error:
        print(f'Ocurrio un error al guardar los recursos: {error}')

#------------------------------------------------------------------------------------------------------------------------------------
def crear_asistencias(matriz_asistencia,matriz_cursos ,dic_estudiantes):
    '''
    Se encargara del ingreso de datos de asistencia de cada estudiante
    Se espera que cree los datos(estado de presente/ausente)
    '''
    try:
        id_asistencia_valido = 0
        while id_asistencia_valido == 0:
            print("Ingrese el ID de la asistencia:")
            id_asistencia = int(input())

            if validadr_id_unico(matriz_asistencia, id_asistencia) == 1:
                id_asistencia_valido = 1
            else:
                print("El ID de la asistencia ya existe. Por favor, ingrese un ID diferente.")

        id_curso_valido = 0
        while id_curso_valido == 0:
            print("Ingrese el ID del curso:")
            id_curso = int(input())
            if validar_id_curso(matriz_cursos, id_curso):
                print("Curso Encontrado!")
                id_curso_valido = 1
            else:
                print("ID del curso no existe. Por favor, ingrese un ID de curso válido.")
        

        id_estudiante_valido = 0
        while id_estudiante_valido == 0:
            print("Ingrese el ID del estudiante: ")
            id_estudiante = int(input().strip())
            if validar_id_estudiantes(dic_estudiantes, id_estudiante)==0:
                print("Estudiante encontrado!")
                id_estudiante_valido = 1
            else:
                print("El ID del estudiante no existe. Por favor, ingrese un ID de estudiante válido. ")


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

        #Alta de una nueva asistencia
        nueva_asistencia = [id_asistencia,id_curso, id_estudiante,estado,fecha]
        matriz_asistencia.append(nueva_asistencia)
        print("Registro de asistencia agregado con éxito.")
        print("Estado actual de matriz_asistencia:", matriz_asistencia)

        
    except ValueError as error:#Excepcion cuando se espera un valor numerico
        raise ValueError(f"Se esperaba un valor Numerico. Detalles:{error}")
    
    except Exception: #Excepcion general
        raise Exception(f"Error inesperado..")
    #Relanzamos con Raise ambos casos hacia modulo menú

#--------------------------------------------------------------------------------------------------------------------------------------
def mostrar_asistencia(matriz_asistencia):
    '''
    Muestra todos los registros de la matriz asistencia.
    '''                 
    try:
        print("\nVista Asistencia de Estudiantes:")
        print(f"| {'ID Asistencia':<15} | {'ID Curso':<10} | {'ID Estudiante':<15} | {'Estado':<10} | {'Fecha':<15} |")
        print("-"*65)

        for registro in matriz_asistencia:
            if len(registro) == 5:
                print(f"| {registro[0]:<15} | {registro[1]:<10} | {registro[2]:<15} | {registro[3]:<10} | {registro[4]:<15} |")
            else:
                print("Registro incompleto",registro)

    except IndexError as error:
        raise IndexError(f"Datos faltantes en la Matriz, detalles: {error}")
    except Exception :
        raise Exception("Error inesperado al mostrar asistencias")
#---------------------------------------------------------------------------------------------------------------------------------------
def actualizar_asistencia(matriz_asistencia, matriz_cursos,dic_estudiantes):
    '''
    Actualiza el estado de una entrada de asistencia existente.
    '''
    try:
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
                        if validar_id_estudiantes(dic_estudiantes, id_estudiante)==0:
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

    except ValueError as error:#Excepcion cuando se espera un valor numerico
        raise ValueError(f"Se esperaba un valor Numerico, detalles:{error}")
    except Exception: #Excepcion general
        raise Exception(f"Error inesperado.") 
    #Relanzamos con Raise ambos casos hacia modulo menú

#-------------------------------------------------------------------------------------------------------------------------------------
def eliminar_asistencia(matriz_asistencia):
    try:
        eliminar = 0
        while eliminar == 0:
            print('Ingrese el ID de Asistencia que desea eliminar:')
            id_eliminar = int(input().strip())

            for asistencia in range(len(matriz_asistencia)):
                if matriz_asistencia[asistencia][0] == id_eliminar:
                    matriz_asistencia.pop(asistencia)
                    print('El registro de asistencia fue eliminado con éxito.')
                    eliminar = 1
                    return matriz_asistencia
            print('El registro de asistencia no fue encontrado. Intente nuevamente.')
    except ValueError as err:
        raise ValueError(f"Se esperaba un valor Numerico, detalles:{err}")
    except Exception:
        raise Exception(f"Error inesperado.")
    #Relanzamos ambas excepciones con raise hacia modulo menu







