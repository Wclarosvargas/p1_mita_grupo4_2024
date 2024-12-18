from validaciones import validar_promedio,validar_id_estudiantes,validar_nombres
import json 

#Función recursiva para cargar notas
def suma_recursiva(Notas):
    if len(Notas)==1:
        return Notas[0]
    else:
        return Notas[0]+ suma_recursiva(Notas[1:])
#-----------------------------------------------------------------------------------------
def cargar_arch_Estudiantes(archivo,modo):
    try:
        with open(archivo, modo, encoding="UTF-8") as datos:
            estudiantes = json.load(datos)
    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
    return estudiantes

def guardar_arch_Estudiantes(dic_estudiantes,archivo,modo):
    try:
        with open(archivo,modo,encoding="UTF-8")as datos:
            json.dump(dic_estudiantes,datos,indent=4)

    except OSError as error:
        print(f"ERROR! {error}")
#------------------------------------------------------------------------------------------

def crearEstudiante(dic_Estudiante):
    '''
    Agrega un nuevo estudiante a la lista de Diccionarios de Estudiante.
    Solicita al usuario el ID, nombre, apellido y promedio del estudiante,
    valida los datos y los añade a la diccionarios si son correctos
    '''

    try:#Uso de try-except
        #asignación de ID
        if not dic_Estudiante:
            id = 1 
        else:
            id = max([estudiante['id'] for estudiante in dic_Estudiante]) +1
        print(f"El ID asignado al estudiante es: {id}")

        #nombre y apellido
        bandera=False
        while bandera==False:
            print("Ingrese el nombre del estudiante:")
            nombre = input()
            print("Ingrese el apellido del estudiante:")
            apellido = input()
            if validar_nombres(nombre) and validar_nombres(apellido):
                bandera=True
            else:
                print("Porfavor, ingrese solo letras")
                print("Intente nuevamente..")
        
        #Promedio
        promedio_valido = 0
        while promedio_valido == 0:
            Autorizacion=0
            while Autorizacion==0:
                print("Ingrese su nota de Matematica")
                Matematica=float(input())
                if validar_promedio(Matematica):
                    Autorizacion=1
                else:
                    print("Ingrese un numero del 1 al 10")
            while Autorizacion==1:
                print("Ingrese su nota de Historia")
                Historia=float(input())
                if validar_promedio(Historia):
                    Autorizacion=0
                else:
                    print("Ingrese un numero del 1 al 10")
            while Autorizacion==0:
                print("Ingrese su nota de Biologia")
                Biologia=float(input())
                if validar_promedio(Biologia):
                    Autorizacion=1
                else:
                    print("Ingrese un numero del 1 al 10")
            while Autorizacion==1:
                print("Ingrese su nota de Literatura")
                Literatura=float(input())
                if validar_promedio(Literatura):
                    Autorizacion=0
                else:
                    print("Ingrese un numero del 1 al 10")
            Notas=[Matematica,Historia,Biologia,Literatura]
            promedio=int((suma_recursiva(Notas))//len(Notas))
            if validar_promedio(promedio):
                promedio_valido = 1
            else:
                print("El promedio debe estar entre 1 y 10. Por favor, ingrese un promedio válido")

        #Alta de un nuevo estudiante.
        nuevo_Estudiante = {
            'id':id, 'nombre':nombre.capitalize(), 'apellido':apellido.capitalize(),'promedio':promedio
        }

        print("¡Estudiante fue agregado con exito!")
        dic_Estudiante.append(nuevo_Estudiante)

    except ValueError as error:#ej:cuando se espera un valor numerico
        raise ValueError(f"Error de Valor, datos ingresados de forma incorrecta, detalles: {error}")
    except TypeError as e:
        raise TypeError(f"Tipo de dato Incorrecto en la operacion, detalles: {e}")
    except Exception: #Excepcion general
        raise Exception("Error inesperado al crear Estudiantes")

#----------------------------------------------------------------------------------------------------------------------------------

def mostrarEstudiante(dic_estudiantes):
    '''
    Muestra la lista de Diccionarios de Estudiante en formato tabular, ordenada por promedio y ID.
    '''

    try:#Uso de try-except
        estudiantes = [{'id':estudiante['id'],'nombre':estudiante['nombre'][:10],'apellido':estudiante['apellido'][:12],'promedio':estudiante['promedio']} for estudiante in dic_estudiantes]

        #Ordena la lista de estudiantes por promedio descendente y luego por ID de forma ascendente
        estudiante_ordenados = sorted(estudiantes, key=lambda x: (-x['promedio'],x['id']))

        print("\nVista Estudiantes:")
        #se imprimira los encabezados
        print(f"| {'ID':<5} | {'Nombre':<10} | {'Apellido':<10} | {'Promedio':>10}")
        print("-"*55) #Línea de separación de los encabezados 

        #Impresión de filas de datos
        for estudiante in estudiante_ordenados:
            print(f"| {estudiante['id']:<5} | {estudiante['nombre']:<10} | {estudiante['apellido']:<10} | {estudiante['promedio']:>10.2f} |")
    
    except KeyError as error:
        raise KeyError(f"Se esperaba la clave: {error} en uno de los diccionarios de estudiantes")
    except Exception:
        raise Exception("Error Inesperado al mostrar estudiantes")
#------------------------------------------------------------------------------------------------------------------------------------
     
def actualizarEstudiante(dic_estudiantes):
    '''
    Actualiza los datos del estudiante existente en la lista de Diccionarios de Estudiante.
    Solicita al usuario el ID del estudiante, busca el estudiante por su ID,
    y actualiza su nombre, apellido y promedio si el estudiante existe.
    '''
    try:
        renovar = 0
        while renovar == 0:
            print('Ingrese el ID del estudiante que desea actualizar.')
            id_renovar = int(input().strip())

            #Busqueda del estudiante por medio de su ID
            for estudiante in dic_estudiantes: 
                if estudiante['id'] == id_renovar:
                    renovar = 1
                    print('Estudiante encontrado')

                    #Actualizar nombre
                    print('Ingrese el nuevo nombre del estudiante:')
                    estudiante['nombre'] = input().capitalize()
                    print('Ingrese el nuevo apellido del estudiante:')
                    estudiante['apellido'] = input().capitalize()

                    #Verificar que el promedio esté entre 1 y 10
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
                    return dic_estudiantes
            
            print('Estudiante no fue encontrado. Intente nuevamente.')

    except ValueError as error:
        raise ValueError(f"Se esperaba un valor numerico , detalles: {error}")
    except Exception:
        raise Exception("Error inesperado al actualizar estudiantes")
    #Relanzamos ambos errores al Menu

#---------------------------------------------------------------------------------------------------------------------------------        
def eliminarEstudiante(dic_Estudiante):
    '''
    Elimina un estudiante existente de la lista de Diccionarios de Estudiante
    Solicita al usuario el id del Estudiante,lo busca por su ID,y lo
    elimina si existe en el diccionario
    '''
    try:
        eliminar = False
        while eliminar == False:
            print('Ingrese el ID del estudiante que desea eliminar:')
            id_eliminar = int(input().strip())

            for i in range(len(dic_Estudiante)):
                if dic_Estudiante[i]['id'] == id_eliminar:
                    dic_Estudiante.pop(i)
                    print("Eliminando..")
                    print('El estudiante fue eliminado con exito!.')
                    eliminar = True
                    return dic_Estudiante
            print('Estudiante no fue encontrado. Intente nuevamente.')
    except ValueError as err:
        raise ValueError(f"Se esperaba unvalor numerico, detalles: {err}")
    except Exception:
        raise Exception(f"Error inesperado al eliminar estudiante")
    #Relanzamos ambas excepciones con raise hacia modulo menu
    