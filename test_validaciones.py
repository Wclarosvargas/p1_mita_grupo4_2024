from validaciones import validadr_id_unico, validar_estado, validar_fecha,validar_horario,validar_id_curso,validar_id_estudiantes,validar_id_profesor,validar_promedio
from cursos import cargar_cursos

def test_id_curso():
    #Carga la matriz cursos desde el archivo
    matriz_cursos = cargar_cursos("archivos/cursos.txt", 'r')

    # Prueba para un ID existente
    resultado = validar_id_curso(matriz_cursos, 108)
    assert resultado == True  # Esperamos que devuelva 1

    # Prueba para un ID inexistente
    resultado = validar_id_curso(matriz_cursos, 106)
    assert resultado == False  # Esperamos que devuelva 0
    

def test_validar_estado():
    resultado = validar_estado('presente')
    assert resultado is True

    resultado = validar_estado('ausente')
    assert resultado is True

    resultado = validar_estado('otro')
    assert resultado is False 