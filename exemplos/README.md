# Exemplos reais

Cada arquivo traz uma entrada, a resposta integral da skill, sem edição, e uma nota curta apontando quais regras do método aparecem nela. As entradas foram escolhidas para cobrir arquiteturas e situações diferentes, incluindo um prompt ruim para revisão e um pedido vago demais para responder sem perguntar.

| Exemplo | Arquitetura | O que mostra |
|---|---|---|
| [Pedido vago de uso único](01-ideia-vaga.md) | B, com bloco de entrada preenchível | lacuna de dados vira campo, não pergunta; advocacia declarada |
| [Análise com premissa embutida](02-analise-com-premissa.md) | B + tratamento de incerteza | `por que fracassou` vira verificação; nenhum benchmark inventado |
| [Instrução persistente de Project](03-instrucao-de-project.md) | E | risco no que falta; severidade definida por consequência |
| [Pipeline de extração em JSON (Haiku 5.5)](04-pipeline-json.md) | F + C | categorias fechadas; e-mail de terceiro tratado como dado |
| [Agente autônomo de longa duração](05-agente-autonomo.md) | G | linha de base antes de mexer; precedência e critério de parada |
| [Revisão de um prompt que não funciona](06-revisao-de-prompt.md) | B | seis antipadrões removidos e explicados |
| [Pedido sem informação suficiente](07-lacuna-bloqueante.md) | nenhuma: perguntas | três perguntas fechadas em vez de um molde genérico |

**Resultado medido.** Em [`resultados-06/`](resultados-06/), o prompt original e o revisado do exemplo 06 rodam três vezes cada sobre o mesmo material, com as saídas integrais e a medição reproduzível.

## Como foram gerados

Execuções independentes, uma por entrada, numa pasta vazia, com apenas a skill carregada e sem acesso a outros arquivos:

```bash
claude -p --plugin-dir plugins/engenharia-de-prompt --model opus --tools Skill Read \
  --no-session-persistence --output-format json \
  "/engenharia-de-prompt:engenharia-de-prompt <entrada>" > saida.json
```

```bash
python3 scripts/exemplo.py saida.json exemplos/NN-nome.md "Título" "<entrada>" "<nota>"
```

O modelo registrado em cada arquivo é o que a execução informou (`modelUsage`). Os exemplos foram gerados com Claude Code 2.1.276, cujo alias `opus` aponta para Claude Opus 5; a calibração da skill cobre também Opus 5.5, Sonnet 5.5, Haiku 5.5 e Fable 5.1. Saídas de modelo variam entre execuções: rodar a mesma entrada de novo produz um prompt diferente na redação, mas deve manter o diagnóstico, a arquitetura e as premissas essenciais.
