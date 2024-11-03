import os
from estudiantes import crearEstudiante, mostrarEstudiante, actualizarEstudiante, eliminarEstudiante, cargar_arch_Estudiantes,guardar_arch_Estudiantes
from cursos import crear_clase, mostrar_curso, actualizar_curso, eliminar_curso, cargar_cursos, guardar_cursos
from asistencia import crear_asistencias, mostrar_asistencia, actualizar_asistencia, eliminar_asistencia, cargar_asistencias,guardar_asistencias
#----------------------------------------------------------------------------------------------
def clear_screen(): #Funcion de la libreria os,para limpiar la pantalla de los Menús.
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    '''
    Muestra el menú principal del programa.
    '''
    print("--------------------------------------- ")
    print("Menú Principal:\n")
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
        #uso de rutas
        rutaEstudiantes = "archivos/estudiantes.json"
        dic_Estudiante = cargar_arch_Estudiantes(rutaEstudiantes, 'r')

        flag_estudiantes = 0
        while flag_estudiantes == 0:
            print("\nMenú de Gestión de estudiantes")
            print("1. Agregar Estudiante")
            print("2. Mostrar estudiante")
            print("3. Actualizar estudiante")
            print("4. Eliminar estudiante")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción:")
            while True:
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
                        guardar_arch_Estudiantes(dic_Estudiante,rutaEstudiantes,"w")
                    else:
                        print("Opción no válida. Intente de nuevo.")
                    break
                except ValueError as error:
                    print(f"[Error]: {error}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error}")
                        break
                except Exception as error:
                    print(f"[Error]: {error}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error}")
                        break

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.KeyboardInterrupt")
        print("Volviendo al Menu principal..")
    except Exception:
        print("\nError inesperado")
        print("Volviendo al Menu principal..")

#------------------------------------------------------------------------------------------------------
def menu_cursos():
    '''
    Gestiona el menú de operaciones de la matriz cursos.
    '''
    #EXEPCIONES EN CURSOS
    try:
        clear_screen()
        ruta_cursos = "archivos/cursos.txt"
        matriz_cursos = cargar_cursos(ruta_cursos, 'r')
        flag_cursos = 0
        while flag_cursos == 0:
            print("\nMenú de Gestión de Cursos")
            print("1. Agregar Curso")
            print("2. Mostrar Cursos")
            print("3. Actualizar curso")
            print("4. Eliminar curso")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            while True:
                try:
                    if opcion == '1':
                        crear_clase(matriz_cursos)
                    elif opcion == '2':
                        if len(matriz_cursos) == 0:
                            print("No hay cursos registrados.")
                        else:
                            mostrar_curso(ruta_cursos, 'r')
                    elif opcion == '3':
                        actualizar_curso(matriz_cursos)
                    elif opcion == '4':
                        eliminar_curso(matriz_cursos)
                    elif opcion == '5':
                        flag_cursos = 1 #Sale del menú de cursos
                        guardar_cursos(matriz_cursos, ruta_cursos, 'w')
                    else:
                        print("Opción no válida. Intente de nuevo")
                    break
                except ValueError as error:
                    print(f"[Error]: {error}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error}")
                        break
                except Exception as error:
                    print(f"[Error]: {error}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error}")
                        break
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.KeyboardInterrupt")
        print("Volviendo al Menu principal..")
    except Exception:
        print("\nError inesperado")
        print("Volviendo al Menu principal..")

def menu_asistencia():
    '''
    Gestiona el menú de operaciones de la matríz asistencia.
    '''
    #EXEPCIONES EN ASISTENCIAS
    try:
        clear_screen()
        matriz_asistencias = cargar_asistencias('asistencias.txt', 'r')
        flag_asistencias = 0
        while flag_asistencias == 0:
            print("\nMenú de Gestión de asistencias")
            print("1. Registrar asistencias")
            print("2. Mostrar asistencias")
            print("3. Actualizar asistencias")
            print("4. Eliminar asistencia")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            while True:
                try:
                    if opcion == '1':
                        crear_asistencias(matriz_asistencias,matriz_cursos,dic_Estudiante)
                    elif opcion == '2':
                        mostrar_asistencia(matriz_asistencias)
                    elif opcion == '3':
                        actualizar_asistencia(matriz_asistencias,matriz_cursos, dic_Estudiante)
                    elif opcion == '4':
                        eliminar_asistencia(matriz_asistencias)
                    elif opcion == '5':
                        flag_asistencias = 1 # Sale del menú de asistencias
                        guardar_asistencias(matriz_asistencias, 'asistencias.txt', 'w')
                    else:
                        print("Opción no válida. Intente de nuevo.")
                    break
                except ValueError as error:
                    print(f"Error: {error}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error}")
                        break
                except Exception as error:
                    print(f"[Error]: {error}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error}")
                        break
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.KeyboardInterrupt")
        print("Volviendo al Menu principal..")
    except Exception:
        print("\nError inesperado")
        print("Volviendo al Menu principal..")

def main():
    '''
    Gestiona el flujo del programa.
    '''
    try:
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
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except Exception as error:
        print(f"Error inesperado del menú estudiantes: {error}")

if __name__ == "__main__":
    main()

