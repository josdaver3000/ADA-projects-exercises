productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]


def buscar_nombre(producto, nombre):
    for producto in productos:
        if producto['nombre'] == nombre:
            return producto
    return None

def buscar_ID(producto, id_p):
    for producto in productos:
        if producto['id'] == id_p:
            return producto
    return None

#comó pueden ser varios resultados, se usa un arreglo domde se almacenarán los datos hallados
def buscar_categoria(producto, categoria):
    hallados = []
    for producto in productos:
        if producto['categoria'] == categoria:
            hallados.append(producto)
    return hallados # se debe poner esto, de lo contrario dara un error ya que lo reconose como None    
        
#pruebas
    
# ======== busqueda por nombre =========
print("========= Producto encontrado por nombre =========")
resultado_nombre = buscar_nombre(productos, 'Dell XPS 13')
if resultado_nombre:
    produ = resultado_nombre
    print(f"ID: {str(produ['id'])} | Nombre: {produ['nombre']} | Marca: {produ['marca']} | Categoría: {produ['categoria']} | Precio: ${produ['precio']} | Stock: {produ['stock']}")
else:
    print("No se encontró ningún producto con ese nombre.")


# ======== busqueda por ID =========
print(f"\n========= Producto encontrado por ID =========")
result_id = buscar_ID(productos, 1)
if result_id:
    print(f"ID: {str(result_id['id'])} | Nombre: {result_id['nombre']} | Marca: {result_id['marca']} | Categoría: {result_id['categoria']} | Precio: ${result_id['precio']} | Stock: {result_id['stock']}")
else:
    print("No se encontró ningún producto con ese ID.")

# ======== busqueda por categoría =========
print(f"\n========= Productos encontrados por categoría =========")
resultado_categoria = buscar_categoria(productos, 'Smartphone')
if resultado_categoria:
    for produ in resultado_categoria:
        print(f"ID: {str(produ['id'])} | Nombre: {produ['nombre']} | Marca: {produ['marca']} | Precio: ${produ['precio']} | Stock: {produ['stock']}")
else:
    print("No se encontraron productos en esa categoría.")


