# GESTOR DE NOTAS ACADÉMICAS

## Descripción del Proyecto

Este es un proyecto de consola en Python diseñado para la gestión de notas académicas. Permite a los usuarios registrar, visualizar, actualizar y **eliminar cursos**. El programa también realiza cálculos estadísticos como el promedio de notas y el conteo de cursos aprobados y reprobados.

El proyecto está estructurado para ser didáctico, demostrando el uso de **listas** en Python como una forma simple de base de datos. Se implementan de forma nativa estructuras de **pila** y **cola** para gestionar operaciones de historial y solicitudes de revisión. Además, se incluyen algoritmos comunes de **búsqueda** (lineal y binaria) y **ordenamiento** (burbuja e inserción).

## Estructura del Código

El código está organizado en funciones modulares, lo que facilita su lectura y mantenimiento:

* **Funciones de Gestión**: `registrar_curso()`, `actualizar_nota()`, y `eliminar_curso()` permiten manipular los datos de los cursos.
* **Funciones de Análisis**: `calcular_promedio()` y `contar_cursos_estado()` proveen estadísticas útiles.
* **Algoritmos**: Funciones como `buscar_curso_lineal()`, `ordenar_burbuja_nota()`, y `buscar_curso_binaria()` demuestran la aplicación de algoritmos básicos.
* **Flujo del Programa**: `mostrar_menu()` y la función principal `main()` controlan la interacción con el usuario.

## Cómo Ejecutar el Proyecto

1.  Asegúrate de tener Python 3.x instalado en tu computadora.
2.  Copia y pega el código completo en un archivo llamado `gestor_notas.py`.
3.  Abre una terminal o línea de comandos.
4.  Navega hasta el directorio donde guardaste el archivo.
5.  Ejecuta el programa con el siguiente comando:
    ```bash
    python gestor_notas.py
    ```
6.  Sigue las instrucciones que aparecen en el menú para interactuar con el gestor de notas.