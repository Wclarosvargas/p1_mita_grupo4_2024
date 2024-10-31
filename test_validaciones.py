from validaciones import validadr_id_unico, validar_estado, validar_fecha,validar_horario,validar_id_curso,validar_id_estudiantes,validar_id_profesor,validar_promedio
from menu import matriz_cursos, matriz_asistencias

def test_id_curso():
    #prueba para un id existente
    resultado = validar_id_curso(matriz_cursos, 101)
    assert resultado == 1

    #prueba para un id inexistente
    resultado = validar_id_curso(matriz_cursos,106)
    assert resultado == 0

def test_validar_estado():
    resultado = validar_estado('presente')
    assert resultado is True

    resultado = validar_estado('ausente')
    assert resultado is True

    resultado = validar_estado('otro')
    assert resultado is False