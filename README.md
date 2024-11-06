### Proyecto Registro de Asistencias

El proyecto consiste en un sistema de registro para estudiantes, cursos y asistencias en un entorno educativo. Este sistema permite a los usuarios agregar, actualizar, eliminar y visualizar.

- Módulo de estudiantes: Permite agregar nuevos estudiantes, actualizar sus datos, eliminar registros y mostrar una lista de estudiantes ordenada por promedio.
- Módulo de cursos: permite agregar cursos, actualizarlos y eliminar los cursos, asi como la visualización de información de cursos.
- Módulo de asistencias: Ofrece funciones para registrar, actualizar, eliminar y mostrar asistencias, además ofrece la capacidad para contar asistencias presentes y ausentes.

El sistema está compuesto por módulos independientes para cada una de las matrices y diccionarios utilizados, además el uso de funciones de validación para asegurar la integridad de los datos introducidos.

### Problemas encontrados
1. Validación de los datos
   - problemas iniciales respecto a los ids duplicados o promedios fuera del rango permitido
   - Para solucionarlo se implemento funciones de validación especificas para cada tipo de dato. Por ejemplo funciones para verificar la unicidad de los IDs, validar promedios dentro del rango permitido, y verificar formatos correctos para fechas y horarios mediante el uso de expresiones regulares.
2. Interfaz de Usuario
   - La interfaz del usuario era demasiada rudimentaria y no guiaba al usuario de manera clara lo cual podía llevar a posibles confusiones y errores.
   - Se diseñó un menú principal con submenús para gestionar estudiantes, cursos y asistencias. Cada submenú ofrece sus respectivas opciones de manera clara y consisa. Además se implementaron mensajes de error para opciones no válidas, proporcionando al usuario una mejor experiencia más intuitiva y amigable.

3. Eficiencia y Organización del codigo
   - El codigo original carecia de una estructura organizada lo cual dificultaba su mantenimiento y extensión.
   - Se reestructuró el código para seguir principios de buena programación y buenas prácticas, como modularizar las matrices y diccionarios y como tambien del uso de las variables utilizadas.Usamos matrices en los módulos cursos y asistencias y Diccionarios en el módulo Estudiantes y cada función de validación que se utiliza para todos los modulos se estructuró en un solo archivo.

4. Documentación y Comentarios
   - La falta de documentación y comentarios en el código hacía difícil entender la funcionalidad de cada parte del sistema y al momento de saber cual fue la mejora que hacia el compañero.
   - Para solucionarlo se implemento el uso de docstring y comentarios detallados a cada función y módulo.
5. Uso de Archivos Planos y JSON
   -Nos enfrentamos en el dilema de dejar de usar las matrices y diccionarios que implementamos anteriormente en los 3 modulos a empezar a usar textos Planos y JSON, nos encontramos con el problema de la eliminacion de todos nuestros datos.
   -Para solucionarlo usamos excepciones para capturar errores , bucles True para  cargar y guardar los respectivos archivos.