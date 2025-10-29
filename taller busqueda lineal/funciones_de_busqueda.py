#funcion para buscar productos por nombre
def buscar_nombre(productos, nombre):
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower(): #.lower() permite ignorar si es mayuscula o minuscula
            return producto                              # es decir no importa como el usuario escriba, el dato se toma
    return None

#funcion para buscar productos por nombre
def buscar_ID(productos, id_p):
    for producto in productos:
        if producto['id'] == id_p:
            return producto
    return None

#funcion para buscar productos por nombre
#comó pueden ser varios resultados, se usa un arreglo domde se almacenarán los datos hallados
def buscar_categoria(productos, categoria):
    hallados = []
    for producto in productos:
        if producto['categoria'].lower() == categoria.lower():
            hallados.append(producto)
    return hallados

#funcion para buscar productos por nombre
def buscar_disponivilidad(productos):
    disponible = []
    for producto in productos:
        if producto['stock'] > 0: #solo los productos que tengan un stock mayor que 0 seran impresos como disponibles
            disponible.append(producto)
    return disponible

#funcion para buscar productos por nombre
def rango_preci(productos, rangomen, rangomay):
    rango = []
    for producto in productos:
        if rangomen <= producto['precio'] <= rangomay: #define el rango menor y mayor de precio, dentro del cual debe estar el producto
            rango.append(producto)
    return rango

#funcion para buscar productos por nombre
def buscar_marca(productos, marca):
    hallada = []
    for producto in productos:
        if producto['marca'].lower() == marca.lower():
            hallada.append(producto)
    return hallada

#funcion para buscar productos por nombre
def cont_prod_cat(productos, categoria):
    conta_produ = 0
    for producto in productos:
        if producto['categoria'].lower() == categoria.lower():
            conta_produ += 1
    return conta_produ

#funcion para buscar productos por nombre
def buscar_nombre_emple(empleados, nombre, apellido):
    for empleado in empleados:
        if empleado['nombre'].lower() == nombre.lower() and empleado['apellido'].lower() == apellido.lower():
            return empleado
    return None

#funcion para buscar productos por nombre
def buscar_departamento(empleados, departamento):
    hallados = []
    for empleado in empleados:
        if empleado['departamento'].lower() == departamento.lower():
            hallados.append(empleado)
    return hallados

#funcion para buscar productos por nombre
#comó pueden ser varios resultados, se usa un arreglo domde se almacenarán los datos hallados
def buscar_empleado_act(empleados):
    hallados = []
    for empleado in empleados:
        if empleado['activo']:
            hallados.append(empleado)
    return hallados