# Exemplos reais

Cada arquivo traz uma entrada, a resposta integral da skill, sem edição, e uma nota curta apontando quais regras do método aparecem nela. As entradas foram escolhidas para cobrir arquiteturas e situações diferentes, incluindo um prompt ruim para revisão e um pedido vago demais para responder sem perguntar.

| Exemplo | Arquitetura | O que mostra |
|---|---|---|
| [Pedido vago de uso único](01-ideia-vaga.md) | B enxuto, com campos preenchíveis | lacuna de dados vira campo, não pergunta; regra com motivo |
| [Análise com premissa embutida](02-analise-com-premissa.md) | B + tratamento de incerteza | `por que fracassou` vira medição; causas avaliadas com evidência a favor e contra |
| [Instrução persistente de Project](03-instrucao-de-project.md) | E | citação antes da análise; severidade definida por consequência |
| [Pipeline de extração em JSON (Haiku 5.5)](04-pipeline-json.md) | F | categorias fechadas; entrada malformada prevista; prompt estático para cache |
| [Agente autônomo de longa duração](05-agente-autonomo.md) | G | linha de base, worktree isolado, precedência e critério de parada |
| [Revisão de um prompt que não funciona](06-revisao-de-prompt.md) | B enxuto | antipadrões removidos e explicados; efeito medido |
| [Pedido sem informação suficiente](07-lacuna-bloqueante.md) | nenhuma: perguntas | três perguntas fechadas em vez de um molde genérico |

**Resultado medido.** Em [`resultados-06/`](resultados-06/), o prompt original e o revisado do exemplo 06 rodam três vezes cada sobre o mesmo material, com as saídas integrais e a medição reproduzível.

## Como foram gerados

Execuções independentes, uma por entrada, numa pasta vazia, com apenas a skill carregada e sem acesso a outros arquivos:

```bash
claude -p --plugin-dir plugins/engenharia-de-prompt --model claude-opus-5-5 --tools Skill Read \
  --no-session-persistence --output-format json \
  "/engenharia-de-prompt:engenharia-de-prompt <entrada>" > saida.json
```

```bash
python3 scripts/exemplo.py saida.json exemplos/NN-nome.md "Título" "<entrada>" "<nota>"
```

O modelo registrado em cada arquivo é o que a execução informou (`modelUsage`). Os exemplos foram gerados com Claude Code 2.1.302 e Claude Opus 5.5 (`claude-opus-5-5`). Versões anteriores do Claude Code não reconhecem esse identificador. A versão 1.0.1 deste repositório trazia os mesmos exemplos gerados com Claude Opus 5, e continua disponível no histórico. Saídas de modelo variam entre execuções: rodar a mesma entrada de novo produz um prompt diferente na redação, mas deve manter o diagnóstico, a arquitetura e as premissas essenciais.
