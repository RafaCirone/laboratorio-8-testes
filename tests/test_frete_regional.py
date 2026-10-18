"""Exercício 7.4 - TDD: taxa adicional para as regiões Norte e Nordeste.

Regra: Norte/Nordeste pagam R$ 10,00 a mais sobre a taxa base (R$ 15,00),
exceto se o subtotal for superior a R$ 300,00, quando o frete é grátis.
"""
import pytest

from frete import calcular_frete


@pytest.mark.parametrize("regiao", ["Norte", "Nordeste"])
def test_norte_e_nordeste_pagam_taxa_adicional(regiao):
    # Arrange
    valor_carrinho = 100.00

    # Act
    frete = calcular_frete(valor_carrinho, regiao)

    # Assert
    assert frete == 25.00


@pytest.mark.parametrize("regiao", ["Norte", "Nordeste"])
def test_norte_e_nordeste_pagam_taxa_ate_300(regiao):
    # Arrange
    valor_carrinho = 300.00

    # Act
    frete = calcular_frete(valor_carrinho, regiao)

    # Assert
    assert frete == 25.00


@pytest.mark.parametrize("regiao", ["Norte", "Nordeste"])
def test_norte_e_nordeste_frete_gratis_acima_de_300(regiao):
    # Arrange
    valor_carrinho = 300.01

    # Act
    frete = calcular_frete(valor_carrinho, regiao)

    # Assert
    assert frete == 0.00


@pytest.mark.parametrize(
    "valor_carrinho, frete_esperado", [(100.00, 15.00), (250.00, 0.00)]
)
def test_outras_regioes_mantem_regra_original(valor_carrinho, frete_esperado):
    # Arrange
    regiao = "Sudeste"

    # Act
    frete = calcular_frete(valor_carrinho, regiao)

    # Assert
    assert frete == frete_esperado
