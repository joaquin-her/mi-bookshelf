from main import max_subarray
def test_sin_negativos():
	a = [5, 3, 2] 
	r = max_subarray(a)
	assert [5, 3, 2] == r 

def test_con_negativo_al_final():
	a = [5, 3, 2, 4, -1] 
	r = max_subarray(a)
	assert [5, 3, 2, 4] == r 
	 
def test_con_negativo_al_final_y_al_medio():
	a = [5, -4, 2, 4, -1]
	r = max_subarray(a)
	assert [5, -4, 2, 4] == r 
	 
def test_con_negativo_al_medio():
	a = [5, -4, 2, 4]
	r = max_subarray(a)
	assert [5, -4, 2, 4] == r 
	 
def test_ejemplo4():
	a = [-3, 4, -1, 2, 1, -5] 
	r = max_subarray(a)
	assert [4, -1, 2, 1] == r 

def test_ejemplo5():
	a = [5, 3, -5, 4, -1]
	r = max_subarray(a)
	assert [5, 3] == r 

def test_negativos_menor_en_el_centro():
	a = [-2,-3,-1,-2,-4]
	r = max_subarray(a)
	assert [-1] == r 

def test_todos_negativos():
	a = [-1,-2,-3,-4,-5]
	r = max_subarray(a)
	assert [-1] == r 

def test_intercalados():
	a = [-1,1,-2,2,-3,3,-4,4,-5,5]
	r = max_subarray(a)
	assert [5] == r 
