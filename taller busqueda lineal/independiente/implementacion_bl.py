def busqueda_lineal_simple(lista, elemento):
    for indice in range(len(lista)):
        lista[indice]

        if lista[indice] == elemento:
            return indice
    
    return -1
            
# Pruebas
numeros = [64, 34, 25, 12, 22, 11, 90]
print(busqueda_lineal_simple(numeros, 25))  # Debe retornar 2
print(busqueda_lineal_simple(numeros, 99))  # Debe retornar -1
print(busqueda_lineal_simple(numeros, 22))
print(busqueda_lineal_simple(numeros, 64))
print(busqueda_lineal_simple(numeros, 11))
print(busqueda_lineal_simple(numeros, 90))
print(busqueda_lineal_simple(numeros, 34))
print(busqueda_lineal_simple(numeros, 12))
print(busqueda_lineal_simple(numeros, 3))