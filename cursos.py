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
    [107, 'Isabel', 'Ramírez']
]

def crear_clase(matriz):
    '''
    Permite al usuario ingresar y validar los datos de una nueva clase para agregarla a la matriz.
    Solicita un ID único, el ID del profesor, el horario y la fecha, asegurando de que sean válidos.
    Si todos los datos son correctos, se añade la nueva clase a la matriz y se muestra un mesaje de éxito.
    '''

    id_valido = 0
    while id_valido == 0:
        print("Ingrese el ID de la clase:")
        id = int(input())
        if validadr_id_unico(matriz,id):
            id_valido = 1
        else:
            print("El ID de la clase ya existee, Por favor, ingrese un ID diferente.")

    print("Ingrese el ID del profesor:")
    id_profesor = int(input())         
    if validar_id_profesor(profesores,id_profesor) == 0:
        print("ID del profesor no válido. Por favor, ingrese un ID de profesor válido. ")
        return

    horario_valido = 0
    while horario_valido == 0:
        print("Ingrese el horario de la clase (por ejemplo, '09:00-10:00'):")
        horario = input()
        if validar_horario(horario) == 1:
            horario_valido = 1
        else:
            print("Horario inválido.Por favor, ingrese un horario válido.")   

    fecha_valida = 0
    while fecha_valida == 0:
        print("Ingrese la fecha de la clase (por ejemplo, '10-09-2024'):")
        fecha = input()
        if validar_fecha(fecha) == 1:
            fecha_valida = 1
        else:
            print("Fecha inválida. Por favor, ingresar una fecha con formato 'DD-MM-YYYY'.")

    nueva_clase = [id,id_profesor,fecha,horario]
    print("Clase agregada con éxito.")
    matriz.append(nueva_clase)

#------------------------------------------------------------------------------------------------------------------------------------
def mostrar_curso(matriz):
    '''
    Pos: está funcion se encargara de mostrar la matriz de cursos en formato tabular.
    Imprime los encabezados y los datos de cada curso, incluyendo ID, ID del profesor, fecha y horario.
    '''
    # Crea una lista 'curso' con ID del curso, ID del profesor,
    # y fechas y horarios truncados a 13 caracteres de 'matriz'.
    curso = [[id,id_profesor,fecha[:13],horario[:13]] for id,id_profesor,fecha,horario in matriz]

    #Impresión de encabezados
    print(f"| {'ID':<5} | {'ID_profesor':<5} | {'Fecha':>13} | {'Horario':>20} |")  
    print("-"*55)          

    #Impresión de filas de datos
    for i in curso:
        print(f"| {i[0]:<5} | {i[1]:>8} | {i[2]:>17} | {i[3]:>20} |")


#---------------------------------------------------------------------------------------------------------------------------------
def actualizar_curso(matriz):
    '''
    Actualiza los datos de la matríz curso mediante el ingreso de los datos
    Se espera que sean modificados id_curso, id_profesor, fecha y horario
    Busca el curso por su ID y, si lo encuentra solicita y valida los nuevos datos previo a actualizarlos.
    '''
    renovar = 0
    while renovar == 0:
        print('Ingrese el ID del curso que desea actualizar:')
        id_renovar = int(input().strip())

        #Busqueda del curso por medio de su ID
        for curso in matriz:
            if curso[0] == id_renovar:
                print('Curso encontrado')

                #Solicita el nuevo ID del profesor
                flag = 0
                while flag == 0:
                    print('Ingrese el nuevo ID del profesor:')
                    id_profesor = int(input())

                    if validar_id_profesor(profesores,id_profesor) == 1:
                        flag = 1
                    else:
                        print('ID del profesor no válido. Por favor, ingrese un ID de profesor válido')
                
                #Solicita nueva fecha
                hora = 0
                while hora == 0:
                    print('Ingrese el nuevo horario,(formato HH:MM-HH:MM)')
                    horario = input().strip()

                    #Validar horario
                    if validar_horario(horario) == 1:
                        hora = 1
                    else:
                        print('Horario inválido. Por favor ingrese un horario válido en formato (HH:MM-HH:MM).')

                #Solicita nueva fecha
                fecha = 0
                while fecha == 0:
                    print('Ingrese la nueva fecha, formato(DD-MM-YYYY).')
                    nueva_fecha = input()

                    #Valida la fecha ingresada
                    if validar_fecha(nueva_fecha) == 1:
                        fecha = 1
                    else:
                        print('Fecha inválida. Por favor ingrese una nueva fecha con formato (DD-MM-YYYY).')


                #Actualización de datos
                curso[1] = id_profesor #Actualiza id_profesor
                curso[2] = nueva_fecha #Actualiza la fecha
                curso[3] = horario     #Actualiza el horario
                print('Los elementos del curso fueron actualizados exitosamente.')
                renovar = 1
                return matriz
        
        print('Curso no fue encontrado. Intente nuevamente.')

#---------------------------------------------------------------------------------------------------------------------------------

def eliminar_curso(matriz):
    eliminar = 0
    while eliminar == 0:
        print('Ingrese el ID del estudiante que desea eliminar:')
        id_eliminar = int(input().strip())

        for curso in range(len(matriz)):
            if matriz[curso][0] == id_eliminar:
                matriz.pop(curso)
                print('El curso fue eliminado con éxito.')
                eliminar = 1
                return matriz
        print('El curso no fue encontrad. Intente nuevamente.')