from main import asignar_mafias, ordenar_finalizacion_ascendente

def test_ordenar_3_horarios_de_fin_ascendentemente():
    a = [(1,2),(3,4),(0,1)]
    r = ordenar_finalizacion_ascendente(a)
    assert r == [(0,1),(1,2),(3,4)]

def test_dos_mafias_no_superpuestas():
    a = [[0,2],[2,4]]
    r = asignar_mafias(a)
    assert len(r) == 2

# def test_asignar_varias_mafias():

def test_sin_mafias():
    a = []
    r = asignar_mafias(a)
    assert r == []

# def test_asignar_mafias_evitar_mas_corta():

# def test_asignar_mafias_evitar_primera(): 

# def test_asignar_3_mafias():

def test_dos_pedidos_inicia_km0():
    a = [(5,10),(0,3),(0,5)] 
    r = asignar_mafias(a)
    assert r == [(0,3),(5,10)]

def test_un_pedido_inicia_km_0():
    a = [(0,10),(5,10)] # debe incluir mas elementos
    r = asignar_mafias(a)
    assert r == [(0,10)]

# def test_varias_asignar_mafias_evitar_colisiones():
#     a = # un array con elemementos que dependiendo el orden, se sobreponen
#     assert len(r) == 4
