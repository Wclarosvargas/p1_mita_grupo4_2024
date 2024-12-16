import os
from estudiantes import crearEstudiante, mostrarEstudiante, actualizarEstudiante, eliminarEstudiante, cargar_arch_Estudiantes,guardar_arch_Estudiantes
from cursos import crear_curso, mostrar_curso, actualizar_curso, eliminar_curso, cargar_cursos, guardar_cursos
from asistencia import crear_asistencias, mostrar_asistencia, actualizar_asistencia, eliminar_asistencia, cargar_matriz_asistencias,guardar_asistencias
#----------------------------------------------------------------------------------------------

def clear_screen(): #Funcion de la libreria os,para limpiar la pantalla de los Menús.
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    clear_screen()
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
#ESTUDIANTES
def menu_estudiantes(rutaEstudiantes):
    '''
    Gestiona el menú de operaciones de la matriz estudiantes.
    '''
    #EXEPCIONES EN ESTUDIANTES  
    try:
        clear_screen()

        flag_estudiantes = False
        while flag_estudiantes == False: #Controla el flujo del menu y permite navegar entre las opciones
            print("\nMenú de Gestión de estudiantes")
            print("1. Agregar Estudiante")
            print("2. Mostrar estudiante")
            print("3. Actualizar estudiante")
            print("4. Eliminar estudiante")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción:")

            banderaInterna=True
            while banderaInterna: #Permite reintentar la misma opcion en caso de excepcion
                try:
                    dic_Estudiante = cargar_arch_Estudiantes(rutaEstudiantes, 'r')
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
                        flag_estudiantes = True # True sale del menú de estudiantes
                    else:
                        print("Opción no válida. Intente de nuevo.")

                except Exception as error_estudiante: #una sola Excepcion que atrapa cualquier raise del Crud estudaintes
                    print(f"[Error]: {error_estudiante}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")#Posibilidad de reingresar en caso de Excepcion
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error_estudiante}")
                        banderaInterna=False#Desactiva el bucle interno y sale hacia el Menu Estudiantes
                else:
                    guardar_arch_Estudiantes(dic_Estudiante,rutaEstudiantes,"w")
                    banderaInterna=False

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.KeyboardInterrupt")
        print("Volviendo al Menu principal..")
    except Exception:
        print("\nError inesperado")
        print("Volviendo al Menu principal..")

#------------------------------------------------------------------------------------------------------
#CURSOS
def menu_cursos(ruta_cursos):
    '''
    Gestiona el menú de operaciones de la matriz cursos.
    '''
    #EXEPCIONES EN CURSOS
    try:
        clear_screen()
        flag_cursos = False
        while flag_cursos ==False:
            print("\nMenú de Gestión de Cursos")
            print("1. Agregar Curso")
            print("2. Mostrar Cursos")
            print("3. Actualizar curso")
            print("4. Eliminar curso")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            
            banderaInterna=True
            while banderaInterna: #Permite reintentar la misma opcion en caso de excepcion
                try:
                    matriz_cursos = cargar_cursos(ruta_cursos, 'r')
                    if opcion == '1':
                        crear_curso(matriz_cursos)
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
                        flag_cursos = True  #Sale del menú de cursos
                    else:
                        print("Opción no válida. Intente de nuevo")

                except Exception as error:
                    print(f"[Error]: {error}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error}")
                        banderaInterna=False  
                else:
                    guardar_cursos(matriz_cursos, ruta_cursos, 'w')
                    banderaInterna=False 

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.KeyboardInterrupt")
        print("Volviendo al Menu principal..")
    except Exception:
        print("\nError inesperado")
        print("Volviendo al Menu principal..")

#------------------------------------------------------------------------------------------------------
#ASISTENCIAS
def menu_asistencia(rutaEstudiantes,ruta_cursos,ruta_asistencia):
    '''
    Gestiona el menú de operaciones de la matríz asistencia.
    '''
    #EXEPCIONES EN ASISTENCIAS
    try:
        clear_screen()
        flag_asistencias = False
        while flag_asistencias ==False:
            print("\nMenú de Gestión de asistencias")
            print("1. Registrar asistencias")
            print("2. Mostrar asistencias")
            print("3. Actualizar asistencias")
            print("4. Eliminar asistencia")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            banderaInterna=True
            while banderaInterna: #Permite reintentar la misma opcion en caso de excepcion
                try: 
                    #Creacion de diccionarios y matrices
                    dic_Estudiante = cargar_arch_Estudiantes(rutaEstudiantes, 'r')
                    matriz_cursos = cargar_cursos(ruta_cursos, 'r')
                    matriz_asistencias = cargar_matriz_asistencias(ruta_asistencia, 'r')

                    if opcion == '1':
                        crear_asistencias(matriz_asistencias,matriz_cursos,dic_Estudiante)

                    elif opcion == '2':
                        mostrar_asistencia(matriz_asistencias)
                    elif opcion == '3':
                        actualizar_asistencia(matriz_asistencias,matriz_cursos, dic_Estudiante)
                    elif opcion == '4':
                        eliminar_asistencia(matriz_asistencias)
                    elif opcion == '5':
                        flag_asistencias = True# Sale del menú de asistencias
                        
                    else:
                        print("Opción no válida. Intente de nuevo.")

                except Exception as error:
                    print(f"[Error]: {error}")
                    resp= input("¿Deseas intentar de nuevo? (s/n): ")
                    if resp.lower() !="s":
                        print(f"Operacion Cancelada. Ultimo Error:{error}")
                        banderaInterna=False 
                else:
                    guardar_asistencias(matriz_asistencias, ruta_asistencia, 'w')
                    banderaInterna=False 
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
    #uso de rutas en TODOS LOS MÓDULOS
    rutaEstudiantes = "archivos/estudiantes.json"
    ruta_cursos = "archivos/cursos.txt"
    ruta_asistencia = "archivos/asistencias.txt"
    
    try:
        flag_programa = False
        while flag_programa == False:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                menu_estudiantes(rutaEstudiantes)
            elif opcion == '2':
                menu_cursos(ruta_cursos)
            elif opcion == '3':
                menu_asistencia(rutaEstudiantes,ruta_cursos,ruta_asistencia)
            elif opcion == '4':
                print("Saliendo del programa...")
                flag_programa = True #Sale del programa principal
            else:
                print("Opción no válida. Intente de nuevo.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except Exception as error:
        print(f"Error inesperado del menú estudiantes: {error}")

if __name__ == "__main__":
    main()

