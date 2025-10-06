#implementacion del algoritmo busqueda binaria
#ejemplo del algoritmo para buscar un precio especifico en un arreglo 
#el arreglo se ordena posteriormente con .sort() para que la busqueda binaria funcione correctamente

#Explicacion y matematica:
# Este algoritmo utiliza la tecnica divide y venceras,
# de tal manera que divide el arreglo en mitades,
# compara con el precio requerido y descarta la mitad en la cual NO esta.
# con el metodo maestro podemos hayar la complejidad del algoritmo:

# la recurrencia es T(n) = T(n/2) + O(1) y se calcula su complejidad con el metodo maestro
# en este caso a=1, b=2 y f(n) = O(1)
# se compara f(n) con n^log_b(a) = n^log_2(1) = n^0 = 1
# caso 2 del metodo maestro cuando son iguales complejidad algoritmica de T(n) = Θ(log n) "es log n y no (n log n)
#porque solo se hace una llamada recursiva (1T) y no dos como en el merge sort (2T)"

#arr de precios
precios = [45300, 25000, 37500, 20000, 45000, 55000, 35000]

#antes de empezar la busqueda binaria, el arreglo debe estar ordenado
#para que el algoritmo sepa donde partir para hallar el valor (precio)
precios.sort()


def busqueda_binaria_precios(precios, precioB): #funcion que aplica la busqueda binaria
    inicio = 0
    fin = len(precios) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2 #encuentra la mitad del arreglo
        precioM = precios[mitad] #obtiene el valor del precio en la mitad

        if precioM == precioB: #si el precio en la mitad es igual al precio buscado, retorna el precio
            return precios[mitad]
        
        #de lo contrario, si el precio en la mitad es MENOR al precio buscado,
        #se descarta lo anterior y se inicia desde el valor siguiente por eso inicio = mitad + 1 
        elif precioM < precioB: 
            inicio = mitad + 1

        #por otro lado, si el precio en la mitad es mayor al precio buscado,
        #se descarta lo posterior y se finaliza en el valor anterior por eso fin = mitad - 1
        else: 
            fin = mitad - 1
    return None


precio_buscar = 45000
resultado = busqueda_binaria_precios(precios, precio_buscar)

if resultado: 
    print(f"Pedido encontrado: {resultado}")
else:
    print("no se encuentra el pedido")