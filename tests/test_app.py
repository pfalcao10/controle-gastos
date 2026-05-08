import sys
import os

# adiciona a pasta src no caminho
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import adicionar_gasto, total_gastos


def test_adicionar_gasto_valido():
    adicionar_gasto("teste", 10)
    assert total_gastos() >= 10


def test_valor_negativo():
    try:
        adicionar_gasto("erro", -5)
        assert False
    except ValueError:
        assert True


def test_total():
    adicionar_gasto("teste2", 20)
    assert total_gastos() >= 20