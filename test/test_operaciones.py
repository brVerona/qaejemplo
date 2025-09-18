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

