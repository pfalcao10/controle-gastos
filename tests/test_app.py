import sys
import os
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import adicionar_gasto, total_gastos, buscar_cotacoes


# --- Testes unitarios originais ---

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


# --- Testes de integracao com mock da API ---

def test_buscar_cotacoes_sucesso():
    """Testa que buscar_cotacoes retorna USD e EUR quando a API responde corretamente."""
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "USDBRL": {"bid": "5.75"},
        "EURBRL": {"bid": "6.20"}
    }

    with patch("requests.get", return_value=mock_response) as mock_get:
        cotacoes = buscar_cotacoes()

        mock_get.assert_called_once()
        assert cotacoes is not None
        assert "USD" in cotacoes
        assert "EUR" in cotacoes
        assert cotacoes["USD"] == 5.75
        assert cotacoes["EUR"] == 6.20


def test_buscar_cotacoes_falha_conexao():
    """Testa que buscar_cotacoes retorna None quando ha erro de conexao."""
    import requests

    with patch("requests.get", side_effect=requests.RequestException("timeout")):
        cotacoes = buscar_cotacoes()
        assert cotacoes is None


def test_buscar_cotacoes_resposta_invalida():
    """Testa que buscar_cotacoes retorna None quando a API retorna JSON inesperado."""
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"chave_errada": {}}

    with patch("requests.get", return_value=mock_response):
        cotacoes = buscar_cotacoes()
        assert cotacoes is None


def test_buscar_cotacoes_chama_url_correta():
    """Testa que a funcao chama a URL correta da AwesomeAPI."""
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "USDBRL": {"bid": "5.80"},
        "EURBRL": {"bid": "6.30"}
    }

    with patch("requests.get", return_value=mock_response) as mock_get:
        buscar_cotacoes()
        args, kwargs = mock_get.call_args
        assert "awesomeapi" in args[0] or "awesomeapi" in str(args)
