from validaciones import validadr_id_unico,validar_promedio

def crear(matriz):
    '''
    Agrega un nuevo estudiante a la matríz de estudiantes.
    Solicita al usuario el ID, nombre, apellido y promedio del estudiante,
    valida los datos y los añade a la matríz si son correctos
    '''

    id_valido = 0
    while id_valido ==0:
        print("Ingrese el ID del estudiante:")
        id = int(input())
        if validadr_id_unico(matriz,id):
            id_valido = 1
        else:
            print("El ID ya existe, Por favor, ingrese un ID diferente.")
    
    print("Ingrese el nombre del estudiante")
    nombre = input()
    print("Ingrese el apellido del estudiante:")
    apellido = input()

    promedio_valido = 0
    while promedio_valido == 0:
        print("Ingrese el promedio del estudiante: ")
        promedio = float(input())
        if validar_promedio(promedio):
            promedio_valido = 1
        else:
            print("El promedio debe estar entre 1 y 10. Por favor, ingrese un promedio válido")

    nombre_capitalizado = nombre.capitalize()
    apellido_capitalizado = apellido.capitalize()

    # Crear una nueva entrada
    new_student = [id, nombre_capitalizado, apellido_capitalizado, promedio]
    print("Estudiante agregado con éxito.")
    matriz.append(new_student)



#Funciones
def mostrar_matriz(matriz):
    '''
    Muestra la matríz de estudiantes en formato tabular, ordenada por promedio y ID.
    '''

    # Crea una lista 'estudiantes' con ID, nombre truncado a 10 caracteres,
    # apellido truncado a 12 caracteres y promedio de 'matriz'.
    estudiantes = [[id,nombre[:10],apellido[:12],promedio] for id,nombre,apellido,promedio in matriz]

    #Ordena la lista de estudiantes por promedio descendente y luego por ID de forma ascendente
    estudiante_ordenados = sorted(estudiantes, key=lambda x: (-x[3],x[0]))
    
    #se imprimira los encabezados
    print(f"| {'ID':<5} | {'Nombre':<10} | {'Apellido':<10} | {'Promedio':>10}")
    print("-"*55) #Línea de separación de los encabezados 

    #Impresión de filas de datos
    for estudiante in estudiante_ordenados:
        print(f"| {estudiante[0]:<5} | {estudiante[1]:<10} | {estudiante[2]:<10} | {estudiante[3]:>10.2f} |")


def actualizar(matriz):
    '''
    Actualiza los datos del estudiante existente en la matriz.
    Solicita al usuario el ID del estudiante, busca el estudiante por su ID,
    y actualiza su nombre, apellido y promedio si el estudiante existe.
    '''
    bandera = 0
    while bandera == 0:
        print("Ingrese el ID del estudiante que desea actualizar:")
        id = int(input().strip())


        #Busca el estudiante por su ID
        encontrado = 0
        for i in range(len(matriz)):
            if matriz[i][0]==id :
                print("Estudiante encontrado")       
                print("Ingrese el nuevo nombre del estudiante:")
                nombre = input()
                print("Ingrese el nuevo apellido del estudiante:")
                apellido = input()

                #Verificamos que el promedio esté entre 1 y 10
                flag=0
                while flag==0: #Verificamos que el promedio este entre 1 y 10
                    flag=1
                    print("Ingrese el nuevo promedio del estudiante: ")
                    promedio = float(input().strip())
                    if 1>promedio or promedio>10:
                        flag=0
                        print("El promedio debe estar entre 1 y 10") 
                #Capitalizar los nombre y apellidos de los nuevos datos ingresados
                nombre_capitalizado = nombre.capitalize()
                apellido_capitalizado = apellido.capitalize()

                #Actualización de los datos
                matriz[i]=[id,nombre_capitalizado,apellido_capitalizado,promedio]
                print("Los datos fueron actualizados")
                bandera = 1 
                return matriz
            
        #Mensaje si no se encuentra el estudiante
        if encontrado == 0:    
            print("Estudiante no encontrado.")


def eliminar(matriz):
    '''
    elimina al estudiante de la matriz por su ID.
    Solicita al usuario el ID del estudiante, busca al estudiante por su ID,
    y lo elimina si el estudiante existe. 
    '''
    bandera = 0
    while bandera == 0:
        print("Ingrese el ID del estudiante que desea eliminar:")
        id = int(input())
        encontrado = 0
        indices_a_eliminar = []
        #Busca el estudiante por ID
        for i in range(len(matriz)):
            if matriz[i][0] == id:
                indices_a_eliminar.append(i)
                encontrado = 1

        for indice in reversed(indices_a_eliminar):
            matriz.pop(indice) #La función pop eliminar los datos de la matriz que se encuentra en el ID ingresado

        if encontrado == 1:
            print("El estudiante fue eliminado con éxito.")
            bandera = 1
        else:
            print("Estudiante no fue encontrado")

    return matriz