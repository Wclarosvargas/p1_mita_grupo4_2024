from estudiantes import crear,mostrar_matriz,actualizar,eliminar

estudiante = [
    [101,"weimar","claros",8.5],
    [105,"juana","pantilla",6.8],
    [102,"juana","pantilla",6.8]
]


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


def mostrar_menu():
    '''
    Muestra el menú de opciones del CRUD.
    '''
    print('Seleccionar una opción, (1)Crear,(2)Leer, (3)Actualizar,(4)Eliminar,(5)Salir')

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

    flag = 0

    while flag  == 0:
        estudiante_capitalizado = conversion(estudiante)
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

