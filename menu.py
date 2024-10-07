import os
from estudiantes import crearEstudiante, mostrarEstudiante, actualizarEstudiante, eliminarEstudiante
from cursos import crear_clase, mostrar_curso, actualizar_curso, eliminar_curso
from asistencia import crear_asistencias, mostrar_asistencia, actualizar_asistencia, eliminar_asistencia

#Uso de lista de Diccionarios en ESTUDIANTE
dic_Estudiante = [
    {'id':1,'nombre':'Juan','apellido':'Gomez','promedio':8.4},
    {'id':2,'nombre':'Ana','apellido':'Perez','promedio':5.4},
    {'id':3,'nombre':'Luis','apellido':'hernandez','promedio':6.4},
    {'id':4,'nombre':'Martin','apellido':'Mejia','promedio':3.4},
    {'id':5,'nombre':'Jose','apellido':'Berrios','promedio':4.5},
    {'id':6,'nombre':'Matias','apellido':'Escalera','promedio':4.5}
    ]


matriz_cursos = [
    [101, 14, '15-09-2025', '10:30-14:40'],
    [102, 25, '16-04-2022', '08:20-12:40'],
    [103, 36, '14-01-2024', '14:30-18:00'],
    [104, 62, '25-10-2024','18:30-22:00'],
    [105, 96, '28-07-2024', '14:30-18:40']
]

matriz_asistencias = [
    [201, 101, 1, 'presente', '16-04-2024'],
    [202,102, 2,'ausente', '15-04-2024'],
    [203,104,5,'presente', '25-11-2024'],
    [204,105,3,'ausente', '15-06-2024'],
    [205,104,4,'ausente', '02-08-2023']
]
def clear_screen(): #Funcion de la libreria os,para limpiar la pantalla de los Menús.
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    '''
    Muestra el menú principal del programa.
    '''
    print("--------------------------------------- ")
    print("\nMenú Principal")
    print("1. Gestión de estudiantes")
    print("2. Gestión de Cursos")
    print("3. Gestión de asistencias")
    print("4. Salir del programa")
    print("--------------------------------------- ")

#------------------------------------------------------------------------------------------------
def menu_estudiantes():
    '''
    Gestiona el menú de operaciones de la matriz estudiantes.
    '''
    #EXEPCIONES EN ESTUDIANTES  
    try:
        #clear_screen()
        flag_estudiantes = 0
        while flag_estudiantes == 0:
            print("\nMenú de Gestión de estudiantes")
            print("1. Agregar Estudiante")
            print("2. Mostrar estudiante")
            print("3. Actualizar estudiante")
            print("4. Eliminar estudiante")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción:")
            try:
                if opcion == '1':
                    crearEstudiante(dic_Estudiante)
                elif opcion == '2':
                    if len(dic_Estudiante) == 0:
                        print("No hay estudiantes registrados.")
                    else:
                        mostrarEstudiante(dic_Estudiante)
                elif opcion == '3':
                    actualizarEstudiante(dic_Estudiante)
                elif opcion == '4':
                    eliminarEstudiante(dic_Estudiante)
                elif opcion == '5':
                    flag_estudiantes = 1 # flag=1 Sale del menú de estudiantes
                else:
                    print("Opción no válida. Intente de nuevo.")

            except Exception as error:
                print(f"Error al ejecutar la opción: {error}")

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except Exception as error:
        print(f"Error inesperado del menú estudiantes: {error}")

#------------------------------------------------------------------------------------------------------
def menu_cursos():
    '''
    Gestiona el menú de operaciones de la matriz cursos.
    '''
    clear_screen()
    flag_cursos = 0
    while flag_cursos == 0:
        print("\nMenú de Gestión de Cursos")
        print("1. Agregar Curso")
        print("2. Mostrar Cursos")
        print("3. Actualizar curso")
        print("4. Eliminar curso")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_clase(matriz_cursos)
        elif opcion == '2':
            if len(matriz_cursos) == 0:
                print("No hay cursos registrados.")
            else:
                mostrar_curso(matriz_cursos)
        elif opcion == '3':
            actualizar_curso(matriz_cursos)
        elif opcion == '4':
            eliminar_curso(matriz_cursos)
        elif opcion == '5':
            flag_cursos = 1 #Sale del menú de cursos
        else:
            print("Opción no válida. Intente de nuevo")


def menu_asistencia():
    '''
    Gestiona el menú de operaciones de la matríz asistencia.
    '''
    clear_screen()
    flag_asistencias = 0
    while flag_asistencias == 0:
        print("\nMenú de Gestión de asistencias")
        print("1. Registrar asistencias")
        print("2. Mostrar asistencias")
        print("3. Actualizar asistencias")
        print("4. Eliminar asistencia")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_asistencias(matriz_asistencias,matriz_cursos,dic_Estudiante)
        elif opcion == '2':
            mostrar_asistencia(matriz_asistencias)
        elif opcion == '3':
            actualizar_asistencia(matriz_asistencias, matriz_cursos, dic_Estudiante)
        elif opcion == '4':
            eliminar_asistencia(matriz_asistencias)
        elif opcion == '5':
            flag_asistencias = 1 # Sale del menú de asistencias
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    '''
    Gestiona el flujo del programa.
    '''
    flag_programa = 0
    while flag_programa == 0:
        #clear_screen() #Actualizo la pantalla
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_estudiantes()
        elif opcion == '2':
            menu_cursos()
        elif opcion == '3':
            menu_asistencia()
        elif opcion == '4':
            print("Saliendo del programa...")
            flag_programa = 1 #Sale del programa principal
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

