#implementacion del algoritmo Quick sort
#ejemplo del algoritmo para ordenar pedidos de un restaurante por precio de mmenor a mayor

#explicacion:
#Quick sort utiliza divide y venceras, es decir:
# divide la tabla en 3 partes a partir de un pivote o dato medio (menore, iguales y mayores)
# ordena resursivamente las listas y luego las combina

# con el metodo maestro podemos hayar la complejidad en el mejor caso del algoritmo:
# la recurrencia es T(n) = 2T(n/2) + O(n) y se calcula su complejidad con el metodo maestro
# en este caso a=2, b=2 y f(n) = O(n)
# se compara f(n) con n^log_b(a) = n^log_2(2) = n^1 = n
# caso 2 del metodo maestro cuando son iguales (n = n) => complejidad algoritmica de T(n) = Θ(n log n)

# complejidad:
# mejor caso: O(n log n) 
# peor caso: O(n²)

#con el metodo maestro no se puede realizar la solucion con el peor caso,
#porque el pivote elije o busca el elemento mas grande o mas pequeño, por ende la divicion queda en desvalance
#es decir, un lado queda con tamaño n - 1 y el otro queda de 1
#la recurrencia queda como: T(n) = T(n-1)+O(n) esto solo se puede solucionar con expancion o sustitucion
 




pedidos = [
    {"nombre_Pedido": "frijoles con carne", "cantidad": 1, "precio": 45000},
    {"nombre_Pedido": "chuleta de cerdo", "cantidad": 2, "precio": 25000},
    {"nombre_Pedido": "caja personal de arroz mixto", "cantidad": 3, "precio": 37500},
    {"nombre_Pedido": "plato de sancocho y arroz", "cantidad": 1, "precio": 20000},
    {"nombre_Pedido": "plato de tilapia frita y adicionales", "cantidad": 2, "precio": 45000},
    {"nombre_Pedido": "bandeja paisa", "cantidad": 1, "precio": 45000},
    {"nombre_Pedido": "pollo apanado", "cantidad": 1, "precio": 35000},
]

def Quick_sort_pedidos(pedidos): 
    if len(pedidos) <= 1: #si pedidos es menor o igual a 1, se retorna ya que esta ordenado o no hay datos
        return pedidos

#el pivote es un dato medio o un punto de referencia desde donde se divide la tabla
    pivote = pedidos[len(pedidos)//2]["precio"]
    men = [pedi for pedi in pedidos if pedi["precio"] < pivote] #datos meores al pivote
    igu = [pedi for pedi in pedidos if pedi["precio"] == pivote] #datos iguales al pivote
    may = [pedi for pedi in pedidos if pedi["precio"] > pivote] #datos mayores al pivote

#se usa recursividad, se ordenana las listas y luego se combinan
    return Quick_sort_pedidos(men) + igu + Quick_sort_pedidos(may) 

pedidos_ordenados = Quick_sort_pedidos(pedidos)


print(f"{'nombre_Pedido':<75}{'cantidad':<20}{'precio':<15}")

for pedido in pedidos_ordenados: 
    print(f"{pedido['nombre_Pedido']:<75}{pedido['cantidad']:<20}{pedido['precio']:<15}")