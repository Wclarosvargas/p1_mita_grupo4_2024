from validaciones import validar_id_unico_clase, validar_horario, validar_id_profesor, validar_fecha

cursos = [
    [202,102,'15-09-2024','10:30-11:30'],
    [205,12,'17-07-2024', '11:40-13:20']
]

# Lista de profesores
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
    Se encargara del ingreso de datos de la clase
    '''

    id_valido = 0
    while id_valido == 0:
        print("Ingrese el ID de la clase:")
        id = int(input())
        if validar_id_unico_clase(matriz,id):
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


def mostrar_curso(matriz):
    '''
    Pos: está funcion se encargara de mostrar la matriz de cursos
    '''
    curso = [[id,id_profesor,fecha[:13],horario[:13]] for id,id_profesor,fecha,horario in matriz]

    #Impresión de encabezados
    print(f"{'ID':<5}{'ID_profesor':<5}{'Fecha':>13}{'Horario':>20}")  
    print("-"*50)          

    #Impresión de filas de datos
    for i in curso:
        print(f"{i[0]:<5}{i[1]:>8}{i[2]:>17}{i[3]:>20}")




def mostrar_menu():
    '''
    Muestra el menú de opciones del CRUD.
    '''
    print('Seleccionar una opción, (1)Crear, (2) leer, (3)Salir : ')


def main():
    

    flag = 0

    while flag  == 0:
        mostrar_menu()
        accion = int(input().strip())

        if accion == 1:
            crear_clase(cursos)
        elif accion == 2:
            mostrar_curso(cursos)
        elif accion == 3:
            print('Saliendo del programa')
            flag = 1
        else:
            print('Opción no válida, por favor ingrese nuevamente el dígito: ')  

main()