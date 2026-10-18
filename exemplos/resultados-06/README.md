# Resultado medido: o prompt original contra o revisado

O [exemplo 06](../06-revisao-de-prompt.md) mostra a skill revisando um prompt de post para LinkedIn que *"não tá funcionando, os posts saem genéricos e enormes"*. Esta pasta testa se a revisão muda de fato a saída, rodando os dois prompts e medindo o resultado.

## Desenho

Três variantes, três execuções independentes cada, mesmo modelo (`claude-opus-5`, via `claude -p` sem ferramentas, 17/10/2026):

| Variante | O que recebe |
|---|---|
| Original | o prompt original, exatamente como foi enviado à skill |
| Original + o mesmo material | o prompt original seguido do relato em [`material.txt`](material.txt) |
| Revisado pela skill | o prompt final do exemplo 06, com o mesmo relato no bloco `<material>` |

A segunda variante existe para separar dois efeitos. O prompt revisado pede um caso concreto e o original não, então comparar só o original com o revisado misturaria o ganho do material com o ganho da reescrita.

O relato em `material.txt` é fictício, escrito para o teste.

## Resultado

| Variante | Palavras na resposta | Com raciocínio ou checklist visível | Detalhes concretos do caso (de 7) | Emoji ou hashtag |
|---|---|---|---|---|
| Original | 348 (324–380) | 3 de 3 | 0,7 (0–1) | 0 de 3 |
| Original + o mesmo material | 428 (391–477) | 3 de 3 | 6,3 (6–7) | 0 de 3 |
| Revisado pela skill | 152 (147–157) | 0 de 3 | 5,7 (5–6) | 0 de 3 |

Média e intervalo entre as três execuções. Medido por [`scripts/comparar.py`](../../scripts/comparar.py), que conta palavras, procura seções de raciocínio ou verificação no início de linha, verifica sete detalhes do relato (os números 47 e 12, o nome Marta, a clínica odontológica, o WhatsApp, as quatro unidades e os meses) e procura emojis e hashtags.

## Leitura

**A especificidade vem do material, não da reescrita.** Com o mesmo relato, o prompt original também produz um post concreto: 6,3 dos 7 detalhes, contra 5,7 do revisado. Atribuir à skill a cura da genericidade seria exagero. O que ela fez foi diagnosticar que a causa era a falta de matéria-prima e criar um lugar obrigatório para ela.

**A reescrita resolve o tamanho e o formato.** O original, que pede raciocínio visível e verificação, devolveu o post precedido de uma seção de raciocínio nas seis execuções e seguido de uma verificação em cinco delas. O texto que se recebe tem de 324 a 477 palavras e precisa ser recortado à mão. O revisado devolveu só o post, pronto para colar, nas três execuções.

**Sem material, o original inventa.** Nas três execuções sem relato, o modelo escreveu casos em primeira pessoa com números fictícios (um relatório de 12 páginas revisado em quatro horas, pull requests triplicados, oito dias de espera que viraram dois) e avisou ao final que eram ilustrativos. O prompt revisado foi escrito para não chegar a esse ponto: sem material, ele manda perguntar em vez de escrever.

**Limites.** Três execuções por variante, um único caso e um único modelo: isto é uma demonstração conferível, não um benchmark. As métricas são de forma e de aderência ao relato, não de qualidade literária. Uma das saídas revisadas acrescentou uma expressão que não estava no relato ("as meninas da recepção"), o que mostra que a regra de usar apenas o material reduz, mas não elimina, o acréscimo.

## Saídas

Todas as nove respostas estão nesta pasta, integrais: `antes-N.md`, `antes_material-N.md` e `depois-N.md`.

Para reproduzir a medição:

```bash
python3 scripts/comparar.py exemplos/resultados-06
```
