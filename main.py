estudiante = [
    [101,"weimar","claros",8.5],
    [105,"juana","pantilla",6.8],
    [102,"juana","pantilla",6.8]
]

#Funciones
def mostrar_matriz(matriz):
    '''
    pos: mostrara la matriz 
    '''
    estudiantes = [[id,nombre[:10],apellido[:10],promedio] for id,nombre,apellido,promedio in matriz]

    #Ordena la lista de estudiantes por promedio descendente y luego por ID de forma ascendente
    estudiante_ordenados = sorted(estudiantes, key=lambda x: (-x[3],x[0]))
    
    #se imprimira los encabezados
    print(f"{'ID':<5}{'Nombre':<10}{'Apellido':<10}{'Promedio':<8}")
    print("-"*36) #Línea de separación de los encabezados 

    #Impresión de filas de datos
    for estudiante in estudiante_ordenados:
        print(f"{estudiante[0]:<5}{estudiante[1]:<10}{estudiante[2]:<10}{estudiante[3]:<8.2f}")

    

def conversion(matriz):
    '''
    convertira el primer caracter de nombre y apellido en mayuscula
    '''
    for i in range(len(matriz)):
        id,nombre,apellido,promedio = matriz[i]
        nombre_capitalizado = nombre.capitalize()
        apellido_capitalizado = apellido.capitalize()
        matriz[i] = [id,nombre_capitalizado,apellido_capitalizado,promedio]
    return matriz

def crear(matriz):
    '''
    Se encargar de ingreso de los datos del alumno
    Se espera que cree los datos del estudiante
    '''
    print("Ingrese el ID del estudiante: ")
    id = int(input())
    print("Ingrese el nombre del estudiante:")
    nombre = input()
    print("Ingrese el apellido del estudiante: ")
    apellido = input()
    print("Ingrese el promedio del estudiante: ")
    promedio = float(input())
        
    nombre_capitalizado = nombre.capitalize()
    apellido_capitalizado = apellido.capitalize()

    #Crea una nueva entrada
    nuevo_estudiante = [id,nombre_capitalizado,apellido_capitalizado,promedio]
    print("Estudiante agregado con éxito.")
    matriz.append(nuevo_estudiante)

def mostrar_menu():
    '''
    Muestra el menú de opciones del CRUD.
    '''
    print('Seleccionar una opción, (1)Crear,(2)Leer, (3)Actualizar,(4)Eliminar,(5)Salir')

def actualizar(matriz):
    '''
    Actualiza los datos del estudiante mediante el ingreso de los datos
    '''
    print("Ingrese el ID del estudiante que desea actualizar:")
    id = int(input())

    #Busca el estudiante por su ID
    for i in range(len(matriz)):
        if matriz[i][0]==id :
            print("Estudiante encontrado")
            print("Ingrese el nuevo nombre del estudiante:")
            nombre = input()
            print("Ingrese el nuevo apellido del estudiante:")
            apellido = input()
            print("Ingrese el nuevo promedio del estudiante:")
            promedio = float(input())

            #Capitalizar los nombre y apellidos de los nuevos datos ingresados
            nombre_capitalizado = nombre.capitalize()
            apellido_capitalizado = apellido.capitalize()

            #Actualización de los datos
            matriz[i]=[id,nombre_capitalizado,apellido_capitalizado,promedio]
            print("Los datos fueron actualizados")
            return matriz
    print("Estudiante no encontrado.")
    return matriz

def eliminar(matriz):
    '''
    eliminara un estudiante especifico 
    '''
    print("Ingrese el ID del estudiante que desea eliminar:")
    id = int(input())

    #Busca el estudiante por ID
    for i in range(len(matriz)):
        if matriz[i][0] == id:
            matriz.pop(i) #La función pop eliminar los datos de la matriz que se encuentra en el ID ingresado
            print("Estudiante eliminado con éxito")
            return matriz
        
    print("Estudiante no fue encontrado")
    return matriz


def main():
    #Matríz estudiante, los primeros tres datos seran ingresados por defecto del programa
    estudiante = [
        [101,"weimar","claros",8.5],
        [105,"juana","pantilla",6.8],
        [102,"juana","pantilla",6.8]
    ]

    '''
    Las funciones creadas son llamadas en está función main
    Los datos son ingresados por teclado
    1 = crear, 2=mostrar, 3=actualizar, 4= eliminar, y 5 = salir 
    '''
    #Las funciones creadas son llamadas en esta función main 
    #Los datos son ing

    estudiante_capitalizado = conversion(estudiante)
    flag = 0

    while flag  == 0:
        mostrar_menu()
        accion = int(input().strip())

        if accion == 1:
            crear(estudiante_capitalizado)
            estudiante_capitalizado = conversion(estudiante_capitalizado) #Hace la capitalización para nuevos datos
        elif accion == 2:
            mostrar_matriz(estudiante_capitalizado)
        elif accion == 3:
            actualizar(estudiante_capitalizado)
        elif accion == 4:
            eliminar(estudiante_capitalizado)
        elif accion == 5:
            print('Saliendo del programa')
            flag = 1
        else:
            print('Opción no válida, por favor ingrese nuevamente el dígito: ')        

main() #Hace el llamdo de la función main, donde se ejecuta todo el programa