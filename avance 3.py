# GESTOR DE NOTAS ACADÉMICAS - PROYECTO 

# Estructuras de datos (simulando bases de datos)
# La lista 'cursos' almacenará diccionarios, donde cada diccionario representa un curso.
# Por ejemplo: {'nombre': 'Matemáticas', 'nota': 85}
cursos = []

# La lista 'historial_cambios' funcionará como una pila para los cambios.
# Se agregarán y eliminarán elementos en el último en entrar, primero en salir
historial_cambios = []

# La lista 'solicitudes_revision' funcionará como una cola.
# Se agregarán elementos al final y se procesarán desde el inicio.
solicitudes_revision = []

def mostrar_menu():
    #Función para mostrar el menú principal en la consola
    print("\n" + "="*40)
    print("====== GESTOR DE NOTAS ACADÉMICAS ======")
    print("="*40)
    print("1.  Registrar nuevo curso")
    print("2.  Mostrar todos los cursos y notas")
    print("3.  Calcular promedio general")
    print("4.  Contar cursos aprobados y reprobados")
    print("5.  Buscar curso por nombre (búsqueda lineal)")
    print("6.  Actualizar nota de un curso")
    print("7.  Eliminar un curso")
    print("8.  Ordenar cursos por nota (ordenamiento burbuja)")
    print("9.  Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")
    print("="*40)

# FUNCIONES DE GESTIÓN CON IMPLEMENTACIÓN

def registrar_curso():
    # Implementa la funcionalidad para el menú 1.
    # Solicita nombre y nota, y los agrega a la lista 'cursos'.
    # Debe validar que la nota esté entre 0 y 100.

    print("\n[Funcionalidad: Registrar nuevo curso]")
    nombre = input("Ingrese el nombre del curso: ").strip()
    try:
        nota = int(input("Ingrese la nota del curso (0-100): "))
        if 0 <= nota <= 100:
            nuevo_curso = {'nombre': nombre, 'nota': nota}
            cursos.append(nuevo_curso)
            print(f"\nCurso '{nombre}' con nota {nota} registrado exitosamente.")
        else:
            print("Error: La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para la nota.")

def mostrar_cursos():
    # Implementa la funcionalidad para el menú 2.
    # Muestra la lista de todos los cursos y sus notas.
 
    print("\n[Funcionalidad: Mostrar todos los cursos y notas]")
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. Nombre: {curso['nombre']}, Nota: {curso['nota']}")

def calcular_promedio():
   # Implementa la funcionalidad para el menú 3.
   # Calcula el promedio general de todas las notas.
    
    print("\n[Funcionalidad: Calcular promedio general]")
    if not cursos:
        print("No hay cursos para calcular el promedio.")
        return
    
    total_notas = sum(curso['nota'] for curso in cursos)
    promedio = total_notas / len(cursos)
    print(f"\nEl promedio general de las notas es: {promedio:.2f}")

# Contadores
def contar_cursos_estado():
   # Implementa la funcionalidad para el menú 4.
   # Cuenta y muestra los cursos aprobados y reprobados (>= 60).

    print("\n[Funcionalidad: Contar cursos aprobados y reprobados]")
    
    if not cursos:
        print("No hay cursos registrados.")
        return

    # Contadores
    aprobados = 0
    reprobados = 0

    for curso in cursos:
        # Condicional para determinar si el curso está aprobado o reprobado
        if curso['nota'] >= 60:
            aprobados += 1  # Incrementa el contador de aprobados
        else:
            reprobados += 1 # Incrementa el contador de reprobados

    print(f"\nCursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

## Búsqueda Lineal
def buscar_curso_lineal():
    # Implementa la funcionalidad para el menú 5.
    # Realiza una búsqueda lineal de un curso por nombre.
    
    print("\n[funcionalidad: Buscar curso por nombre (búsqueda lineal)]")
    
    if not cursos:
        print("No hay cursos registrados para buscar.")
        return

    nombre_buscado = input("Ingrese el nombre del curso a buscar: ").strip()
    encontrado = False

    # Bucle para la búsqueda lineal
    for curso in cursos:
        if curso['nombre'].lower() == nombre_buscado.lower():
            print(f"\n¡Curso encontrado! Nombre: {curso['nombre']}, Nota: {curso['nota']}")
            encontrado = True
            break # Detiene la búsqueda una vez que se encuentra el curso

    if not encontrado:
        print(f"\nEl curso '{nombre_buscado}' no fue encontrado.")

## Actualización de Datos
def actualizar_nota():
    # Implementa la funcionalidad para el menú 6.
    # Permite actualizar la nota de un curso existente.
    
    print("\n[Funcionalidad: Actualizar nota de un curso]")
    
    if not cursos:
        print("No hay cursos para actualizar.")
        return

    nombre_curso = input("Ingrese el nombre del curso a actualizar: ").strip()
    
    curso_encontrado = None
    # Búsqueda para encontrar el curso a actualizar
    for curso in cursos:
        if curso['nombre'].lower() == nombre_curso.lower():
            curso_encontrado = curso
            break

    if curso_encontrado:
        try:
            nueva_nota = int(input("Ingrese la nueva nota (0-100): "))
            # Validación con condicional
            if 0 <= nueva_nota <= 100:
                curso_encontrado['nota'] = nueva_nota # Actualización del dato
                print(f"\n¡La nota de '{curso_encontrado['nombre']}' ha sido actualizada a {nueva_nota}!")
            else:
                print("Error: La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la nota.")
    else:
        print(f"\nEl curso '{nombre_curso}' no fue encontrado.")

def eliminar_curso():
    # Implementa la funcionalidad para el menú 7.
    # Elimina un curso de la lista.
    
    print("\n[Funcionalidad: Eliminar un curso]")
    if not cursos:
        print("No hay cursos para eliminar.")
        return

    nombre_eliminar = input("Ingrese el nombre del curso a eliminar: ").strip()
    
    curso_encontrado = None
    for curso in cursos:
        if curso['nombre'].lower() == nombre_eliminar.lower():
            curso_encontrado = curso
            break

    if curso_encontrado:
        cursos.remove(curso_encontrado)
        print(f"\nEl curso '{nombre_eliminar}' ha sido eliminado.")
    else:
        print(f"\nEl curso '{nombre_eliminar}' no fue encontrado.")

def ordenar_burbuja_nota():
    # Implementa la funcionalidad para el menú 8.
    # Ordena los cursos por nota usando el algoritmo de ordenamiento burbuja.
    
    print("\n[Funcionalidad: Ordenar cursos por nota (burbuja)]")
    if not cursos:
        print("No hay cursos para ordenar.")
        return
    
    n = len(cursos)
    # Bucle para el ordenamiento burbuja
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if cursos[j]['nota'] > cursos[j + 1]['nota']:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    
    print("\nCursos ordenados por nota de menor a mayor:")
    mostrar_cursos()

def ordenar_insercion_nombre():
    # Implementa la funcionalidad para el menú 9.
    # Ordena los cursos por nombre usando el algoritmo de ordenamiento por inserción.
    
    print("\n[Funcionalidad: Ordenar cursos por nombre (inserción)]")
    if not cursos:
        print("No hay cursos para ordenar.")
        return
    
    n = len(cursos)
    # Bucle para el ordenamiento por inserción
    for i in range(1, n):
        key = cursos[i]
        j = i - 1
        while j >= 0 and key['nombre'].lower() < cursos[j]['nombre'].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key
        
    print("\nCursos ordenados por nombre alfabéticamente:")
    mostrar_cursos()

def buscar_curso_binaria():
    # Implementa la funcionalidad para el menú 10.
    # Realiza una búsqueda binaria en la lista de cursos (debe estar ordenada por nombre)
    
    print("\n[Funcionalidad: Buscar curso por nombre (búsqueda binaria)]")
    if not cursos:
        print("No hay cursos para buscar. Ordene primero por nombre (Opción 9).")
        return
    
    nombre_buscado = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    
    # Aseguramos que la lista esté ordenada para la búsqueda binaria
    ordenar_insercion_nombre()

    izquierda, derecha = 0, len(cursos) - 1
    encontrado = False
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_medio = cursos[medio]['nombre'].lower()

        if nombre_medio == nombre_buscado:
            print(f"\n¡Curso encontrado! Nombre: {cursos[medio]['nombre']}, Nota: {cursos[medio]['nota']}")
            encontrado = True
            break
        elif nombre_medio < nombre_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    if not encontrado:
        print(f"\nEl curso '{nombre_buscado}' no fue encontrado.")

def simular_cola_revision():
    # Implementa la funcionalidad para el menú 11.
    # Simula una cola de solicitudes de revisión.
    
    print("\n[Funcionalidad: Simular cola de solicitudes de revisión]")
    solicitud = input("Ingrese el curso para solicitar revisión: ").strip()
    solicitudes_revision.append(solicitud)
    print(f"Solicitud para '{solicitud}' agregada a la cola.")
    
    if solicitudes_revision:
        print("\nProcesando solicitudes...")
        while solicitudes_revision:
            solicitud_actual = solicitudes_revision.pop(0) # Retira el primer elemento
            print(f"  > Procesando solicitud de: {solicitud_actual}")
        print("Todas las solicitudes han sido procesadas.")
    else:
        print("No hay solicitudes para procesar.")

def mostrar_historial_pila():
    # Implementa la funcionalidad para el menú 12.
    # Muestra el historial de cambios guardados en la pila
    
    print("\n[Funcionalidad: Mostrar historial de cambios (pila)]")
    if not historial_cambios:
        print("No hay historial de cambios.")
        return
    
    print("Últimos cambios (del más reciente al más antiguo):")
    # Recorremos la pila sin modificarla
    for i in range(len(historial_cambios) - 1, -1, -1):
        print(f"  > {historial_cambios[i]}")

# ==============================================================================
# BUCLE PRINCIPAL DEL PROGRAMA
# Controla el flujo de la aplicación mostrando el menú y procesando las opciones.

def main():
    # Función principal que contiene el bucle del menú.
    
    opcion = None

    while opcion != 13:
        mostrar_menu()
        
        # Validación de la entrada del usuario para asegurar que es un número
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("\nError: Por favor, ingrese un número válido del 1 al 13.")
            continue # Vuelve al inicio del bucle para mostrar el menú de nuevo

        # Lógica para llamar a la función correspondiente según la opción
        # (Condicionales)
        if opcion == 1:
            registrar_curso()
        elif opcion == 2:
            mostrar_cursos()
        elif opcion == 3:
            calcular_promedio()
        elif opcion == 4:
            contar_cursos_estado()
        elif opcion == 5:
            buscar_curso_lineal()
        elif opcion == 6:
            actualizar_nota()
        elif opcion == 7:
            eliminar_curso()
        elif opcion == 8:
            ordenar_burbuja_nota()
        elif opcion == 9:
            ordenar_insercion_nombre()
        elif opcion == 10:
            buscar_curso_binaria()
        elif opcion == 11:
            simular_cola_revision()
        elif opcion == 12:
            mostrar_historial_pila()
        elif opcion == 13:
            print("\nGracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
        else:
            print("\nOpción no válida. Por favor, seleccione un número del 1 al 13.")
            
# Punto de entrada principal para ejecutar el programa
if __name__ == "__main__":
    main()