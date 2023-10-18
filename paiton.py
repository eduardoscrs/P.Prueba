def bus_bin(lista, x):
    izq = 0
    der = len(lista) - 1
    iteracion = 0  # Variable para llevar un registro del número de iteraciones
    
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            print(f"Elemento {x} encontrado en la posición {medio} después de {iteracion} iteraciones.")
            return medio
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
        iteracion += 1  # Incrementa el contador de iteraciones en cada ciclo
        
        # Agrega una impresión para mostrar la información de la iteración actual
        print(f"Iteración {iteracion}: izq = {izq}, der = {der}, medio = {medio}, x = {x}")
    
    print(f"Elemento {x} no encontrado después de {iteracion} iteraciones.")
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bus_bin(lista, 10))
