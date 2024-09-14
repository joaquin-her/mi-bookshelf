from main import max_subarray

def test_ejemplo1():
	a = [1, 2, 3, 4, 5]
	r = max_subarray(a)
	assert r = [1, 2, 3, 4, 5]

def test_ejemplo2():
	a = [1, 2]
	r = max_subarray(a)
	assert r = [1, 2]

def test_ejemplo3():
	a = [-100, 11, 12, -3, -4, -5]
	r = max_subarray(a)
	assert r = [11, 12]

def test_ejemplo4():
	a = [-1, -2, -3, 14, 15, -500]	
	r = max_subarray(a)
	assert r = [14, 15]

def test_ejemplo5():
	a = [1, -2]	
	r = max_subarray(a)
	assert r = [1]

def test_ejemplo6():
	a = [-2, -3, 0, -4, -1, -2]
	r = max_subarray(a)
	assert r = [0]

def test_ejemplo7():
	a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	r = max_subarray(a)
	assert r = [4, -1, 2, 1]

def test_ejemplo8():
	a = [-2, 1, -3, 4, -1, 2, 1, -5]
	r = max_subarray(a)
	assert r = [4, -1, 2, 1]

def test_ejemplo9():
	a = [-3, 4, -1, 2, 1, -5, 4]
	r = max_subarray(a)
	assert r = [4, -1, 2, 1]

def test_ejemplo10():
	a = [1,-2, 5, 4, 3, -2, 4]
	r = max_subarray(a)
	assert r = [5, 4, 3, -2, 4]

def test_ejemplo11():
	a = [5]
	r = max_subarray(a)
	assert r = [5]

def test_ejemplo12():
	a = [5, 3, -5, 4, -1]
	r = max_subarray(a)
	assert r = [5, 3]

def test_ejemplo13():
	a = [5, -4, 2, 4]
	r = max_subarray(a)
	assert r = [5, -4, 2, 4]

def test_ejemplo14():
	a = [-49, -40, -35, 25, -26, 68, 51]
	r = max_subarray(a)
	assert r = [68, 51]

def test_ejemplo15():
	a = [1,-2, 1,-2, 5, 4, 3, -2, 4, 1, -2, 1, -2, 1, -2, 1, -2]
	r = max_subarray(a)
	assert r = [5, 4, 3, -2, 4, 1]

def test_ejemplo16():
	a = [-44, 82, -60, -75, -81, 17, 85]
	r = max_subarray(a)
	assert r = [17, 85]


