# Sistema de tienda electronica - TechStore

Este proyecto implementa un sistema de busqueda lineal aplicado a una simulacion de una tienda electronica.
Permite buscar productos o empleados desde una **version de consola** y otra **version con interfaz grafica tkinter**.

==== contenido del taller TechStore ======
- archivo **sistema_tienda_terminal.py** es la version del sistema de tienda electronica, ejecuable desde la terminal/consola. 
  este incluye los menus y las funciones de impresion.
- archivo **sistema_tienda_tkinter.py** es la version del sistema de tienda electronica, ejecutable con una interfaz grafica en tkinter.
  cuenta con manejo de errores de entrada de usuario, funciones.
- archivo **datos_ejemplo.py** contiene los datos o la lista de empleados y prductos.
- archivo **funciones_de_busqueda.py** contiene las funciones de busqueda lineal que permiten realizar las busquedas en productos o empleados.
- archivo **README.md** documentacion del proyecto

El sistema TechStore se ejecuta principalmente desde el archivo **sistema_tienda_terminal.py** o **sistema_tienda_tkinter.py** dependiendo como se desea ejecutar, con interfaz o en terminal, en este archivo se hacen importaciones de otros achivos que permie el funcionamiento de la tienda, es decir se toman los datos de **funciones_de_busqueda.py** y los **datos_ejemplo.py** y se importan este, creando la tienda.

======= Funcionamiento del sistema =========

El programa utiliza **busqueda lineal** recorriendo las listas de productos o empleados hasta encontrar la coincidencia.
Dependiendo el modo: 

**sistema_tienda_tkinter.py** 
  -ventana principal, que permite al usuario elejir entre, buscar productos, empleados o salir.
  -submenus con menus desplegables con estilo cortina vertical(combobox) para elejir el tipo de busqueda.
  -resultados que se muestran en una tabla con estilo de excel (treeview)
  -incluye manejo de errores try-except (valores no validos, campos vacios o precios invertidos)

**sistema_tienda_terminal.py**
  -se navega desde la terminal mediante menus numericos, donde el usuario elije introduciendo el numero correspondiente  cada opcion.
  -El usuario elije el tipo de busqueda elijiendo el menu (productos o empleados) y los submenus con cada funcion de busqueda.
  -los resultados se muestran en la terminal o consola de manera simple.


==== requisitos para ejecutar el sistema ======
  - python 3.10 o superior
  - librerias correctamente importadas (ya estan en el codigo)
  - se deben tener todos los archivos en la misma carpeta para que la importacion de los mismos en el archivo principal **sistema_tienda_terminal.py** o **sistema_tienda_tkinter.py** funcione y no genere errores.











