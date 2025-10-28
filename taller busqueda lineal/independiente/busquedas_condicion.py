productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]

def buscar_disponivilidad(productos):
    disponible = []
    for producto in productos:
        if producto['stock'] > 0:
            disponible.append(producto)
    return disponible

def rango_preci(productos, rangomen, rangomay):
    rango = []
    for producto in productos:
        if rangomen <= producto['precio'] <= rangomay:
            rango.append(producto)
    return rango

def buscar_marca(productos, marca):
    hallada = []
    for producto in productos:
        if producto['marca'] == marca:
            hallada.append(producto)
    return hallada

def cont_prod_cat(productos, categoria):
    conta_produ = 0
    for producto in productos:
        if producto['categoria'] == categoria:
            conta_produ += 1
    return conta_produ

disponivilidad = buscar_disponivilidad(productos)
print(f"=========productos disponibles===========")
if disponivilidad:
    for produ in disponivilidad:
        print(f"ID: {str(produ['id'])} | Nombre: {produ['nombre']} | Marca: {produ['marca']} | Categoría: {produ['categoria']} | Precio: ${produ['precio']} | Stock: {produ['stock']}")
else:
    print("no hay productos disponibles")

print(f"=========productos en rango de precio===========")
rango = rango_preci(productos, 1000, 1500)
if rango:
    for ran in rango:
        print(f"ID: {str(ran['id'])} | Nombre: {ran['nombre']} | Marca: {ran['marca']} | Categoría: {ran['categoria']} | Precio: ${ran['precio']} | Stock: {ran['stock']}")
else:
    print("no hay productos dentro del rango")

print(f"=========Numero de productos contado===========")
categoria = 'Laptop'
canti_produc = cont_prod_cat(productos, categoria)
print(f"la cantidad de productos encontrados en la cateoria '{categoria}' son: {canti_produc}")
