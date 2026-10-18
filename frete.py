"""Módulo de cálculo de frete."""

FRETE_PADRAO = 15.00
LIMITE_FRETE_GRATIS = 250.00

REGIOES_COM_TAXA_ADICIONAL = {"Norte", "Nordeste"}
TAXA_ADICIONAL_REGIONAL = 10.00
LIMITE_FRETE_GRATIS_REGIONAL = 300.00


def calcular_frete(valor_carrinho: float, regiao: str | None = None) -> float:
    """Calcula o frete do carrinho.

    - Regra geral: R$ 15,00 abaixo de R$ 250,00; grátis a partir disso.
    - Norte/Nordeste: R$ 15,00 + R$ 10,00, exceto se o subtotal for
      superior a R$ 300,00, quando o frete é grátis.
    """
    if valor_carrinho < 0:
        raise ValueError("O valor do carrinho não pode ser negativo.")

    if regiao in REGIOES_COM_TAXA_ADICIONAL:
        if valor_carrinho > LIMITE_FRETE_GRATIS_REGIONAL:
            return 0.00
        return FRETE_PADRAO + TAXA_ADICIONAL_REGIONAL

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
