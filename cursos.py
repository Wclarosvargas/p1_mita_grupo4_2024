from validaciones import validadr_id_unico, validar_horario, validar_fecha, validar_id_profesor

# Matríz de profesores
profesores = [
    [14, 'Carlos', 'Pérez'],
    [25, 'Ana', 'García'],
    [36, 'Luis', 'Martínez'],
    [43, 'María', 'Lopez'],
    [56, 'José', 'Hernández'],
    [62, 'Laura', 'Gómez'],
    [79, 'Miguel', 'Rodríguez'],
    [80, 'Sofía', 'Fernández'],
    [96, 'Jorge', 'Sánchez'],
    [107, 'Mariano', 'Eito']
]

#transformo la matríz profesores a conjuntos de ids
conjunto_profesores = {profesor[0] for profesor in profesores}

#---------------------------------------------------------------------------------------------------------------------------
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
        print(f'Ocurrio un error: {e}')
    return matriz_cursos

def guardar_cursos(matriz_cursos, archivo,modo):
    #Toma los valores de la matriz
    try:
        with open(archivo,modo, encoding='UTF-8') as file:
            for curso in matriz_cursos:
                linea = ','.join(map(str,curso))
                file.write(linea + '\n')
        print('Cursos guardado exitosamente.')
    except Exception as e:
        print(f'Ocurrió un error al guardar los cursos: {e}')

#---------------------------------------------------------------------------------------------------------------------
def crear_clase(matriz):
    '''
    Permite al usuario ingresar y validar los datos de una nueva clase para agregarla a la matriz.
    Solicita un ID único, el ID del profesor, el horario y la fecha, asegurando de que sean válidos.
    Si todos los datos son correctos, se añade la nueva clase a la matriz y se muestra un mesaje de éxito.
    '''
    try:
        id_valido = False
        while id_valido == False:
            print("Ingrese el ID de la clase:")
            id = int(input())
            if validadr_id_unico(matriz,id):
                print("Ingrese el ID del profesor:")
                id_profesor = int(input())

                if validar_id_profesor(conjunto_profesores,id_profesor) != False:
                    print("Profesor Encontrado!")
                    id_valido=True                   
                else:
                    print("ID del profesor no válido. Por favor, ingrese un ID de profesor válido. ")
            else:
                print("El ID de la clase ya existee, Por favor, ingrese un ID diferente.")


            
        print("Ingrese Nombre de la materia del curso:")
        materia = input()
        
        horario_valido = False
        while horario_valido == False:
            print("Ingrese el horario de la clase (por ejemplo, '09:00-10:00'):")
            horario = input()
            if validar_horario(horario) == True:
                horario_valido = True
            else:
                print("Horario inválido.Por favor, ingrese un horario válido.")   

        fecha_valida = False
        while fecha_valida == False:
            print("Ingrese la fecha de la clase (por ejemplo, '10-09-2024'):")
            fecha = input()
            if validar_fecha(fecha) == True:
                fecha_valida = True
            else:
                print("Fecha inválida. Por favor, ingresar una fecha con formato 'DD-MM-YYYY'.")

        #Alta nueva curso
        nuevo_curso = [id,id_profesor,materia.capitalize(),fecha,horario]
        print("Clase agregada con éxito.")
        matriz.append(nuevo_curso)
        
        #Archivo en proceso
        """
        archivo=open("cursos.txt",mode="w")
        archivo.write(id,id_profesor,materia.capitalize(),fecha,horario)
        archivo.close()
        """
    except ValueError as error:#Excepcion cuando se espera un valor numerico
        print(f"Se esperaba un valor Numerico. Detalles:{error}")
    
    except Exception: #Excepcion general
        print(f"Error inesperado..")
    #Relanzamos con Raise ambos casos hacia modulo menú

#------------------------------------------------------------------------------------------------------------------------------------

def mostrar_curso(archivo,modo):
    try:
        # Crea una lista 'curso' con ID del curso, ID del profesor,materia
        # y fechas y horarios truncados a 13 caracteres de 'matriz'.
        #curso = [[id,id_profesor,materia[:13],fecha[:13],horario[:13]] for id,id_profesor,materia,fecha,horario in matriz]
        #print("\nVista de Cursos:")
        #Impresión de encabezados
        #print(f"| {'ID':<5} | {'ID_profesor':<12} | {'Materia':<15} | {'Fecha':<15} | {'Horario':<15} |")  
        #print("-"*65)          
        
        #Uso de archivos en proceso
        """
        archivo=open("cursos.txt","r",encoding="UTF-8")
        for linea in archivo:
            id,id_profesor,materia,fecha,horario=linea
            print(f"| {linea[0]:<5} | {linea[1]:<12} | {linea[2]:<15} | {linea[3]:<15} | {linea[4]:<15} |")
        #curso = [[id,id_profesor,materia[:13],fecha[:13],horario[:13]] for id,id_profesor,materia,fecha,horario in archivo]
        archivo.close()
        """

        #Impresión de filas de datos
        #for i in curso:
         #   print(f"| {i[0]:<5} | {i[1]:<12} | {i[2]:<15} | {i[3]:<15} | {i[4]:<15} |")

        print("\nVista de Profesores:")
        mostrar = open(archivo,modo, encoding='UTF-8')
    except OSError:
        print('No se pudo leer el archivo cursos.txt')
    else:
        print('Listado de empleados')
        print(f"{'ID':<5}{'ID_profesor':<12}{'Materia':<15}{'Fecha':<15}{'Horario':<15}")  
        linea = mostrar.readline()
        while linea != '':
            curso = linea.strip().split(',')
            if len(curso) == 5:
                id = int(curso[0])
                id_profesor = int(curso[1])
                materia = curso[2][:15]
                fecha = curso[3][:10]
                horario = curso[4][:15]
                print(f'{id:<5}{id_profesor:<12}{materia:<15}{fecha:<15}{horario:<15}')
            linea = mostrar.readline()
        print("\nLista de Profesores:")

        # Impresión de encabezados
        print(f"| {'ID':<5} | {'Nombre':<12} | {'Apellido':<15} |")
        print("-"*40)  #linea que se repite 40 veces

        # Impresión de las filas profesores
        for profesor in profesores:
            print(f"| {profesor[0]:<5} | {profesor[1]:<12} | {profesor[2]:<15} |")
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
            id_renovar = int(input().strip())

            #Busqueda del curso por medio de su ID
            for curso in matriz:
                if curso[0] == id_renovar:
                    print('Curso encontrado')

                    #Solicita el nuevo ID del profesor
                    flag = False
                    while flag == False:
                        print('Ingrese el nuevo ID del profesor:')
                        id_profesor = int(input())

                        if validar_id_profesor(conjunto_profesores,id_profesor) == True:
                            flag = True
                        else:
                            print('ID del profesor no válido. Por favor, ingrese un ID de profesor válido')

                        #Nueva materia asignada
                        print("Ingrese Nombre de la materia del curso:")
                        materia = input()
            
                    #Solicita nueva fecha
                    hora = False
                    while hora == False:
                        print('Ingrese el nuevo horario,(formato HH:MM-HH:MM)')
                        horario = input().strip()

                        #Validar horario
                        if validar_horario(horario) == True:
                            hora = True
                        else:
                            print('Horario inválido. Por favor ingrese un horario válido en formato (HH:MM-HH:MM).')

                    #Solicita nueva fecha
                    fecha = False
                    while fecha == False:
                        print('Ingrese la nueva fecha, formato(DD-MM-YYYY).')
                        nueva_fecha = input()

                        #Valida la fecha ingresada
                        if validar_fecha(nueva_fecha) == True:
                            fecha = True
                        else:
                            print('Fecha inválida. Por favor ingrese una nueva fecha con formato (DD-MM-YYYY).')


                    #Actualización de datos
                    curso[1] = id_profesor #Actualiza id_profesor
                    curso[2] = materia
                    curso[3] = nueva_fecha #Actualiza la fecha
                    curso[4] = horario     #Actualiza el horario
                    print('Los elementos del curso fueron actualizados exitosamente.')
                    renovar = True
                    return matriz
            
            print('Curso no fue encontrado. Intente nuevamente.')

    except ValueError as error:#Excepcion cuando se espera un valor numerico
        print(f"Se esperaba un valor Numerico, detalles:{error}")
    except Exception: #Excepcion general
        print(f"Error inesperado.") 
    #Relanzamos con Raise ambos casos hacia modulo menú


#---------------------------------------------------------------------------------------------------------------------------------

def eliminar_curso(matriz):
    try:
        eliminar = False
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
        print(f"Se esperaba un valor Numerico, detalles:{err}")
    except Exception:
        print(f"Error inesperado.")
    #Relanzamos ambas excepciones con raise hacia modulo menu