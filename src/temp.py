def buscar_mejor_subarray(arr, inicio=0):
    if len(arr) == 1:
        # Caso base: si solo hay un elemento, el mejor subarray es ese elemento
        return arr, [inicio, inicio + 1], arr[0]

    medio = len(arr) // 2

    # Llamadas recursivas para los subarrays izquierdo y derecho
    arr_i, indices_i, suma_izq = buscar_mejor_subarray(arr[:medio], inicio)
    arr_d, indices_d, suma_der = buscar_mejor_subarray(arr[medio:], inicio + medio)

    # Encontrar la mejor suma cruzando la mitad
    suma_centro, a, b = suma_maxima_cruzada(arr, medio, inicio)

    # Comparar los tres casos: suma izquierda, derecha y cruzada
    if suma_centro > suma_der and suma_centro > suma_izq:
        suma_maxima = suma_centro
        indices = [a, b]
        mejor_subarray = arr[a - inicio:b - inicio]
    elif suma_der > suma_izq:
        suma_maxima = suma_der
        indices = indices_d
        mejor_subarray = arr[indices_d[0] - inicio:indices_d[1] - inicio]
    else:
        suma_maxima = suma_izq
        indices = indices_i
        mejor_subarray = arr[indices_i[0] - inicio:indices_i[1] - inicio]

    return mejor_subarray, indices, suma_maxima


def suma_maxima_cruzada(arr, medio, inicio):
    # Calcular la mejor suma hacia la izquierda desde la mitad
    suma_izquierda = float('-inf')
    suma = 0
    mejor_izquierda = medio - 1
    for i in range(medio - 1, -1, -1):
        suma += arr[i]
        if suma > suma_izquierda:
            suma_izquierda = suma
            mejor_izquierda = i

    # Calcular la mejor suma hacia la derecha desde la mitad
    suma_derecha = float('-inf')
    suma = 0
    mejor_derecha = medio
    for i in range(medio, len(arr)):
        suma += arr[i]
        if suma > suma_derecha:
            suma_derecha = suma
            mejor_derecha = i

    # Devolver la suma máxima cruzada y los índices
    return suma_izquierda + suma_derecha, mejor_izquierda + inicio, mejor_derecha + 1 + inicio
    
print([-2, 1, -3, 4, -1, 2, 1, -5, 4], max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))