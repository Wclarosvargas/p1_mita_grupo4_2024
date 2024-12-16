from validaciones import validar_id_unico, validar_horario, validar_fecha, validar_id_profesor

# Matríz de profesores
profesores = [
    [10, 'Carlos', 'Pérez'],
    [14, 'Juan', 'Nardone'],
    [16, 'Luis', 'Martínez'],
    [18, 'María', 'Lopez'],
    [20, 'Ezequiel', 'Escalante'],
    [22, 'Laura', 'Gómez'],
    [40, 'Miguel', 'Rodríguez'],
    [42, 'Sofía', 'Fernández'],
    [80, 'Jorge', 'Sánchez'],
    [82, 'Maximiliano', 'Guzman'],
    [90, 'Sergio', 'Aguilar'],
    [92, 'Mariano', 'Eito']
]

#transformo la matríz profesores a conjuntos de ids
conjunto_profesores = {profesor[0] for profesor in profesores}

#-----------------------------------------------------------------------------------------------------------
def cargar_cursos(archivo, modo):
    matriz_cursos = []
    try:
        with open(archivo,modo, encoding='UTF-8') as file:
            while True:
                linea = file.readline()
                if not linea :
                    break
                curso = linea.strip().split(',')
                matriz_cursos.append([int(curso[0]), int(curso[1]), curso[2], curso[3], curso[4]])
    except FileNotFoundError:
        print('Archivo de cursos no fue encontrado.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    return matriz_cursos

#---------------------------------------------------------------------------------------------------------
def guardar_cursos(matriz_cursos, archivo,modo):
    #Toma los valores de la matriz
    try:
        with open(archivo,modo, encoding='UTF-8') as file:
            for curso in matriz_cursos:
                linea = ','.join(map(str,curso))
                file.write(linea + '\n')
    except Exception as e:
        print(f'Ocurrió un error al guardar los cursos: {e}')

#-------------------------------------------------------------------------------------------------------

def crear_curso(matriz):
    '''
    Permite al usuario ingresar y validar los datos de una nueva clase para agregarla a la matriz.
    Solicita un ID único, el ID del profesor, el horario y la fecha, asegurando de que sean válidos.
    Si todos los datos son correctos, se añade la nueva clase a la matriz y se muestra un mensaje de éxito.
    '''
    try:
        #asignación de ID
        if not matriz:
            id = 1 
        else:
            id = max([curso[0] for curso in matriz]) +1
        print(f"El ID asignado al curso es: {id}")

        #ID profesor
        bandera=False
        while bandera==False:
            print("Ingrese el ID del profesor:")
            id_profesor = int(input())

            if validar_id_profesor(conjunto_profesores,id_profesor):
                print("Profesor Encontrado!")
                bandera=True                   
            else:
                print("ID del profesor no válido. Por favor, ingrese un ID de profesor válido. ")

        #Seguimos con el nombre..
        print("Ingrese Nombre de la materia del curso:")
        materia = input()
        
        #Horario
        horario_valido = 0
        while horario_valido == 0:
            print("Ingrese el horario de la clase (sirva de ejemplo: '09:00-10:00'):")
            horario = input()
            if validar_horario(horario) == 1:
                horario_valido = 1
            else:
                print("Horario inválido.Por favor, ingrese un horario válido.")   

        #Fecha
        fecha_valida = 0
        while fecha_valida == 0:
            print("Ingrese la fecha de la clase (por ejemplo, '10-09-2024'):")
            fecha = input()
            if validar_fecha(fecha) == 1:
                fecha_valida = 1
            else:
                print("Fecha inválida. Por favor, ingresar una fecha con formato 'DD-MM-YYYY'.")

        #Alta nueva curso con nombre de materia primera letra en mayuscula.
        nuevo_curso = [id,id_profesor,materia.capitalize(),fecha,horario]
        print("Clase agregada con éxito!.")
        matriz.append(nuevo_curso)
        #Agregamos ese registro a la matriz_curso

    except ValueError as error:#Excepcion cuando se espera un valor numerico
        raise ValueError(f"Se esperaba un valor Numerico. Detalles:{error}")
    
    except Exception: #Excepcion general
        raise Exception(f"Error inesperado al crear curso")
    #Relanzamos con Raise ambos casos hacia módulo menú

#------------------------------------------------------------------------------------------------------------------------------------

def mostrar_curso(archivo,modo):
    try:
        mostrar = open(archivo,modo, encoding='UTF-8')
    except OSError:
        print('No se pudo leer el archivo cursos.txt')
    else:

        print("\nLista de Profesores:")
        # Impresión de encabezados
        print(f"| {'ID':<5} | {'Nombre':<12} | {'Apellido':<15} |")
        print("-"*40)  #linea que se repite 40 veces

        # Impresión de las filas profesores
        for profesor in profesores:
            print(f" {profesor[0]:<5} | {profesor[1]:<12} | {profesor[2]:<15}")
        print("~"*40)          
        # Impresión de encabezados
        print("Listado de Cursos")
        print(f"{'| ID':<7}{'| ID_profesor':<15}{'| Materia':<18}{'| Fecha':<18}{'| Horario':<18}|")
        print("-" * 70)

        linea = mostrar.readline()  # Primera línea del archivo
        while linea != '':
            curso = linea.strip().split(',')  # Elimina espacios y divide por comas para crear una lista `curso`
            if len(curso) == 5:  # Omite líneas incompletas
                id = int(curso[0])
                id_profesor = int(curso[1])
                materia = curso[2][:15]
                fecha = curso[3][:10]
                horario = curso[4][:15]
                # Impresión alineada de cada registro
                print(f"| {id:<5} | {id_profesor:<12} | {materia:<15} | {fecha:<15} | {horario:<15}")
            linea = mostrar.readline()  # Lee la siguiente línea
        print("-"*65)

        
    finally:
        mostrar.close()

#---------------------------------------------------------------------------------------------------------------------------------
def actualizar_curso(matriz):
    '''
    Actualiza los datos de la matríz curso mediante el ingreso de los datos
    Se espera que sean modificados id_curso, id_profesor, fecha y horario
    Busca el curso por su ID y, si lo encuentra solicita y valida los nuevos datos previo a actualizarlos.
    '''
    try:
        renovar = False
        while renovar == False:
            print('Ingrese el ID del curso que desea actualizar:')
            id_renovado = int(input())
            if validar_id_unico(matriz,id_renovado):
                print("Curso Encontrado!")
                renovar=True
            else:
                print("Id de curso inexistente")
                print("Intente nuevamente..")
                
        #ingreso de nuevo ID profesor y validación
        flag = False
        while flag == False:
            print('Ingrese el nuevo ID del profesor:')
            id_profesor = int(input())

            if validar_id_profesor(conjunto_profesores,id_profesor):
                flag = True
                print("Profesor encontrado!")
            else:
                print('ID del profesor no válido. Por favor, ingrese un ID de profesor válido')

        #Nueva materia asignada
        print("Ingrese Nombre de la materia del curso:")
        materia = input()

        #Ingreso de nueva fecha y validacion
        fecha = False
        while fecha == False:
            print('Ingrese la nueva fecha, formato(DD-MM-YYYY).')
            nueva_fecha = input()

            #Valida la fecha ingresada
            if validar_fecha(nueva_fecha):
                fecha = True
            else:
                print('Fecha inválida. Por favor ingrese una nueva fecha con formato (DD-MM-YYYY).')

        #Ingreso de nueva fecha y validacion
        hora = False
        while hora == False:
            print('Ingrese el nuevo horario,(formato HH:MM-HH:MM)')
            nuevo_horario = input().strip()
            #Validar horario
            if validar_horario(nuevo_horario):
                hora = True
            else:
                print('Horario inválido. Por favor ingrese un horario válido en formato (HH:MM-HH:MM).')


        # recorremos la fila a actualizar para despues cambiar los datos 
        for curso in matriz:
                if curso[0] == id_renovado:
                    curso[0],curso[1],curso[2],curso[3],curso[4]= [id_renovado,id_profesor,materia,nueva_fecha,nuevo_horario]
        print("Actualizando cambios en el registro..")
        print('Actualizacion Exitosa!')
        return matriz

    except ValueError as error:#Excepcion cuando se espera un valor numerico
        raise ValueError(f"Se esperaba un valor Numerico, detalles:{error}")
    except Exception: #Excepcion general
        raise Exception(f"Error inesperado al actualizar curso") 
    #Relanzamos con Raise ambos casos hacia modulo menú


#---------------------------------------------------------------------------------------------------------------------------------

def eliminar_curso(matriz):
    try:
        eliminar =False
        while eliminar == False:
            print('Ingrese el ID del Curso que desea eliminar:')
            id_eliminar = int(input().strip())

            for curso in range(len(matriz)):
                if matriz[curso][0] == id_eliminar:
                    matriz.pop(curso)
                    print('El curso fue eliminado con éxito.')
                    eliminar = True
                    return matriz
            print('El curso no fue encontrado. Intente nuevamente.')
            
    except ValueError as err:
        raise ValueError(f"Se esperaba un valor Numerico, detalles:{err}")
    except Exception:
        raise Exception(f"Error inesperado al eliminar curso")
    #Relanzamos ambas excepciones con raise hacia modulo menu