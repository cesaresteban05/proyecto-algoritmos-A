# GESTOR DE NOTAS ACADÉMICAS - PROYECTO FINAL
# ==============================================================================
# ESTRUCTURAS DE DATOS
# ==============================================================================

# Lista de diccionarios para almacenar los cursos
cursos = []

# Pila (Stack) para el historial de cambios (LIFO).
historial_cambios = []

# Cola (Queue) para solicitudes de revisión (FIFO).
solicitudes_revision = []

# ==============================================================================
# FUNCIONES DEL PROGRAMA
# ==============================================================================

def mostrar_menu():
    """Imprime el menú principal de opciones."""
    print("\n" + "="*40)
    print("====== GESTOR DE NOTAS ACADÉMICAS ======")
    print("="*40)
    print("1.  Registrar nuevo curso")
    print("2.  Mostrar todos los cursos y notas")
    print("3.  Calcular promedio general")
    print("4.  Contar cursos aprobados y reprobados")
    print("5.  Buscar curso (Búsqueda Lineal)")
    print("6.  Actualizar nota de un curso")
    print("7.  Eliminar un curso")
    print("8.  Ordenar cursos por nota (Burbuja)")
    print("9.  Ordenar cursos por nombre (Inserción)")
    print("10. Buscar curso (Búsqueda Binaria)")
    print("11. Gestionar cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (Pila)")
    print("13. Salir")
    print("="*40)

def registrar_curso():
    """Opción 1: Registra un nuevo curso con su nota (0-100)."""
    print("\n[1. Registrar Nuevo Curso]")
    nombre = input("Ingrese el nombre del curso: ").strip()
    if not nombre:
        print("Error: El nombre del curso no puede estar vacío.")
        return

    try:
        nota = int(input("Ingrese la nota del curso (0-100): "))
        if 0 <= nota <= 100:
            nuevo_curso = {'nombre': nombre, 'nota': nota}
            cursos.append(nuevo_curso)
            historial_cambios.append(f"Registro: '{nombre}' con nota {nota}")
            print(f"\n>> Curso '{nombre}' registrado exitosamente.")
        else:
            print("Error: La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Ingrese un número válido para la nota.")

def mostrar_cursos():
    """Opción 2: Muestra una lista de todos los cursos registrados."""
    print("\n[2. Lista de Cursos Registrados]")
    if not cursos:
        print("No hay cursos registrados.")
        return
    
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. Nombre: {curso['nombre']}, Nota: {curso['nota']}")

def calcular_promedio():
    """Opción 3: Calcula el promedio de las notas de todos los cursos."""
    print("\n[3. Calcular Promedio General]")
    if not cursos:
        print("No hay cursos para calcular el promedio.")
        return
    
    total_notas = sum(curso['nota'] for curso in cursos)
    promedio = total_notas / len(cursos)
    print(f"\n>> El promedio general es: {promedio:.2f}")

def contar_cursos_estado():
    """Opción 4: Cuenta los cursos aprobados (>= 60) y reprobados."""
    print("\n[4. Conteo de Cursos Aprobados y Reprobados]")
    if not cursos:
        print("No hay cursos registrados.")
        return

    aprobados = sum(1 for curso in cursos if curso['nota'] >= 60)
    reprobados = len(cursos) - aprobados

    print(f"\n>> Cursos aprobados: {aprobados}")
    print(f">> Cursos reprobados: {reprobados}")

def buscar_curso_lineal():
    """Opción 5: Busca un curso por nombre usando búsqueda lineal."""
    print("\n[5. Búsqueda Lineal de Curso]")
    if not cursos:
        print("No hay cursos registrados para buscar.")
        return

    nombre_buscado = input("Ingrese el nombre del curso a buscar: ").strip()
    encontrado = False

    for curso in cursos:
        if curso['nombre'].lower() == nombre_buscado.lower():
            print(f"\n>> ¡Curso encontrado! Nombre: {curso['nombre']}, Nota: {curso['nota']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\n>> El curso '{nombre_buscado}' no fue encontrado.")

def actualizar_nota():
    """Opción 6: Actualiza la nota de un curso y registra el cambio."""
    print("\n[6. Actualizar Nota de un Curso]")
    if not cursos:
        print("No hay cursos para actualizar.")
        return

    nombre_curso = input("Ingrese el nombre del curso a actualizar: ").strip()
    curso_encontrado = next((c for c in cursos if c['nombre'].lower() == nombre_curso.lower()), None)

    if curso_encontrado:
        try:
            print(f"Nota actual de '{curso_encontrado['nombre']}': {curso_encontrado['nota']}")
            nueva_nota = int(input("Ingrese la nueva nota (0-100): "))
            
            if 0 <= nueva_nota <= 100:
                nota_anterior = curso_encontrado['nota']
                curso_encontrado['nota'] = nueva_nota
                historial_cambios.append(f"Actualización: Nota de '{curso_encontrado['nombre']}' de {nota_anterior} a {nueva_nota}")
                print(f"\n>> ¡La nota ha sido actualizada!")
            else:
                print("Error: La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Ingrese un número válido para la nota.")
    else:
        print(f"\n>> El curso '{nombre_curso}' no fue encontrado.")

def eliminar_curso():
    """Opción 7: Elimina un curso y registra el cambio."""
    print("\n[7. Eliminar un Curso]")
    if not cursos:
        print("No hay cursos para eliminar.")
        return

    nombre_eliminar = input("Ingrese el nombre del curso a eliminar: ").strip()
    curso_encontrado = next((c for c in cursos if c['nombre'].lower() == nombre_eliminar.lower()), None)

    if curso_encontrado:
        cursos.remove(curso_encontrado)
        historial_cambios.append(f"Eliminación: Curso '{curso_encontrado['nombre']}' (Nota: {curso_encontrado['nota']})")
        print(f"\n>> El curso '{nombre_eliminar}' ha sido eliminado.")
    else:
        print(f"\n>> El curso '{nombre_eliminar}' no fue encontrado.")

def ordenar_burbuja_nota():
    """Opción 8: Ordena los cursos por nota (menor a mayor) usando Bubble Sort."""
    print("\n[8. Ordenar Cursos por Nota (Burbuja)]")
    if not cursos:
        print("No hay cursos para ordenar.")
        return
    
    cursos_a_ordenar = cursos[:] # Copia para no modificar la lista original
    n = len(cursos_a_ordenar)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if cursos_a_ordenar[j]['nota'] > cursos_a_ordenar[j + 1]['nota']:
                cursos_a_ordenar[j], cursos_a_ordenar[j + 1] = cursos_a_ordenar[j + 1], cursos_a_ordenar[j]
    
    print("\n>> Cursos ordenados por nota (menor a mayor):")
    for i, curso in enumerate(cursos_a_ordenar, 1):
        print(f"{i}. Nota: {curso['nota']}, Nombre: {curso['nombre']}")
    
    if input("¿Desea guardar este orden? (s/n): ").lower() == 's':
        cursos[:] = cursos_a_ordenar
        historial_cambios.append("Se ordenaron los cursos por nota")
        print(">> El orden ha sido guardado.")

def ordenar_insercion_nombre():
    """Opción 9: Ordena los cursos por nombre (alfabéticamente) usando Insertion Sort."""
    print("\n[9. Ordenar Cursos por Nombre (Inserción)]")
    if not cursos:
        print("No hay cursos para ordenar.")
        return
    
    cursos_a_ordenar = cursos[:] # Copia para no modificar la lista original

    for i in range(1, len(cursos_a_ordenar)):
        key = cursos_a_ordenar[i]
        j = i - 1
        while j >= 0 and key['nombre'].lower() < cursos_a_ordenar[j]['nombre'].lower():
            cursos_a_ordenar[j + 1] = cursos_a_ordenar[j]
            j -= 1
        cursos_a_ordenar[j + 1] = key
        
    print("\n>> Cursos ordenados por nombre alfabéticamente:")
    for i, curso in enumerate(cursos_a_ordenar, 1):
        print(f"{i}. Nombre: {curso['nombre']}, Nota: {curso['nota']}")

    if input("¿Desea guardar este orden? (s/n): ").lower() == 's':
        cursos[:] = cursos_a_ordenar
        historial_cambios.append("Se ordenaron los cursos por nombre")
        print(">> El orden ha sido guardado.")

def buscar_curso_binaria():
    """Opción 10: Busca un curso en la lista ordenada por nombre usando Búsqueda Binaria."""
    print("\n[10. Búsqueda Binaria de Curso]")
    if not cursos:
        print("No hay cursos para buscar.")
        return

    # La búsqueda binaria requiere que la lista esté ordenada.
    cursos_ordenados = sorted(cursos, key=lambda x: x['nombre'].lower())
    
    print("(Nota: La búsqueda se realiza sobre la lista ordenada alfabéticamente)")
    nombre_buscado = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    
    izquierda, derecha = 0, len(cursos_ordenados) - 1
    encontrado = False
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_medio = cursos_ordenados[medio]['nombre'].lower()

        if nombre_medio == nombre_buscado:
            print(f"\n>> ¡Curso encontrado! Nombre: {cursos_ordenados[medio]['nombre']}, Nota: {cursos_ordenados[medio]['nota']}")
            encontrado = True
            break
        elif nombre_medio < nombre_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    if not encontrado:
        print(f"\n>> El curso '{nombre_buscado}' no fue encontrado.")

def gestionar_cola_revision():
    """Opción 11: Gestiona la cola de solicitudes de revisión."""
    print("\n[11. Cola de Solicitudes de Revisión]")
    print("a. Agregar solicitud | b. Procesar siguiente | c. Ver pendientes")
    sub_opcion = input("Seleccione una opción: ").lower()

    if sub_opcion == 'a':
        solicitud = input("Ingrese el nombre del curso para solicitar revisión: ").strip()
        solicitudes_revision.append(solicitud) # Enqueue
        print(f">> Solicitud para '{solicitud}' agregada a la cola.")
    
    elif sub_opcion == 'b':
        if solicitudes_revision:
            solicitud_actual = solicitudes_revision.pop(0) # Dequeue
            print(f">> Procesando solicitud de: {solicitud_actual}")
        else:
            print("No hay solicitudes para procesar.")
    
    elif sub_opcion == 'c':
        if not solicitudes_revision:
            print("La cola de revisión está vacía.")
        else:
            print("Solicitudes pendientes:")
            for i, sol in enumerate(solicitudes_revision, 1):
                print(f"{i}. {sol}")
    else:
        print("Opción no válida.")

def mostrar_historial_pila():
    """Opción 12: Muestra el historial de cambios (LIFO)."""
    print("\n[12. Historial de Cambios (Pila)]")
    if not historial_cambios:
        print("No hay historial de cambios.")
        return
    
    print("Últimos cambios (del más reciente al más antiguo):")
    for cambio in reversed(historial_cambios):
        print(f"  > {cambio}")

# ==============================================================================
# BUCLE PRINCIPAL
# ==============================================================================

def main():
    """Función principal que ejecuta el bucle del menú."""
    opcion = 0
    while opcion != 13:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            
            opciones = {
                1: registrar_curso, 2: mostrar_cursos, 3: calcular_promedio,
                4: contar_cursos_estado, 5: buscar_curso_lineal, 6: actualizar_nota,
                7: eliminar_curso, 8: ordenar_burbuja_nota, 9: ordenar_insercion_nombre,
                10: buscar_curso_binaria, 11: gestionar_cola_revision, 12: mostrar_historial_pila
            }
            
            if opcion in opciones:
                opciones[opcion]()
            elif opcion == 13:
                print("\nGracias por usar el Gestor de Notas. ¡Hasta pronto!")
            else:
                print("\nError: Opción no válida.")
        
        except ValueError:
            print("\nError: Por favor, ingrese un número válido.")
        
        if opcion != 13:
            input("\nPresione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
