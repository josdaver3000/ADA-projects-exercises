#implementacion del algoritmo merge sort
#ejemplo del algoritmo para ordenar pedidos de un restaurante por precio de mayor a menor.
# si el preco es igual, se ordenara por cantidad.

#Explicacion y matematica:
# Este algoritmo utiliza la tecnica divide y venceras,
# de tal manera que distribuye el trabajo y hace todo mas eficiente,
# a comparacion de otros algoritmos de complejodad O(n^2)
# 
# con el metodo maestro podemos hayar la complejidad del algoritmo:
# la recurrencia es T(n) = 2T(n/2) + O(n) y se calcula su complejidad con el metodo maestro
# en este caso a=2, b=2 y f(n) = O(n)
# se compara f(n) con n^log_b(a) = n^log_2(2) = n^1 = n
# caso 2 del metodo maestro cuando son iguales (n = n) la complejidad algoritmica es de T(n) = Θ(n log n)



#lista de pedidos del restaurante
pedidos = [
    {"nombre_Pedido": "frijoles con carne", "cantidad": 1, "precio": 45000},
    {"nombre_Pedido": "chuleta de cerdo", "cantidad": 2, "precio": 25000},
    {"nombre_Pedido": "caja personal de arroz mixto", "cantidad": 3, "precio": 37500},
    {"nombre_Pedido": "plato de sancocho y arroz", "cantidad": 1, "precio": 20000},
    {"nombre_Pedido": "plato de tilapia frita y adicionales", "cantidad": 2, "precio": 45000},
    {"nombre_Pedido": "bandeja paisa", "cantidad": 1, "precio": 45000},
    {"nombre_Pedido": "pollo apanado", "cantidad": 1, "precio": 35000},
]


def merge_sort_precios(pedidos): #funcion meerge_sort para ordenar por precio de mayor a menor
    if len(pedidos) <= 1: #se identifica si la lista tiene un solo elemento o esta vacia (retorna pedidos ya que no ay nada que ordenar)
        return pedidos
    
    mid = len(pedidos)//2 #se divide la lista en dos mitades (izquierda y derecha) "subproblemas"

    #se llama a la funcion recursivamente para ordenar las dos mitades y luego se combinan con merge 
    izq = merge_sort_precios(pedidos[:mid]) 
    der = merge_sort_precios(pedidos[mid:])
    return merge(izq, der)

#funcion merge para combinar las dos mitades ordenadas
def merge(izq, der):
    resultado = []
    x = y = 0 #variables para recorrer las 2 mitades

#combinacion de las dos mitades ordenadas
    #menor a mayor
    while x < len(izq) and y < len(der):
        if izq[x]["precio"] > der[y]["precio"]:
            resultado.append(izq[x])
            x += 1

        elif izq[x]["precio"] < der[y]["precio"]:
            resultado.append(der[y])
            y += 1

    #si el precio es igual, se oredena por cantidad de mayor a menor
        else:
            if izq[x]["cantidad"] > der[y]["cantidad"]:
                resultado.append(izq[x])
                x += 1
            else:
                resultado.append(der[y])
                y += 1
        
    resultado.extend(izq[x:])
    resultado.extend(der[y:])
    return resultado

#llamada a la funcion merge_sort_precios que se guarda en una nueva variable (pedidos_ordenados)
pedidos_ordenados = merge_sort_precios(pedidos) 
print(f"{'nombre_Pedido':<75}{'cantidad':<20}{'precio':<15}")

for pedido in pedidos_ordenados: 
    print(f"{pedido['nombre_Pedido']:<75}{pedido['cantidad']:<20}{pedido['precio']:<15}")
