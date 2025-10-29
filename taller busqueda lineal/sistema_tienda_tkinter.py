from tkinter import * #impota la libreria tkinter de manera global
from tkinter import ttk, messagebox #importa messagebox para las ventanas emerjentes y ttk para los estilos
from funciones_de_busqueda import * #aqui se importa globalmente o totalmente el archivo de funciones_de busqueda
from datos_ejemplo import empleados, productos #se importan los datos de ejemplo


#============== funciones de las interfaces ==============

#tree se usa mas adelante para creear y administrar la tabla donde van los resultados
def mostrar_productos(resultado, tree):
    for item in tree.get_children():
        tree.delete(item)

    #se normaliza el resultado para que siempre devuelva listas, esto para que no ocurran errores al leer diccionarios u otros
    if resultado is None:
        lista = []
    elif isinstance(resultado, dict):
        lista = [resultado]
    elif isinstance(resultado, list):
        lista = resultado
    else:
        lista = []

    if not lista:
        messagebox.showinfo("Sin resultados", "No se encontraron productos.")
        return

    for produ in lista:
        tree.insert(
            "",
            "end",
            values=(
                produ["id"],
                produ["nombre"],
                produ["marca"],
                produ["categoria"],
                produ["precio"],
                produ["stock"],
            ),
        )


def mostrar_empleado(resultado, tree):
    for item in tree.get_children():
        tree.delete(item)

    if resultado is None:
        lista = []
    elif isinstance(resultado, dict):
        lista = [resultado]
    elif isinstance(resultado, list):
        lista = resultado
    else:
        lista = []

    if not lista:
        messagebox.showinfo("Sin resultados", "No se encontraron empleados.")
        return

    for emple in lista:
        tree.insert(
            "",
            "end",
            values=(
                emple["id"],
                emple["nombre"],
                emple["apellido"],
                emple["departamento"],
                emple["salario"],
                emple["activo"],
            ),
        )


#============== interfaz principal ==============

def interfaz_principal():
    interfaz = Tk() #tk crea la ventana
    interfaz.title("Sistema de tienda electronica") #title sirve para poner nombre a la ventana
    interfaz.geometry("950x600") #tamaño de la ventana
    interfaz.config(bg="black") #color de la ventana

    #========== opciones ==========

    frame_opciones = Frame(interfaz, bg="black") #crea un espacio en la ventana
    frame_opciones.pack(fill=BOTH, expand=True)#centrar y expandir el frame

    Label(frame_opciones, text="Menú principal", bg="black",fg="white", font=("Arial", 22, "bold")).pack(pady=0) 

    # creacion de los botones de eleccion de busqueda y salida
    # "comand = lambda ...... sirve para dar un comando a cumplir a cada boton"
    Button(frame_opciones, text="Buscar Productos",bg="light blue", fg="black", font=("Arial", 12, "bold"), height=5, width=40, command=lambda: mostrar_menu_productos(interfaz)).pack(pady=15) 
    Button(frame_opciones, text="Buscar Empleados",bg="light blue", fg="black",font=("Arial", 12, "bold"), height=5, width=40, command=lambda: mostrar_menu_empleados(interfaz)).pack(pady=15)
    Button(frame_opciones, text="Salir",bg="light green", fg="black",font=("Arial", 12, "bold"),width=40, command=interfaz.destroy).pack(pady=10) #interfaz.destroy destruye la interfaz y cierra el programa

    #pie de pagina (por lo general se usa para mostrar derechos o el nombre del creador/dueño)
    Label(frame_opciones, text="@TechStore Sistem", bg="black", fg="white").pack(side=BOTTOM, pady=10)

    interfaz.mainloop() #llamada de la funcion


#============== submenús ==============

def mostrar_menu_productos(interfaz):
    win = Toplevel(interfaz) #toplevel sirve para crear otra ventana o subpantalla
    win.title("Buscar Productos")
    win.geometry("900x600")

    Label(win, text="Menú para buscar productos", font=("Arial", 12, "bold")).pack(pady=10)

    frame_busqueda = Frame(win)
    frame_busqueda.pack(pady=10)

#diccionaio para elejir opciones
    opciones = [
        "Por nombre",
        "Por ID",
        "Por categoría",
        "Por disponibilidad",
        "Por rango de precio",
        "Por marca",
        "Contar por categoría",
    ]

#caja de opciones con estilo cortina vertical
    combo = ttk.Combobox(frame_busqueda, values=opciones, state="readonly", width=30)
    combo.current(0)
    combo.grid(row=0, column=0, padx=5, pady=5)
    entry1 = Entry(frame_busqueda)              #entry es la caja donde el usuario escribe
    entry2 = Entry(frame_busqueda)
    entry1.grid(row=0, column=1, padx=5, pady=5)

#permite cambiar las opciones o capmos
    def actualizar_campos(event=None):
        for w in (entry1, entry2):
            w.grid_forget()
        tipo = combo.get()
        if tipo in ["Por nombre", "Por ID", "Por categoría", "Por marca", "Contar por categoría"]: #en estas solo pone una caja de entrada ya que solo es nesesaria 1
            entry1.grid(row=0, column=1, padx=5, pady=5)
            entry1.delete(0, END)
        elif tipo == "Por rango de precio": #en esta parte agrega otra caja de entrada donde el usuario ingresa datos
            entry1.grid(row=0, column=1, padx=5, pady=5)
            entry2.grid(row=0, column=2, padx=5, pady=5)
            entry1.delete(0, END)
            entry2.delete(0, END)
    combo.bind("<<ComboboxSelected>>", actualizar_campos)

    # Treeview o espacio para ver las respuestas con estilo hoja de excel
    # tree crea un panel o tabla con filas y columnas, tipo exel o ventana de tareas
    cols = ("ID", "Nombre", "Marca", "Categoría", "Precio", "Stock")
    tree = ttk.Treeview(win, columns=cols, show="headings", height=15)
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=130)
    tree.pack(expand=True, fill=BOTH, padx=10, pady=10)

    # función de búsqueda
    #manejo de errores try-except para evitar bloqueos
    #se usa if,elif y else para las elecciones del usuario,
    #ademas de que le dice o define como debe ser cada funcion, con int o float o por el contrario si debe llevar 1 o 2 cajas de entrad de texto
    def buscar():
        tipo = combo.get()
        try:
            if tipo == "Por nombre":
                r = buscar_nombre(productos, entry1.get())
            elif tipo == "Por ID":
                r = buscar_ID(productos, int(entry1.get()))
            elif tipo == "Por categoría":
                r = buscar_categoria(productos, entry1.get())
            elif tipo == "Por disponibilidad":
                r = buscar_disponivilidad(productos)
            elif tipo == "Por rango de precio":
                precio_min = float(entry1.get())
                precio_max = float(entry2.get())

                # manejo de error de entrada: si el mínimo es mayor que el máximo, se muestra advertencia
                if precio_min > precio_max:
                    messagebox.showerror("Error", "El precio mínimo no puede ser mayor que el precio máximo.")
                    return

                # si está correcto, ejecuta la búsqueda normalmente
                r = rango_preci(productos, precio_min, precio_max)

            elif tipo == "Por marca":
                r = buscar_marca(productos, entry1.get())
            elif tipo == "Contar por categoría":
                cantidad = cont_prod_cat(productos, entry1.get())
                messagebox.showinfo("Cantidad", f"Se encontraron {cantidad} productos en '{entry1.get()}'")
                return
            else:
                r = None
            mostrar_productos(r, tree)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.") #ventana emergente para mostrar errores

    Button(win, text="Buscar", width=20, command=buscar).pack(pady=5) #boton para buscar, ejecuta  una opcion



def mostrar_menu_empleados(interfaz):
    win = Toplevel(interfaz) #toplevel sirve para crear otra ventana o subpantalla
    win.title("Buscar Empleados")
    win.geometry("900x600")

    Label(win, text="Menú para buscar empleados", font=("Arial", 12, "bold")).pack(pady=10)

    frame_busqueda = Frame(win)
    frame_busqueda.pack(pady=10)

    opciones = [
        "Por nombre",
        "Por departamento",
        "Por estado activo",
    ]
    combo = ttk.Combobox(frame_busqueda, values=opciones, state="readonly", width=30)
    combo.current(0)
    combo.grid(row=0, column=0, padx=5, pady=5)

    entry1 = Entry(frame_busqueda)
    entry2 = Entry(frame_busqueda)
    entry1.grid(row=0, column=1, padx=5, pady=5)
    entry2.grid(row=0, column=2, padx=5, pady=5)

    def actualizar_campos(event=None):
        for w in (entry1, entry2):
            w.grid_forget()
        tipo = combo.get()
        if tipo == "Por nombre":
            entry1.grid(row=0, column=1, padx=5, pady=5)
            entry2.grid(row=0, column=2, padx=5, pady=5)
            entry1.delete(0, END)
            entry2.delete(0, END)
        elif tipo == "Por departamento":
            entry1.grid(row=0, column=1, padx=5, pady=5)
            entry1.delete(0, END)
        # como estado "activo", no requiere nada para ingresar datos se deja asi
    combo.bind("<<ComboboxSelected>>", actualizar_campos)

    cols = ("ID", "Nombre", "Apellido", "Departamento", "Salario", "Activo")
    tree = ttk.Treeview(win, columns=cols, show="headings", height=15)
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=130)
    tree.pack(expand=True, fill=BOTH, padx=10, pady=10)

    def buscar():
        tipo = combo.get()
        try:
            if tipo == "Por nombre":
                r = buscar_nombre_emple(empleados, entry1.get(), entry2.get())
            elif tipo == "Por departamento":
                r = buscar_departamento(empleados, entry1.get())
            elif tipo == "Por estado activo":
                r = buscar_empleado_act(empleados)
            else:
                r = None
            mostrar_empleado(r, tree)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(win, text="Buscar", width=20, command=buscar).pack(pady=5)


#============== ejecución del main ==============
if __name__ == "__main__":
    interfaz_principal()
