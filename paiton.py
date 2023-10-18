def insertsort(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and temp < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = temp

        # Imprimir el estado de la lista en cada iteración
        print(f"Iteración {i}: {lista}")

    return lista


lista = [1, 5, 3, 2, 4, 3, 4, 5, 12, 11, 10, 9, 8, 7, 6]

print(insertsort(lista))                
                
                