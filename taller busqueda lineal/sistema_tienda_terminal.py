from funciones_de_busqueda import * #importar todo desde funciones de busqueda
from datos_ejemplo import empleados, productos #importar desde datos de ejemplo, productos y empleados


#creacion del menu principal
def menu_principal():
    while True:
        print("\n========menu principal========")
        print("1) buscar productos")
        print("2) buscar empleados")
        print("3)Salir")

    #opciones
        opcion = input("elija una opcion: ")  #guarda la eleccion del usuario

        if opcion == '1':
            menu_de_productos()
        elif opcion == '2':
            menu_de_empleados()
        elif opcion == '3':
            break
        else:
            print("la opcion elejida NO es valida, elija otra opcion")


#submenu de productos
def menu_de_productos():
    while True:
        print("\n==========menu para buscar productos==========")
        print("1) buscar producto por nombre")
        print("2) buscar producto por ID")
        print("3) buscar producto por categoria")
        print("4) buscar producto por disponivilidad")
        print("5) buscar producto por rango de precio")
        print("6) buscar producto por marca")
        print("7) buscar por cantidad segun la categoria")     
        print("8) regresar al menu principal")

        opcion = input("elija una opcion: ") #almacena la eleccion del usuario

        if opcion == '1':
            nombre = input("ingrese el nombre del producto")
            resultado = buscar_nombre(productos, nombre)
            mostrar_productos(resultado)
        
        #manejo de errores con try-except para evitar bloqueos por entradas no validas,
        # (solo se aplica en las fucniones donde el usuario debe ingresar datos)
        elif opcion == '2':
            while True:
                try:
                    id_p = int(input("ingrese el ID del producto"))

                except ValueError:
                    print("Error. ingrese un numero valido")
                    continue

                resultado = buscar_ID(productos, id_p)
                mostrar_productos([resultado] if resultado else [])
                

        elif opcion == '3':
            categoria = input("ingrese la categoria del producto")
            resultado = buscar_categoria(productos, categoria)
            mostrar_productos(resultado)

        elif opcion == '4':
            resultado = buscar_disponivilidad(productos)
            mostrar_productos(resultado)
        
        elif opcion == '5':
            while True:
                try:
                    rangomen = float(input("ingrese el precio minimo"))
                    rangomay = float(input("ingrese el precio maximo"))
                    #condicional que proteje al sistema de errores, en caso de que el usuario ingrese los valores alrevez
                    if rangomen > rangomay:
                        print(f"el precio minimo no puede ser mayor que el precio maximo ")
                        continue
                    break

                except ValueError:
                    print("Error. ingrese un numero valido \n")

            resultado = rango_preci(productos, rangomen, rangomay)

            if resultado:
                mostrar_productos(resultado)
            else:
                print(f"no hay productos dentro del rango de precio: {rangomen} - {rangomay}")

        elif opcion == '6':
            marca = input("ingrese la marca del producto")
            resultado = buscar_marca(productos, marca)
            mostrar_productos(resultado)

        elif opcion == '7':
            categoria = input("ingrese la categoria del producto")
            resultado = cont_prod_cat(productos, categoria)
            mostrar_productos(resultado)
            print(f"la cantidad de productos encontrados en la cateoria '{categoria}' es: {resultado}")

        elif opcion == '8':
            break
        else:
            print("la opcion elejida NO es valida, elija otra opcion")
        
def menu_de_empleados():
    while True:
        print("\n==========menu para buscar empleados==========")
        print("1) buscar empleado por nombre")
        print("2) buscar empleado por departamento")
        print("3) buscar empleado por estado (activo o no)")
        print("4) regresar al menu principal")

        opcion = input("elija una opcion: ")

        if opcion == '1':
            nombre = input("ingrese el nombre del empleado")
            apellido = input("ingrese el apelllido del empleado")
            resultado = buscar_nombre_emple(empleados, nombre, apellido)
            mostrar_empleado(resultado)

        elif opcion == '2':
            departamento = input("ingrese el departamento")
            resultado = buscar_departamento(empleados, departamento)
            mostrar_empleado(resultado)

        elif opcion == '3':
            resultado = buscar_empleado_act(empleados)
            mostrar_empleado(resultado)
        
        elif opcion == '4':
            break
        else:
            print("la opcion elejida NO es valida, elija otra opcion")


#================ funciones para imprimir los resutlados=============
            
def mostrar_productos(resultado):

    #se normaliza el resultado para que siempre devuelva listas, esto para que no ocurran errores al leer diccionarios u otros
    if resultado is None:
        lista = []
    elif isinstance(resultado, dict):
        lista = [resultado]
    elif isinstance(resultado, list):
        lista = resultado
    else:
        # por seguridad, rechaza otros tipos paa que no ocurran errores
        lista = []

    # filtra solo elementos que sean dicts válidos
    lista_filtrada = [p for p in lista if isinstance(p, dict)]

    if not lista_filtrada:
        print("No se encontraron productos.")
        return

    print("\n ======== Resultado =======")
    for produ in lista_filtrada:
        print(f"ID: {produ['id']} | Nombre: {produ['nombre']} | Marca: {produ['marca']} | Categoría: {produ['categoria']} | Precio: ${produ['precio']} | Stock: {produ['stock']}")


def mostrar_empleado(lista):
    if not lista:
        print("No se encontro el empleado")
        return
    print("\n ======== Rsultado ========")
    for emple in lista:
        print(f"ID: {str(emple['id'])}| Nombre: {emple['nombre']}| Departamento: {emple['departamento']}| Salario: ${emple['salario']}| Estado: {emple['activo']}")

if __name__ == "__main__":
    menu_principal()
