empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True}
]

def buscar_nombre(empleados, nombre, apellido):
    for empleado in empleados:
        if empleado['nombre'] == nombre and empleado['apellido'] == apellido:
            return empleado
    return None

def buscar_departamento(empleados, departamento):
    hallados = []
    for empleado in empleados:
        if empleado['departamento'] == departamento:
            hallados.append(empleado)
    return hallados
#comó pueden ser varios resultados, se usa un arreglo domde se almacenarán los datos hallados
def buscar_empleado_act(empleados):
    hallados = []
    for empleado in empleados:
        if empleado['activo']:
            hallados.append(empleado)
    return hallados # se debe poner esto, de lo contrario dara un error ya que lo reconose como None    
        
#pruebas
    
result = buscar_nombre(empleados, 'María', 'Rodríguez')
if result:
    print(f"ID: {str(result['id'])}| Nombre: {result['nombre']}| Departamento: {result['departamento']}| Salario: ${result['salario']}| Estado: {result['activo']}")
else:
    print("no se encontraron los datos")

print(" ")

result_depa = buscar_departamento(empleados, 'Técnico')
if result_depa:
    for depa in result_depa:
        print(f"ID: {str(depa['id'])}| Nombre: {depa['nombre']}| Departamento: {depa['departamento']}| Salario: ${depa['salario']}| Estado: {depa['activo']}")
else:
    print("no se encontraron los datos")

print(" ")
res_emp_act = buscar_empleado_act(empleados)
if res_emp_act:
    for estado in res_emp_act:
        print(f"ID: {str(estado['id'])}| Nombre: {estado['nombre']}| Departamento: {estado['departamento']}| Salario: ${estado['salario']}| Estado: {estado['activo']}")
else:
    print("no se encontraron los datos")
