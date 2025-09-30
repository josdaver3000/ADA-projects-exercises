tareas_empresa = [
    {"nombre": "Procesos legales y copyright", "prioridad": 3, "tiempo": "4:50 horas"},
    {"nombre": "Configurar software de gestión", "prioridad": 5, "tiempo": "3:30 horas"},    
    {"nombre": "Archivar documentación final y copias de seguridad", "prioridad": 10, "tiempo": "2:00 horas"},
    {"nombre": "Auditoría interna del proyecto", "prioridad": 8, "tiempo": "9:00 horas"},
    {"nombre": "Diseñar cronograma del proyecto", "prioridad": 3, "tiempo": "7:00 horas"},
    {"nombre": "Definir métricas de éxito", "prioridad": 4, "tiempo": "5:00 horas"},
    {"nombre": "Monitorear presupuesto", "prioridad": 7, "tiempo": "4:00 horas"},
    {"nombre": "Capacitación del equipo en herramientas", "prioridad": 5, "tiempo": "9:00 horas"},
    {"nombre": "Evaluación final del proyecto", "prioridad": 9, "tiempo": "6:30 horas"},
    {"nombre": "Definir el alcance del proyecto", "prioridad": 1, "tiempo": "5:30 horas"},    
    {"nombre": "Analizar escalabilidad a largo plazo", "prioridad": 5, "tiempo": "8:00 horas"},
    {"nombre": "Reunión inicial con el o los clientes", "prioridad": 2, "tiempo": "2:30 horas"},
    {"nombre": "Revisión semanal de avances", "prioridad": 6, "tiempo": "2:30 horas"},
    {"nombre": "Reunión de cierre con stakeholders", "prioridad": 9, "tiempo": "3:00 horas"},
    {"nombre": "Proceso de confidencialidad y NO diculgacion", "prioridad": 2, "tiempo": "5:39 horas"},
    {"nombre": "Gestion interna de errores y/o modificaciones", "prioridad": 4, "tiempo": "6:00 horas"},
    {"nombre": "Preparar un presupuesto inicial", "prioridad": 1, "tiempo": "8:00 horas"},
    {"nombre": "Control de cambios", "prioridad": 6, "tiempo": "6:30 horas"},
    {"nombre": "Elaborar plan de comunicación", "prioridad": 4, "tiempo": "4:00 horas"},
    {"nombre": "Gestión de proveedores", "prioridad": 7, "tiempo": "5:30 horas"},
    {"nombre": "Entrega de informes al o los clientes", "prioridad": 1, "tiempo": "4:30 horas"},
    {"nombre": "Preparar documentación técnica", "prioridad": 8, "tiempo":"7:00 horas"},
    {"nombre": "Identificar riesgos del proyecto y contratar seguros", "prioridad": 2, "tiempo": "6:00 horas"},
    {"nombre": "Testing y recopilación de opiniones", "prioridad": 6, "tiempo": "5:00 horas"},
    {"nombre": "Solución de errores y modificaciones solicitadas por el cliente", "prioridad": 7, "tiempo": "8:00 horas"},
    {"nombre": "Asignar roles al equipo y organizar grupos de accion", "prioridad": 3, "tiempo": "3:30 horas"}

]

def merge_sort_tareas(lista): #funcion merge_sort_tareas que recibe la lista

    #si la la lista tiene 1 o menos elementos, ya esta ordenada y se retorna 
    if len(lista) <= 1:
        return lista

    #de lo contrario la lista se divide en dos mitades derecha e izquierda y luego se combinan con merge
    mid = len(lista) // 2
    izq_half = merge_sort_tareas(lista[:mid])
    der_half = merge_sort_tareas(lista[mid:])

    return merge(izq_half, der_half)

def merge(izq, der): #funcion merge que recibe las dos listas ordenadas
    resultado = []
    x = y = 0

    #siempre  cuando haya elementos en ambas listas 
    while x < len(izq) and y < len(der):

        #se compara la prioridad de las tareas (de mayor a menor "1 a 10")
        if izq[x]["prioridad"] < der[y]["prioridad"]:
            resultado.append(izq[x])
            x += 1

        elif izq[x]["prioridad"] > der[y]["prioridad"]:
            resultado.append(der[y])
            y += 1

        else:
            if izq[x]["tiempo"] < der[y]["tiempo"]:
                resultado.append(izq[x])
                x += 1
            else:
                resultado.append(der[y])
                y += 1
    resultado.extend(izq[x:]) #agrega los elementos restantes de "izq" a partir de x (por eso x:)
    resultado.extend(der[y:]) #agrega los elementos restantes de "der" a partir de y (por eso y:)
    return resultado

tareas_ordenadas = merge_sort_tareas(tareas_empresa) 
print(f"{'Nombre':<75}{'prioridad':<20}{'tiempo':<15}") 
print("=" * 105)

for tareas_empresa in tareas_ordenadas:
    print(f"{tareas_empresa['nombre']:<75}{tareas_empresa['prioridad']:<20}{tareas_empresa['tiempo']:<15}")