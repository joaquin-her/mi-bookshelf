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
	array, indices, suma_maxima = buscar_mejor_subarray(array)
	return array[indices[0]:indices[1]]

def buscar_mejor_subarray(arr):
	medio = len(arr)//2
	arr_i, indices_i, suma_izq = mejor_subarray(arr[:medio])
	arr_d, indices_d, suma_der = mejor_subarray(arr[medio:])
	mejor_izq = arr_i[indices_i[0]:indices_i[1]]
	mejor_der = arr_d[indices_d[0]:indices_d[1]]
	 # se pueden enwrappar la suma parcial y resolver ahi
	suma_centro =suma_izq + suma_der + mi_sum(arr_i[indices_i[1]:] + arr_d[:indices_d[0]])
	if suma_centro > suma_der and suma_centro > suma_izq :
		a = indices_i[0]
		b = medio + indices_d[1]
		suma_maxima = suma_der + suma_izq
	elif suma_der > suma_izq:
		a = medio + indices_d[0]
		b = medio + indices_d[1]
		suma_maxima = suma_der
	else:
		a = indices_i[0]
		b = indices_i[1]
		suma_maxima = suma_izq	
	indices = [a, b]
	return arr, indices, suma_maxima
def mejor_subarray(arr:list)-> list [int,int]:
	if len(arr) == 1:
		indices = [0,1]
		return arr, indices, arr[0]
	return buscar_mejor_subarray(arr)

def mi_sum(array):
	c = 0
	for items in array:
		c += items
	return c

