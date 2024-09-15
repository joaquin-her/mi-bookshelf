
def max_subarray(array):
	array, indices, suma_maxima = buscar_mejor_subarray(array)
	return array[indices[0]:indices[1]]

def buscar_mejor_subarray(arr):
	if len(arr) == 1:
		indices = [0,1]
		return arr, indices, arr[0]
	medio = len(arr)//2
	arr_i, indices_i, suma_izq = buscar_mejor_subarray(arr[:medio])
	arr_d, indices_d, suma_der = buscar_mejor_subarray(arr[medio:])
	suma_centro =suma_izq + suma_der + mi_sum(arr_i[indices_i[1]:] + arr_d[:indices_d[0]])
	
	print(arr_i, suma_izq, arr_i+arr_d, suma_der, arr_d)

	if suma_centro > suma_der and suma_centro > suma_izq :
		a = indices_i[0]
		b = medio + indices_d[1]
		suma_maxima = suma_centro
	elif suma_der > suma_izq:
		a = medio + indices_d[0]
		b = medio + indices_d[1]
		suma_maxima = suma_der
	else:
		a = indices_i[0]
		b = indices_i[1]
		suma_maxima = suma_izq	
	
	print(indices_i, indices_d)

	print(a,b, '\n')
	indices = [a, b]
	return arr, indices, suma_maxima

def mi_sum(array):
	c = 0
	for items in array:
		c += items
	return c


print([-2, 1, -3, 4, -1, 2, 1, -5, 4], max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))