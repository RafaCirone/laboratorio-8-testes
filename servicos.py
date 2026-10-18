"""Serviços externos dos quais o cálculo de frete depende.

Nos testes, estes serviços são substituídos por Test Doubles.
"""


class ServicoLogisticaAPI:
    """Consulta taxas locais de frete em uma API de logística externa."""

    def __init__(self, url_base: str = "https://api.logistica.exemplo.com"):
        self.url_base = url_base

    def consultar_taxa(self, cep: str) -> float:
        # Em produção faria uma requisição HTTP; aqui não é usado nos testes.
        raise ConnectionError("Chamada de rede real não disponível neste ambiente.")


class ServicoNotificacao:
    """Envia alertas de envio ao cliente."""

    def enviar_notificacao_rastreio(self, pedido_id: str) -> None:
        raise ConnectionError("Envio real de notificação não disponível neste ambiente.")
