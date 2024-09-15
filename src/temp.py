ENUNCIADO = 13
"""Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el 
subarreglo contiguo de máxima suma, utilizando División y Conquista. Indicar y 
	justificar la complejidad del algoritmo.
	Ejemplo: [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
	[5, 3, -5, 4, -1] ->  [5, 3]
	[5, -4, 2, 4, -1] -> [5, -4, 2, 4]
	[5, -4, 2, 4] -> [5, -4, 2, 4]
	[-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]
"""

def max_subarray(array):
	medio = len(array) // 2
	subarray, suma = buscar_mejor_subarray(array,0, len(array)-1)
	return subarray

def buscar_mejor_subarray(arr, inicio, fin):
	if inicio == fin:
		return arr[inicio:inicio+1], arr[inicio]

	medio = (inicio + fin)//2
	arr_i, suma_izq = buscar_mejor_subarray(arr, inicio, medio)
	arr_d, suma_der = buscar_mejor_subarray(arr, medio +1, fin)

	arr_c, suma_centro = buscar_cruzado(arr, inicio, medio, fin)

	if suma_centro > suma_der and suma_centro > suma_izq:
		return arr_c, suma_centro
	elif suma_der > suma_izq :
		return arr_d, suma_der
	else:
		return arr_i, suma_izq


def buscar_cruzado(arr, inicio, medio, fin):
	suma_maxima_der = float('-inf')
	suma_maxima_izq = float('-inf')
	suma = 0

	mejor_izquierda = medio
	for i in range(medio, inicio-1, -1):
		suma += arr[i]
		if suma > suma_maxima_izq:
			suma_maxima_izq = suma
			mejor_izquierda = i

	suma = 0
	mejor_derecha = medio +1
	for i in range(medio+1, fin+1):
		suma += arr[i]
		if suma > suma_maxima_der:
			suma_maxima_der = suma
			mejor_derecha = i

	return arr[mejor_izquierda:mejor_derecha+1], suma_maxima_der + suma_maxima_izq

