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


class CalculadoraFrete:
    """Calcula e confirma o frete usando os serviços externos injetados."""

    def __init__(self, servico_logistica, servico_notificacao):
        self.servico_logistica = servico_logistica
        self.servico_notificacao = servico_notificacao

    def confirmar_frete(self, usuario, pedido_id: str, valor_carrinho: float, cep: str) -> float:
        """Confirma o frete do pedido e notifica o cliente.

        `usuario` faz parte da assinatura (auditoria futura), mas não é usado na lógica.
        """
        if valor_carrinho >= LIMITE_FRETE_GRATIS:
            frete = 0.00
        else:
            frete = self.servico_logistica.consultar_taxa(cep)

        self.servico_notificacao.enviar_notificacao_rastreio(pedido_id)
        return frete
