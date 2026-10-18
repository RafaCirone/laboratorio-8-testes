"""Exercício 7.1 - Teste unitário do cálculo de frete (padrão AAA)."""
import pytest

from frete import calcular_frete


@pytest.mark.parametrize("valor_carrinho", [0.01, 100.00, 249.99])
def test_frete_padrao_para_carrinho_abaixo_de_250(valor_carrinho):
    # Arrange
    frete_esperado = 15.00

    # Act
    frete = calcular_frete(valor_carrinho)

    # Assert
    assert frete == frete_esperado


@pytest.mark.parametrize("valor_carrinho", [250.00, 250.01, 1000.00])
def test_frete_gratis_para_carrinho_igual_ou_acima_de_250(valor_carrinho):
    # Arrange
    frete_esperado = 0.00

    # Act
    frete = calcular_frete(valor_carrinho)

    # Assert
    assert frete == frete_esperado


def test_valor_negativo_gera_erro():
    # Arrange
    valor_invalido = -1.00

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_frete(valor_invalido)
