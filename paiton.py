import tkinter as tk

# Función para agregar números a la lista y actualizar la visualización
def add_numbers():
    user_input = input_entry.get()
    numbers = user_input.split()
    for num in numbers:
        if num.strip().isdigit():
            lista.append(int(num.strip()))
    update_display()
    input_entry.delete(0, "end")

# Función para iniciar el ordenamiento
def start_sort():
    bubble_sort(lista)

# Función para actualizar la visualización
def update_display():
    canvas.delete("all")
    num_elements = len(lista)
    element_width = 20
    spacing = 5  # Espacio entre los elementos
    canvas.config(width=num_elements * (element_width + spacing) + 20)  # Ajustar el ancho del lienzo
    x = 20
    for num in lista:
        canvas.create_rectangle(x, 150, x + element_width, 150 - num * 5, fill="blue")
        canvas.create_text(x + element_width / 2, 160, text=str(num))
        x += element_width + spacing
    window.update()

# Función para ordenar con el algoritmo de burbuja
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                update_display()
                window.after(100)  # Pequeña pausa para visualización

# Función para buscar con el algoritmo de búsqueda binaria con animación
def binary_search():
    search_value = int(search_entry.get())
    result = busq_binaria_animacion(lista, search_value)
    if result != -1:
        search_result_label.config(text=f"El número {search_value} se encuentra en la posición {result}.")
    else:
        search_result_label.config(text=f"El número {search_value} no se encontró en la lista.")

# Función para realizar una búsqueda binaria con animación
def busq_binaria_animacion(lista, x):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        highlight_middle(medio)  # Destacar el elemento medio
        update_display()
        window.after(500)  # Pequeña pausa para la animación
        if lista[medio] == x:
            clear_highlights()
            return medio
        elif lista[medio] > x:
            clear_highlights()
            der = medio - 1
        else:
            clear_highlights()
            izq = medio + 1
    clear_highlights()
    return -1

# Función para destacar el elemento medio
def highlight_middle(medio):
    x = 20 + medio * (element_width + spacing)
    canvas.create_rectangle(x, 150, x + element_width, 150 - lista[medio] * 5, fill="red")
    canvas.create_text(x + element_width / 2, 160, text=str(lista[medio]))

# Función para borrar todos los resaltados
def clear_highlights():
    canvas.delete("red")

# Crear una ventana
window = tk.Tk()
window.title("Ordenamiento y Búsqueda")

# Crear un lienzo para dibujar
canvas = tk.Canvas(window, height=200)
canvas.pack()

# Crear una entrada para que el usuario ingrese números
input_label = tk.Label(window, text="Ingrese números (separados por espacios):")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

# Botón para agregar los números
add_button = tk.Button(window, text="Agregar números", command=add_numbers)
add_button.pack()

# Botón para iniciar el ordenamiento
sort_button = tk.Button(window, text="Iniciar Ordenamiento", command=start_sort)
sort_button.pack()

# Entrada para la búsqueda binaria
search_label = tk.Label(window, text="Ingrese el número a buscar:")
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

# Botón para realizar la búsqueda binaria
search_button = tk.Button(window, text="Buscar", command=binary_search)
search_button.pack()

# Etiqueta para mostrar el resultado de la búsqueda binaria
search_result_label = tk.Label(window, text="")
search_result_label.pack()

# Lista de números
lista = []
element_width = 20
spacing = 5  # Espacio entre los elementos

# Cerrar la ventana al hacer clic en la "X"
window.protocol("WM_DELETE_WINDOW", window.quit)

# Ejecutar la ventana
window.mainloop()
