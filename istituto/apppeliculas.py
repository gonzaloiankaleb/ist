import tkinter as tk
from tkinter import messagebox

# Estructura de datos para las películas
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010, "actor": "Leonardo DiCaprio"},
    {"title": "The Matrix", "genre": "Sci-Fi", "year": 1999, "actor": "Keanu Reeves"},
    {"title": "Titanic", "genre": "Romance", "year": 1997, "actor": "Leonardo DiCaprio"},
    {"title": "Troya", "genre": "accion", "year": 2014, "actor": "brad pitt"}
]

def add_movie():
    title = entry_title.get()
    genre = entry_genre.get()
    year = entry_year.get()
    actor = entry_actor.get()

    if title and genre and year and actor:
        new_movie = {"title": title, "genre": genre, "year": int(year), "actor": actor}
        movies.append(new_movie)
        messagebox.showinfo("Éxito", "Película añadida correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

def search_movie():
    genre = entry_search_genre.get()
    year = entry_search_year.get()
    actor = entry_search_actor.get()

    filtered_movies = [
        movie for movie in movies
        if (not genre or movie["genre"] == genre) and
           (not year or movie["year"] == int(year)) and
           (not actor or movie["actor"] == actor)
    ]

    if filtered_movies:
        result = "\n".join([movie["title"] for movie in filtered_movies])
        messagebox.showinfo("Películas encontradas", result)
    else:
        messagebox.showinfo("Sin resultados", "False")

# Configuración de la ventana principal
root = tk.Tk()
root.geometry("400x400")
root.resizable(False, False)
root.title("Gestor de Películas")

# Entradas para añadir una nueva película
frame_add = tk.Frame(root)
frame_add.pack(pady=10)

tk.Label(frame_add, text="Añadir Película").grid(row=0, columnspan=2)

tk.Label(frame_add, text="Título:").grid(row=1, column=0)
entry_title = tk.Entry(frame_add)
entry_title.grid(row=1, column=1)

tk.Label(frame_add, text="Género:").grid(row=2, column=0)
entry_genre = tk.Entry(frame_add)
entry_genre.grid(row=2, column=1)

tk.Label(frame_add, text="Año:").grid(row=3, column=0)
entry_year = tk.Entry(frame_add)
entry_year.grid(row=3, column=1)

tk.Label(frame_add, text="Actor:").grid(row=4, column=0)
entry_actor = tk.Entry(frame_add)
entry_actor.grid(row=4, column=1)

btn_add_movie = tk.Button(frame_add, text="Añadir", command=add_movie)
btn_add_movie.grid(row=5, columnspan=2, pady=10)

# Entradas para buscar una película
frame_search = tk.Frame(root)
frame_search.pack(pady=10)

tk.Label(frame_search, text="Buscar Película").grid(row=0, columnspan=2)

tk.Label(frame_search, text="Género:").grid(row=1, column=0)
entry_search_genre = tk.Entry(frame_search)
entry_search_genre.grid(row=1, column=1)

tk.Label(frame_search, text="Año:").grid(row=2, column=0)
entry_search_year = tk.Entry(frame_search)
entry_search_year.grid(row=2, column=1)

tk.Label(frame_search, text="Actor:").grid(row=3, column=0)
entry_search_actor = tk.Entry(frame_search)
entry_search_actor.grid(row=3, column=1)

btn_search_movie = tk.Button(frame_search, text="Buscar", command=search_movie)
btn_search_movie.grid(row=4, columnspan=2, pady=10)

root.mainloop()
