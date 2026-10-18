# Lab 8 — Testes Unitários (Módulo de Frete)

| Exercício | Arquivo |
|---|---|
| 7.1 — Teste unitário (AAA) | `tests/test_frete.py` |
| 7.2 — Test Doubles (Dummy, Stub, Mock/Spy) | `tests/test_frete_doubles.py` |
| 7.3 — Execução no PyCharm | ver abaixo |
| 7.4 — TDD (Norte/Nordeste) | `tests/test_frete_regional.py` + `frete.py` |

Código de produção: `frete.py` (cálculo e `CalculadoraFrete`) e `servicos.py`
(`ServicoLogisticaAPI` e `ServicoNotificacao`).

## Regras de negócio
- Carrinho abaixo de R$ 250,00: frete R$ 15,00. A partir de R$ 250,00: grátis.
- Norte/Nordeste: R$ 15,00 + R$ 10,00 = R$ 25,00, exceto se o subtotal for
  superior a R$ 300,00, quando o frete é grátis.

## Ciclo TDD (7.4) no histórico do Git
1. `TDD (vermelho)` — testes escritos antes do código; 8 falhas.
2. `TDD (verde + refatoração)` — implementação mínima com constantes nomeadas; todos passam.

## Como rodar
```bash
pip install -r requirements.txt
pytest -v
```

### No PyCharm (Exercício 7.3)
1. Abra a pasta do projeto e configure o interpretador Python.
2. Settings → Tools → Python Integrated Tools → Default test runner: **pytest**.
3. Clique com o botão direito na pasta `tests` → **Run 'pytest in tests'**.
4. Capture a tela da janela **Run** mostrando os testes passando.
