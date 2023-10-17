import tkinter as tk

# Función para agregar números a la lista y actualizar la visualización
def add_numbers():
    user_input = input_entry.get()
    numbers = user_input.split()
    for num in numbers:
        if num.strip().isdigit():
            arr.append(int(num.strip()))
    update_display()
    input_entry.delete(0, "end")

# Función para iniciar el ordenamiento
def start_sort():
    bubble_sort(arr)

# Función para actualizar la visualización
def update_display():
    canvas.delete("all")
    x = 20
    for num in arr:
        canvas.create_rectangle(x, 150, x + 20, 150 - num * 5, fill="blue")
        x += 25
    window.update()

# Función para ordenar con el algoritmo de burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_display()
                window.after(100)  # Pequeña pausa para visualización

# Crear una ventana
window = tk.Tk()
window.title("Bubble Sort Visualization")

# Crear un lienzo para dibujar
canvas = tk.Canvas(window, width=400, height=200)
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

# Lista de números
arr = []

# Cerrar la ventana al hacer clic en la "X"
window.protocol("WM_DELETE_WINDOW", window.quit)

# Ejecutar la ventana
window.mainloop()
