import tkinter as tk
from tkinter import messagebox

class Main_Ordenamiento:
    def __init__(self, window):
        self.window = window
        self.window.title("Ordenamiento y Búsqueda")

        self.lista = []
        # Ancho de cada elemento de la lista
        self.element_width = 10
        # Espacio entre cada elemento de la lista
        self.spacing = 5

        # Crear el lienzo
        self.canvas = tk.Canvas(self.window, height=200)
        # Empaquetar el lienzo
        self.canvas.pack()

        self.widget_entrada()
        self.widget_ordenar()
        self.widget_busqueda()

        self.window.protocol("WM_DELETE_WINDOW", self.window.quit)
    
    #* Función para crear los widgets de entrada
    def widget_entrada(self):
        input_label = tk.Label(self.window, text="Ingrese números (separados por espacios):")
        input_label.pack()

        self.input_entrada = tk.Entry(self.window)
        self.input_entrada.pack()

        add_button = tk.Button(self.window, text="Agregar números", command=self.agregar_num)
        add_button.pack()

        clear_button = tk.Button(self.window, text="Limpiar Lista", command=self.clear_list)
        clear_button.pack()
        
    #* Función para crear los widgets de ordenamiento
    def widget_ordenar(self):
        sort_button = tk.Button(self.window, text="Iniciar Ordenamiento", command=self.ordernar)
        sort_button.pack()
        
    #* Función para crear los widgets de búsqueda
    def widget_busqueda(self):
        search_label = tk.Label(self.window, text="Ingrese el número a buscar:")
        search_label.pack()
        # Entrada para la búsqueda binaria
        self.search_entry = tk.Entry(self.window)
        self.search_entry.pack()
        # Botón para realizar la búsqueda binaria
        search_button = tk.Button(self.window, text="Buscar", command=self.busq_bin)
        search_button.pack()
        # Etiqueta para mostrar el resultado de la búsqueda binaria
        self.search_result_label = tk.Label(self.window, text="")
        self.search_result_label.pack()

    #* Función para agregar los números ingresados por el usuario a la lista de números a ordenar y mostrarlos en el lienzo
    def agregar_num(self):
        input_usuario = self.input_entrada.get()
        if self.validate_input(input_usuario):
            numeros = input_usuario.split()
            for num in numeros:
                self.lista.append(int(num.strip()))
            self.actualizar_ventana()
            self.input_entrada.delete(0, "end")
        else:
            tk.messagebox.showerror("Error", "Ingrese números enteros separados por espacios.")

    def validate_input(self, input_str):
        # Verificar si la cadena contiene solo números enteros separados por espacios
        return all(num.strip().isdigit() for num in input_str.split())
    
    def clear_list(self):
        self.lista = []
        self.actualizar_ventana()
   

    #* Función para iniciar el ordenamiento
    def ordernar(self):
        # Ordenar la lista usando el algoritmo de ordenamiento burbuja
        self.insertion_sort()

    #* Función para actualizar el lienzo
    def actualizar_ventana(self):
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

    #* Función para ordenar la lista usando el algoritmo de ordenamiento por inserción
    def insertion_sort(self):
        for i in range(1, len(self.lista)):
            temp = self.lista[i]
            j = i - 1
            while j >= 0 and temp < self.lista[j]:
                self.lista[j + 1] = self.lista[j]
                j -= 1
                self.actualizar_ventana()
                self.window.after(100)
            self.lista[j + 1] = temp
        self.actualizar_ventana()

    
    #* Función para realizar una búsqueda binaria con animación
    def busq_bin(self):
        # Obtener el valor a buscar
        objetivo = int(self.search_entry.get())
        # Realizar la búsqueda binaria
        result = self.busq_binaria_animacion(objetivo)
        # Mostrar el resultado de la búsqueda
        if result != -1:
            self.search_result_label.config(text=f"El número {objetivo} se encuentra en la posición {result}.")
        else:
            self.search_result_label.config(text=f"El número {objetivo} no se encontró en la lista.")

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
            self.actualizar_ventana()
            # Pequeña pausa para la animación
            self.window.after(150)
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
        self.canvas.create_rectangle(x, 150, x + self.element_width, 150 - self.lista[medio] * 5, fill="green")
        self.canvas.create_text(x + self.element_width / 2, 160, text=str(self.lista[medio]))

    def clear_highlights(self):
        self.canvas.delete("red")

#* Crear la ventana principal


        
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("1000x500")
    app = Main_Ordenamiento(window)
    window.mainloop()
