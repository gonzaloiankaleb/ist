import tkinter as tk
from tkinter import ttk, messagebox

# Datos de ejemplo para prendas
prendas = [
    {"tipo": "Camisa", "talle": "M", "color": "Azul", "precio": 50.0, "stock": 10},
    {"tipo": "Pantalón", "talle": "L", "color": "Negro", "precio": 75.0, "stock": 5},
    {"tipo": "Vestido", "talle": "S", "color": "Rojo", "precio": 120.0, "stock": 2},
]

# Ventana principal
window = tk.Tk()
window.title("Gestión de inventario de tienda de indumentaria")
window.geometry("600x400")

# Funciones para manejar prendas

def actualizar_lista_prendas(filtro=""):
    for row in tree.get_children():
        tree.delete(row)
    found = False
    for prenda in prendas:
        if filtro.lower() in prenda["tipo"].lower() or filtro.lower() in prenda["color"].lower():
            tree.insert("", tk.END, values=(prenda["tipo"], prenda["talle"], prenda["color"], prenda["precio"], prenda["stock"]))
            found = True
    if not found and filtro:
        messagebox.showwarning("Advertencia", "False")

def agregar_prenda():
    def guardar_nueva_prenda():
        nueva_prenda = {
            "tipo": tipo_entry.get().strip(),
            "talle": talle_combobox.get().strip(),
            "color": color_entry.get().strip(),
            "precio": float(precio_entry.get()),
            "stock": int(stock_entry.get())
        }
        prendas.append(nueva_prenda)
        actualizar_lista_prendas()
        ventana_nueva_prenda.destroy()

    ventana_nueva_prenda = tk.Toplevel(window)
    ventana_nueva_prenda.title("Agregar nueva prenda")

    tipo_label = tk.Label(ventana_nueva_prenda, text="Tipo de prenda:")
    tipo_entry = tk.Entry(ventana_nueva_prenda)

    talle_label = tk.Label(ventana_nueva_prenda, text="Talle:")
    talle_options = ["XS", "S", "M", "L", "XL"]
    talle_combobox = ttk.Combobox(ventana_nueva_prenda, values=talle_options)
    talle_combobox.current(0)  # Seleccionar valor predeterminado (XS)

    color_label = tk.Label(ventana_nueva_prenda, text="Color:")
    color_entry = tk.Entry(ventana_nueva_prenda)

    precio_label = tk.Label(ventana_nueva_prenda, text="Precio:")
    precio_entry = tk.Entry(ventana_nueva_prenda)

    stock_label = tk.Label(ventana_nueva_prenda, text="Stock:")
    stock_entry = tk.Entry(ventana_nueva_prenda)

    guardar_button = tk.Button(ventana_nueva_prenda, text="Guardar", command=guardar_nueva_prenda)

    tipo_label.grid(row=0, column=0, padx=5, pady=5)
    tipo_entry.grid(row=0, column=1, padx=5, pady=5)

    talle_label.grid(row=1, column=0, padx=5, pady=5)
    talle_combobox.grid(row=1, column=1, padx=5, pady=5)

    color_label.grid(row=2, column=0, padx=5, pady=5)
    color_entry.grid(row=2, column=1, padx=5, pady=5)

    precio_label.grid(row=3, column=0, padx=5, pady=5)
    precio_entry.grid(row=3, column=1, padx=5, pady=5)

    stock_label.grid(row=4, column=0, padx=5, pady=5)
    stock_entry.grid(row=4, column=1, padx=5, pady=5)

    guardar_button.grid(row=5, column=1, padx=5, pady=5)

    ventana_nueva_prenda.mainloop()

# Crear tabla de prendas
columns = ("tipo", "talle", "color", "precio", "stock")
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading("tipo", text="Tipo")
tree.heading("talle", text="Talle")
tree.heading("color", text="Color")
tree.heading("precio", text="Precio")
tree.heading("stock", text="Stock")
tree.pack(fill=tk.BOTH, expand=True)

# Función de búsqueda
def buscar_prenda():
    filtro = search_entry.get().strip()
    actualizar_lista_prendas(filtro)

# Campo y botón de búsqueda
search_frame = tk.Frame(window)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Buscar:")
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Buscar", command=buscar_prenda)
search_button.pack(side=tk.LEFT, padx=5)

# Botón para agregar prenda
add_button = tk.Button(window, text="Agregar prenda", command=agregar_prenda)
add_button.pack(pady=10)

# Actualizar la lista de prendas al iniciar
actualizar_lista_prendas()

window.mainloop()
