from validaciones import validadr_id_unico,validar_promedio,validar_id_estudiantes

def crear(matriz):
    '''
    Agrega un nuevo estudiante a la matríz de estudiantes.
    Solicita al usuario el ID, nombre, apellido y promedio del estudiante,
    valida los datos y los añade a la matríz si son correctos
    '''

    id_valido = 0
    while id_valido == 0:
        print("Ingrese el ID del estudiante:")
        id = int(input())
        if validar_id_estudiantes(matriz,id):
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

    new_student = {
        'id':id, 'nombre':nombre.capitalize(), 'apellido':apellido.capitalize(),'promedio':promedio
    }

    print("Estudiante fue agregado con exito")
    matriz.append(new_student)


#----------------------------------------------------------------------------------------------------------------------------------

#Funciones
def mostrar_matriz(matriz):
    '''
    Muestra la matríz de estudiantes en formato tabular, ordenada por promedio y ID.
    '''
    # Crear una lista de estudiantes con id, nombre (hasta 10 caracteres), apellido (hasta 12 caracteres) y promedio
    estudiantes = [{'id':estudiante['id'],'nombre':estudiante['nombre'][:10],'apellido':estudiante['apellido'][:12],'promedio':estudiante['promedio']} for estudiante in matriz]

    #Ordena la lista de estudiantes por promedio descendente y luego por ID de forma ascendente
    estudiante_ordenados = sorted(estudiantes, key=lambda x: (-x['promedio'],x['id']))

 

    
    #se imprimira los encabezados
    print(f"| {'ID':<5} | {'Nombre':<10} | {'Apellido':<10} | {'Promedio':<10}")
    print("-"*55) #Línea de separación de los encabezados 
    
    salidas = [f'| {estudiante['id']:<5} | {estudiante['nombre']:<10} | {estudiante['apellido']:<10} | {estudiante['promedio']:<10.2f} |' for estudiante in estudiante_ordenados]

    for salida in salidas:
        print(salida)

   

#------------------------------------------------------------------------------------------------------------------------------------
     
def actualizar(matriz):
    '''
    Actualiza los datos del estudiante existente en la matriz.
    Solicita al usuario el ID del estudiante, busca el estudiante por su ID,
    y actualiza su nombre, apellido y promedio si el estudiante existe.
    '''
    renovar = 0
    while renovar == 0:
        print('Ingrese el ID del estudiante que desea actualizar.')
        id_renovar = int(input().strip())

        #Busqueda del estudiante por medio de su ID
        for estudiante in matriz: 
            if estudiante['id'] == id_renovar:
                renovar = 1
                print('Estudiante encontrado')

                #Actualizar nombre
                print('Ingrese el nuevo nombre del estudiante:')
                estudiante['nombre'] = input().capitalize()
                print('Ingrese el nuevo apellido del estudiante:')
                estudiante['apellido'] = input().capitalize()

                #verifica que el promedio esté entre 1 y 10
                promedio_valido = 0
                while promedio_valido == 0:
                    print('Ingrese el promedio del estudiante:')
                    promedio = float(input())
                    if validar_promedio(promedio):
                        promedio_valido = 1
                    else:
                        print('El promedio debe estar entre 1 y 10. Por favor, ingresar un promedio válido.')


                estudiante['promedio'] = promedio
                print('Los datos fueron actualizados')
                return matriz
        
        print('Estudiante no fue encontrado. Intente nuevamente.')
            

#---------------------------------------------------------------------------------------------------------------------------------        
def eliminar(matriz):
    eliminar = 0
    while eliminar == 0:
        print('Ingrese el ID del estudiante que desea eliminar:')
        id_eliminar = int(input().strip())

        for i in range(len(matriz)):
            if matriz[i]['id'] == id_eliminar:
                matriz.pop(i)
                print('El estudiante fue eliminado con exito.')
                eliminar = 1
                return matriz
        print('Estudiante no fue encontrado. Intente nuevamente.')