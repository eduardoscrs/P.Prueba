import tkinter as tk

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
    
    def create_input_widgets(self):
        input_label = tk.Label(self.window, text="Ingrese números (separados por espacios):")
        input_label.pack()

        self.input_entry = tk.Entry(self.window)
        self.input_entry.pack()

        add_button = tk.Button(self.window, text="Agregar números", command=self.add_numbers)
        add_button.pack()

    def create_sorting_widgets(self):
        sort_button = tk.Button(self.window, text="Iniciar Ordenamiento", command=self.start_sort)
        sort_button.pack()

    def create_search_widgets(self):
        search_label = tk.Label(self.window, text="Ingrese el número a buscar:")
        search_label.pack()

        self.search_entry = tk.Entry(self.window)
        self.search_entry.pack()

        search_button = tk.Button(self.window, text="Buscar", command=self.binary_search)
        search_button.pack()

        self.search_result_label = tk.Label(self.window, text="")
        self.search_result_label.pack()

    def add_numbers(self):
        user_input = self.input_entry.get()
        numbers = user_input.split()
        for num in numbers:
            if num.strip().isdigit():
                self.lista.append(int(num.strip()))
        self.update_display()
        self.input_entry.delete(0, "end")

    def start_sort(self):
        self.bubble_sort()

    def update_display(self):
        self.canvas.delete("all")
        num_elements = len(self.lista)
        self.canvas.config(width=num_elements * (self.element_width + self.spacing) + 20)
        x = 20
        for num in self.lista:
            self.canvas.create_rectangle(x, 150, x + self.element_width, 150 - num * 5, fill="blue")
            self.canvas.create_text(x + self.element_width / 2, 160, text=str(num))
            x += self.element_width + self.spacing
        self.window.update()

    def bubble_sort(self):
        n = len(self.lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.lista[j] > self.lista[j+1]:
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
                    self.update_display()
                    self.window.after(100)
    
    def binary_search(self):
        search_value = int(self.search_entry.get())
        result = self.busq_binaria_animacion(search_value)
        if result != -1:
            self.search_result_label.config(text=f"El número {search_value} se encuentra en la posición {result}.")
        else:
            self.search_result_label.config(text=f"El número {search_value} no se encontró en la lista.")

    def busq_binaria_animacion(self, x):
        izq = 0
        der = len(self.lista) - 1
        while izq <= der:
            medio = (izq + der) // 2
            self.highlight_middle(medio)
            self.update_display()
            self.window.after(500)
            if self.lista[medio] == x:
                self.clear_highlights()
                return medio
            elif self.lista[medio] > x:
                self.clear_highlights()
                der = medio - 1
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

if __name__ == "__main__":
    window = tk.Tk()
    app = NumberVisualizer(window)
    window.mainloop()
