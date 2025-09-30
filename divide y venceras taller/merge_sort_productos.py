import csv #importacion de la libreria para leer el archivo csv

productos = []

#abrir el archivo CSV, "r" para que el archivo sea en lecctura (read),
#encoding para que lea los caracteres especiales como tildes, letras como ñ o emojis, 
with open("divide y venceras taller\productos.csv", "r", encoding="utf-8") as f: 
    lector = csv.DictReader(f) #DictReader convierte las filas del CSV en diccionarios con claves = nombres de las columnas
    for fila in lector: #para recorrer cada fila del archivo csv
        #aqui se convierten los datos a su tipo correspondiente en estilo diccionario
        productos.append({
            "id": int(fila["id"]),
            "nombre": fila["nombre"], 
            "precio": float(fila["precio"]),
            "calificacion": int(fila["calificacion"]),
            "stock": int(fila["stock"])
        })

def merge_sort_productos(lista): #funcion merge_sort_productos que recibe la lista

    #si la la lista tiene 1 o menos elementos, ya esta ordenada y se retorna 
    if len(lista) <= 1:
        return lista

    #de lo contrario la lista se divide en dos mitades derecha e izquierda y luego se combinan con merge
    mid = len(lista) // 2
    izq_half = merge_sort_productos(lista[:mid])
    der_half = merge_sort_productos(lista[mid:])

    return merge(izq_half, der_half)

def merge(izq, der): #funcion merge que recibe las dos listas ordenadas
    resultado = []
    x = y = 0

    #siempre  cuando haya elementos en ambas listas 
    while x < len(izq) and y < len(der):

        #se compara la calificacion de los productos (de mayor a menor "5 a 1")
        if izq[x]["calificacion"] > der[y]["calificacion"]:
            resultado.append(izq[x])
            x += 1

        elif izq[x]["calificacion"] < der[y]["calificacion"]:
            resultado.append(der[y])
            y += 1

        #si tienen la midma calificacon, se hace una comparacion por precio (de menor a mayor)
        else:
            if izq[x]["precio"] < der[y]["precio"]:
                resultado.append(izq[x])
                x += 1
            else:
                resultado.append(der[y])
                y += 1
    resultado.extend(izq[x:]) #agrega los elementos restantes de "izq" a partir de x (por eso x:)
    resultado.extend(der[y:]) #agrega los elementos restantes de "der" a partir de y (por eso y:)
    return resultado


#para ver los 5mil datos ordenados por calificacion y precio.
#debes descomentar las siguientes lineas y COMENTAR o ELIMINAR las lineas de abajo que crean el diseño para los 20 primeros y 20 ultimos

#como nota adicional, la terminal no podra mostrar los 5mil datos (productos),
#porque esta tiene un limite de datos que si se exede continua imprimiendo pero elimina lo anterior para poder continuar
#-------------------------------------------------------
# productos_ordenados = merge_sort_productos(productos) 
# for producto in productos_ordenados:
#   print(producto)
#-------------------------------------------------------



# Mostrar los 20 primeros y 20 últimos productos ordenados como prueba de que funciona
productos_ordenados = merge_sort_productos(productos) 

print("\n" + "*******20 PRIMEROS PRODUCTOS ORDENADOS*******" + "\n")

print(f"{'ID':<6}{'Nombre':<15}{'Precio':<10}{'Calificación':<15}{'Stock':<6}") 
print("=" * 60)

# 20 primeros
for productos in productos_ordenados[:20]: # muestra los primeros 20 productos
    print(f"{productos['id']:<6}{productos['nombre']:<15}{productos['precio']:<10.2f}{productos['calificacion']:<15}{productos['stock']:<6}")

print("\n" + "_" * 60 + "\n")

print("\n" + "*******20 ULTIMOS PRODUCTOS ORDENADOS*******" + "\n")

# 20 últimos
print(f"{'ID':<6}{'Nombre':<15}{'Precio':<10}{'Calificación':<15}{'Stock':<6}")
print("=" * 60)
for productos in productos_ordenados[-20:]: # muestra los ultimos 20 productos
    print(f"{productos['id']:<6}{productos['nombre']:<15}{productos['precio']:<10.2f}{productos['calificacion']:<15}{productos['stock']:<6}")