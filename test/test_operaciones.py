import pytest
import operaciones


def test_sumar():
    assert operaciones.sumar(2,4) == 6




def test_division_por_cero():
    with pytest.raises(ValueError):
        operaciones.dividir(10,0)


@pytest.mark.parametrize("a,b,esperado",[
    (2,5,7), # numeros positivos
    (-4,-2,-6), # numeros negativos
    (0,0,0) # numeros ceros
])
def test_sumar_varios(a,b,esperado):
    assert operaciones.sumar(a,b) == esperado

@pytest.mark.listo

def test_restar_com_fixture(numeros):
    a,b = numeros
    assert operaciones.restar(a,b) == 0

def test_sumar_con_fixture(numeros):
    a,b= numeros
    assert operaciones.sumar(a,b) == 10

@pytest.mark.lento
def test_sumar_lento():
    assert operaciones.sumar(1,2) == 3

def test_float():
    resultado = 0.1 + 0.2
    assert resultado == pytest.approx(0.3) # tolerancia automática

def test_estructura():
    data = {"nombre":"Ana" , "edad": 23}

    assert "nombre" in data
    
    assert "edad" in data
    assert isinstance(data["nombre"], str)
    assert isinstance(data["edad"], int)

def test_lista():
    lista = [{"id":1},{"id":2}]
    assert all("id" in item for item in lista)