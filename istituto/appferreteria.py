import tkinter as tk
from tkinter import ttk, messagebox

# Datos de ejemplo para productos de ferretería
productos = [
    {"tipo": "Martillo", "marca": "Stanley", "color": "Amarillo", "precio": 15.0, "stock": 20},
    {"tipo": "Destornillador", "marca": "Philips", "color": "Negro", "precio": 5.0, "stock": 50},
    {"tipo": "Taladro", "marca": "Bosch", "color": "Verde", "precio": 100.0, "stock": 10},
]

# Ventana principal
window = tk.Tk()
window.title("Gestión de inventario de ferretería")
window.geometry("600x400")

# Funciones para manejar productos

def actualizar_lista_productos(filtro=""):
    for row in tree.get_children():
        tree.delete(row)
    found = False
    for producto in productos:
        if filtro.lower() in producto["tipo"].lower() or filtro.lower() in producto["marca"].lower():
            tree.insert("", tk.END, values=(producto["tipo"], producto["marca"], producto["color"], producto["precio"], producto["stock"]))
            found = True
    if not found and filtro:
        messagebox.showwarning("Advertencia", "False")

def agregar_producto():
    def guardar_nuevo_producto():
        nuevo_producto = {
            "tipo": tipo_entry.get().strip(),
            "marca": marca_entry.get().strip(),
            "color": color_entry.get().strip(),
            "precio": float(precio_entry.get()),
            "stock": int(stock_entry.get())
        }
        productos.append(nuevo_producto)
        actualizar_lista_productos()
        ventana_nuevo_producto.destroy()

    ventana_nuevo_producto = tk.Toplevel(window)
    ventana_nuevo_producto.title("Agregar nuevo producto")

    tipo_label = tk.Label(ventana_nuevo_producto, text="Tipo de producto:")
    tipo_entry = tk.Entry(ventana_nuevo_producto)

    marca_label = tk.Label(ventana_nuevo_producto, text="Marca:")
    marca_entry = tk.Entry(ventana_nuevo_producto)

    color_label = tk.Label(ventana_nuevo_producto, text="Color:")
    color_entry = tk.Entry(ventana_nuevo_producto)

    precio_label = tk.Label(ventana_nuevo_producto, text="Precio:")
    precio_entry = tk.Entry(ventana_nuevo_producto)

    stock_label = tk.Label(ventana_nuevo_producto, text="Stock:")
    stock_entry = tk.Entry(ventana_nuevo_producto)

    guardar_button = tk.Button(ventana_nuevo_producto, text="Guardar", command=guardar_nuevo_producto)

    tipo_label.grid(row=0, column=0, padx=5, pady=5)
    tipo_entry.grid(row=0, column=1, padx=5, pady=5)

    marca_label.grid(row=1, column=0, padx=5, pady=5)
    marca_entry.grid(row=1, column=1, padx=5, pady=5)

    color_label.grid(row=2, column=0, padx=5, pady=5)
    color_entry.grid(row=2, column=1, padx=5, pady=5)

    precio_label.grid(row=3, column=0, padx=5, pady=5)
    precio_entry.grid(row=3, column=1, padx=5, pady=5)

    stock_label.grid(row=4, column=0, padx=5, pady=5)
    stock_entry.grid(row=4, column=1, padx=5, pady=5)

    guardar_button.grid(row=5, column=1, padx=5, pady=5)

    ventana_nuevo_producto.mainloop()

# Crear tabla de productos
columns = ("tipo", "marca", "color", "precio", "stock")
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading("tipo", text="Tipo")
tree.heading("marca", text="Marca")
tree.heading("color", text="Color")
tree.heading("precio", text="Precio")
tree.heading("stock", text="Stock")
tree.pack(fill=tk.BOTH, expand=True)

# Función de búsqueda
def buscar_producto():
    filtro = search_entry.get().strip()
    actualizar_lista_productos(filtro)

# Campo y botón de búsqueda
search_frame = tk.Frame(window)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Buscar:")
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Buscar", command=buscar_producto)
search_button.pack(side=tk.LEFT, padx=5)

# Botón para agregar producto
add_button = tk.Button(window, text="Agregar producto", command=agregar_producto)
add_button.pack(pady=10)

# Actualizar la lista de productos al iniciar
actualizar_lista_productos()

window.mainloop()
