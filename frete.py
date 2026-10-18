"""Módulo de cálculo de frete."""

FRETE_PADRAO = 15.00
LIMITE_FRETE_GRATIS = 250.00


def calcular_frete(valor_carrinho: float) -> float:
    """Retorna o frete: R$ 15,00 abaixo de R$ 250,00; grátis a partir disso."""
    if valor_carrinho < 0:
        raise ValueError("O valor do carrinho não pode ser negativo.")
    if valor_carrinho >= LIMITE_FRETE_GRATIS:
        return 0.00
    return FRETE_PADRAO
