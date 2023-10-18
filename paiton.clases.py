import tkinter as tk
from tkinter import messagebox

class NumberVisualizer:
    def __init__(self, window):
        self.window = window
        self.window.title("Ordenamiento y Búsqueda")

        self.lista = []
        self.element_width = 20
        self.spacing = 5

        self.canvas = tk.Canvas(self.window, height=200)
        self.canvas.pack()

        self.create_input_widgets()
        self.create_sorting_widgets()
        self.create_search_widgets()

        self.window.protocol("WM_DELETE_WINDOW", self.window.quit)
    
    #* Función para crear los widgets de entrada
    def create_input_widgets(self):
        input_label = tk.Label(self.window, text="Ingrese números (separados por espacios):")
        input_label.pack()

        self.input_entry = tk.Entry(self.window)
        self.input_entry.pack()

        add_button = tk.Button(self.window, text="Agregar números", command=self.add_numbers)
        add_button.pack()

        clear_button = tk.Button(self.window, text="Limpiar Lista", command=self.clear_list)
        clear_button.pack()
        
    #* Función para crear los widgets de ordenamiento
    def create_sorting_widgets(self):
        sort_button = tk.Button(self.window, text="Iniciar Ordenamiento", command=self.start_sort)
        sort_button.pack()
        
    #* Función para crear los widgets de búsqueda
    def create_search_widgets(self):
        search_label = tk.Label(self.window, text="Ingrese el número a buscar:")
        search_label.pack()
        # Entrada para la búsqueda binaria
        self.search_entry = tk.Entry(self.window)
        self.search_entry.pack()
        # Botón para realizar la búsqueda binaria
        search_button = tk.Button(self.window, text="Buscar", command=self.binary_search)
        search_button.pack()
        # Etiqueta para mostrar el resultado de la búsqueda binaria
        self.search_result_label = tk.Label(self.window, text="")
        self.search_result_label.pack()

    #* Función para agregar los números ingresados por el usuario a la lista de números a ordenar y mostrarlos en el lienzo
    def add_numbers(self):
        user_input = self.input_entry.get()
        if self.validate_input(user_input):
            numbers = user_input.split()
            for num in numbers:
                self.lista.append(int(num.strip()))
            self.update_display()
            self.input_entry.delete(0, "end")
        else:
            tk.messagebox.showerror("Error", "Ingrese números enteros separados por espacios.")

    def validate_input(self, input_str):
        # Verificar si la cadena contiene solo números enteros separados por espacios
        return all(num.strip().isdigit() for num in input_str.split())
    
    def clear_list(self):
        self.lista = []
        self.update_display()
   

    #* Función para iniciar el ordenamiento
    def start_sort(self):
        # Ordenar la lista usando el algoritmo de ordenamiento burbuja
        self.bubble_sort()

    #* Función para actualizar el lienzo
    def update_display(self):
        # Borrar todo lo que hay en el lienzo
        self.canvas.delete("all")
        # Dibujar los elementos de la lista
        num_elements = len(self.lista)
        # Ajustar el tamaño del lienzo según la cantidad de elementos
        self.canvas.config(width=num_elements * (self.element_width + self.spacing) + 20)
        # Dibujar los elementos
        x = 20
        # Dibujar los elementos de la lista
        for num in self.lista:
            self.canvas.create_rectangle(x, 150, x + self.element_width, 150 - num * 5, fill="blue")
            self.canvas.create_text(x + self.element_width / 2, 160, text=str(num))
            x += self.element_width + self.spacing
        self.window.update()

    #* Función para ordenar la lista usando el algoritmo de ordenamiento burbuja
    def bubble_sort(self):
        for i in range(1, len(self.lista)):
            key = self.lista[i]
            j = i - 1
            while j >= 0 and key < self.lista[j]:
                self.lista[j + 1] = self.lista[j]
                j -= 1
                self.update_display()
                self.window.after(100)
            self.lista[j + 1] = key
        self.update_display()

    
    #* Función para realizar una búsqueda binaria con animación
    def binary_search(self):
        # Obtener el valor a buscar
        search_value = int(self.search_entry.get())
        # Realizar la búsqueda binaria
        result = self.busq_binaria_animacion(search_value)
        # Mostrar el resultado de la búsqueda
        if result != -1:
            self.search_result_label.config(text=f"El número {search_value} se encuentra en la posición {result}.")
        else:
            self.search_result_label.config(text=f"El número {search_value} no se encontró en la lista.")

    #* Función para realizar una búsqueda binaria con animación
    def busq_binaria_animacion(self, x):
        # Inicializar los índices izquierdo y derecho
        izq = 0
        der = len(self.lista) - 1
        # Mientras el índice izquierdo sea menor o igual al índice derecho
        while izq <= der:
            # Calcular el índice medio
            medio = (izq + der) // 2
            # Destacar el elemento medio
            self.highlight_middle(medio)
            # Actualizar el lienzo
            self.update_display()
            # Pequeña pausa para la animación
            self.window.after(500)
            # Si el elemento medio es el valor buscado, retornar el índice medio
            if self.lista[medio] == x:
                self.clear_highlights()
                return medio
            # Si el elemento medio es mayor que el valor buscado, actualizar el índice derecho
            elif self.lista[medio] > x:
                self.clear_highlights()
                der = medio - 1
            # Si el elemento medio es menor que el valor buscado, actualizar el índice izquierdo
            else:
                self.clear_highlights()
                izq = medio + 1
        self.clear_highlights()
        return -1

    def highlight_middle(self, medio):
        x = 20 + medio * (self.element_width + self.spacing)
        self.canvas.create_rectangle(x, 150, x + self.element_width, 150 - self.lista[medio] * 5, fill="red")
        self.canvas.create_text(x + self.element_width / 2, 160, text=str(self.lista[medio]))

    def clear_highlights(self):
        self.canvas.delete("red")

#* Crear la ventana principal
if __name__ == "__main__":
    window = tk.Tk()
    app = NumberVisualizer(window)
    window.mainloop()
