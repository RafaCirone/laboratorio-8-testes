"""Exercício 7.2 - Teste unitário isolado com Test Doubles (unittest.mock).

- Dummy: objeto de usuário/sessão que só preenche a assinatura.
- Stub:  ServicoLogisticaAPI devolvendo uma taxa fixa, sem rede.
- Mock/Spy: verifica a chamada de enviar_notificacao_rastreio().
"""
from unittest.mock import Mock, create_autospec

from frete import CalculadoraFrete
from servicos import ServicoLogisticaAPI, ServicoNotificacao


def test_confirmar_frete_usa_taxa_da_api_e_notifica_uma_vez():
    # Arrange
    usuario_dummy = object()  # Dummy: nunca é lido pela lógica

    logistica_stub = create_autospec(ServicoLogisticaAPI, instance=True)
    logistica_stub.consultar_taxa.return_value = 22.50  # Stub: resposta programada

    notificacao_mock = create_autospec(ServicoNotificacao, instance=True)  # Mock/Spy

    calculadora = CalculadoraFrete(logistica_stub, notificacao_mock)
    pedido_id = "PED-1001"

    # Act
    frete = calculadora.confirmar_frete(
        usuario_dummy, pedido_id, valor_carrinho=120.00, cep="01001-000"
    )

    # Assert
    assert frete == 22.50
    logistica_stub.consultar_taxa.assert_called_once_with("01001-000")
    notificacao_mock.enviar_notificacao_rastreio.assert_called_once_with(pedido_id)


def test_frete_gratis_nao_consulta_api_mas_notifica_uma_vez():
    # Arrange
    usuario_dummy = Mock(name="sessao_dummy")
    logistica_stub = create_autospec(ServicoLogisticaAPI, instance=True)
    notificacao_mock = create_autospec(ServicoNotificacao, instance=True)
    calculadora = CalculadoraFrete(logistica_stub, notificacao_mock)

    # Act
    frete = calculadora.confirmar_frete(
        usuario_dummy, "PED-2002", valor_carrinho=300.00, cep="01001-000"
    )

    # Assert
    assert frete == 0.00
    logistica_stub.consultar_taxa.assert_not_called()
    notificacao_mock.enviar_notificacao_rastreio.assert_called_once_with("PED-2002")
    assert usuario_dummy.mock_calls == []  # prova de que o Dummy não foi usado
