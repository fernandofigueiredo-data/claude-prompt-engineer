# Resultado medido: o prompt original contra o revisado

O [exemplo 06](../06-revisao-de-prompt.md) mostra a skill revisando um prompt de post para LinkedIn que *"não tá funcionando, os posts saem genéricos e enormes"*. Esta pasta testa se a revisão muda de fato a saída, rodando os dois prompts e medindo o resultado.

## Desenho

Três variantes, três execuções independentes cada, no mesmo modelo, via `claude -p` sem ferramentas:

| Variante | Prompt enviado |
|---|---|
| Original | [`prompt-original.txt`](prompt-original.txt), exatamente como foi enviado à skill |
| Original + o mesmo material | [`prompt-original-com-material.txt`](prompt-original-com-material.txt): o original seguido do relato |
| Revisado pela skill | [`prompt-revisado.txt`](prompt-revisado.txt): o prompt final do exemplo 06, com os blocos `<autor>` e `<material>` preenchidos |

A segunda variante existe para separar dois efeitos. O prompt revisado pede um caso concreto e o original não, então comparar só o original com o revisado misturaria o ganho do material com o ganho da reescrita. O bloco `<autor>` foi preenchido apenas com o que já está no relato, para que a variante revisada não receba nenhuma informação a mais.

O relato em [`material.txt`](material.txt) é fictício, escrito para o teste.

## Resultado

Claude Opus 5.5 (`claude-opus-5-5`), 17/10/2026:

| Variante | Palavras na resposta | Texto além do post | Caso declarado como inventado | Detalhes do relato usados (de 7) | Emoji ou hashtag |
|---|---|---|---|---|---|
| Original | 233 (186–278) | 3 de 3 | 3 de 3 | 0,7 (0–1) | 0 de 3 |
| Original + o mesmo material | 316 (280–350) | 3 de 3 | 0 de 3 | 6,0 (6–6) | 0 de 3 |
| Revisado pela skill | 165 (141–188) | 0 de 3 | 0 de 3 | 5,0 (5–5) | 0 de 3 |

A mesma comparação, repetida com Claude Opus 5 (`claude-opus-5`) e o prompt revisado que a skill gerou naquele modelo ([`opus-5/`](opus-5/)):

| Variante | Palavras na resposta | Texto além do post | Caso declarado como inventado | Detalhes do relato usados (de 7) | Emoji ou hashtag |
|---|---|---|---|---|---|
| Original | 348 (324–380) | 3 de 3 | 3 de 3 | 0,7 (0–1) | 0 de 3 |
| Original + o mesmo material | 428 (391–477) | 3 de 3 | 0 de 3 | 6,3 (6–7) | 0 de 3 |
| Revisado pela skill | 152 (147–157) | 0 de 3 | 0 de 3 | 5,7 (5–6) | 0 de 3 |

Média e intervalo entre as três execuções. Medido por [`scripts/comparar.py`](../../scripts/comparar.py):

- **Texto além do post:** a resposta traz bastidores, checklist das restrições ou aviso ao autor, que precisam ser recortados à mão antes de publicar.
- **Caso declarado como inventado:** a própria resposta avisa que os fatos do post são ilustrativos ou pede para trocá-los por dados reais.
- **Detalhes do relato usados:** quantos de sete detalhes do relato aparecem (os números 47 e 12, o nome Marta, a clínica odontológica, o WhatsApp, as quatro unidades e os meses).

Os padrões do script foram conferidos contra a leitura manual das dezoito saídas.

## Leitura

**A especificidade vem do material, não da reescrita.** Com o mesmo relato, o prompt original também produz um post concreto, e usa até um detalhe a mais que o revisado. Atribuir à skill a cura da genericidade seria exagero. O que ela fez foi diagnosticar que a causa era a falta de matéria-prima e criar um lugar obrigatório para ela.

**A reescrita resolve o tamanho e o formato.** O original pede raciocínio visível e verificação, e todas as seis respostas a ele, com ou sem material, trazem bastidores, contagem de palavras ou avisos ao redor do post. O revisado devolveu só o post, pronto para colar, nas três execuções, nos dois modelos.

**Sem material, o original inventa.** Nas três execuções sem relato, nos dois modelos, o modelo escreveu um caso em primeira pessoa com números fictícios (uma analista que resume 12 entrevistas em 40 minutos, um contrato de 30 páginas revisado em 40 minutos) e avisou ao final que eram exemplos. O prompt revisado foi escrito para não chegar a esse ponto: depende do material e diz que nada fora dele pode aparecer como fato.

**O resultado se repete em dois modelos.** O Opus 5.5 escreve respostas mais curtas que o Opus 5 em todas as variantes, mas a diferença entre elas é a mesma.

**Limites.** Três execuções por variante, um único caso e dois modelos da mesma família: é uma demonstração conferível, não um benchmark. As métricas medem forma e aderência ao relato, não qualidade literária. O prompt revisado pede que o post defenda uma posição, e as saídas acrescentaram opiniões que não estão no relato (por exemplo, que é um erro avaliar o assistente só pelo tempo de resposta). São opiniões, não fatos, e foram pedidas, mas quem publica deve conferir se concorda com elas.

## Arquivos

- `antes-N.md`, `antes_material-N.md`, `depois-N.md`: as nove respostas do Opus 5.5, integrais.
- `opus-5/`: as nove respostas do Opus 5 e o prompt revisado usado naquela rodada.
- `prompt-*.txt` e `material.txt`: as entradas exatas.

Para reproduzir a medição:

```bash
python3 scripts/comparar.py exemplos/resultados-06
```

```bash
python3 scripts/comparar.py exemplos/resultados-06/opus-5
```
