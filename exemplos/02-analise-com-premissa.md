# Análise com premissa embutida

## Entrada

> por que a campanha de black friday da minha loja fracassou? tenho os dados de vendas de novembro de 2025 e de 2026 e o relatório do meta ads

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**
Você quer um diagnóstico causal do resultado da Black Friday, montado a partir de três fontes: vendas do ano anterior, vendas do ano da campanha e o relatório do Meta Ads. É uma análise de uso único, numa conversa, com os arquivos anexados. Dois pontos pesam mais na qualidade do prompt. O primeiro é que a pergunta já dá o fracasso como certo. Por isso o prompt manda medir o resultado antes de explicar, sem abrir mão da sua pergunta. O segundo é que há uma inconsistência de datas: hoje é 17/10/2026, então ainda não existem dados de novembro de 2026. O prompt chama os períodos de "ano anterior" e "ano da campanha", e assim serve para quaisquer dois anos.

**PROMPT FINAL**
```
<contexto>
Tenho uma loja online e a campanha de Black Friday deste ano ficou abaixo do que eu esperava. Quero entender por quê. Anexei três arquivos:
- vendas de novembro do ano anterior;
- vendas de novembro do ano da campanha;
- relatório do Meta Ads da campanha.
</contexto>

<tarefa>
Explique por que a campanha de Black Friday teve o resultado que teve. Faça isso nesta ordem:

1. Meça o resultado. Compare os dois novembros em receita, número de pedidos, ticket médio e, se os dados permitirem, conversão e produtos mais vendidos. Compare também a semana da Black Friday de cada ano, porque a data cai em dias diferentes a cada ano. Diga em uma frase se houve queda, estabilidade ou crescimento, e em quais métricas. Se os números não mostrarem fracasso em alguma métrica, diga isso claramente antes de seguir.

2. Analise o Meta Ads. Olhe investimento, alcance, CPM, CTR, CPC, conversões atribuídas, custo por conversão e ROAS. Separe por campanha, conjunto de anúncios e criativo se o relatório trouxer esse nível de detalhe. Aponte onde o funil quebrou: entrega (alcance ou CPM), atração (CTR) ou conversão (cliques que não viraram compra).

3. Levante as causas possíveis e avalie cada uma. Para cada causa, mostre os dados que a apoiam e os que a enfraquecem. Classifique como sustentada pelos dados, plausível mas não comprovada ou descartada pelos dados. Considere também causas que não estão na mídia paga, como preço, sortimento, estoque ou concorrência, e diga quais dados seriam necessários para confirmá-las.

4. Feche com as duas ou três causas mais prováveis, em ordem, e com o que eu deveria verificar ou mudar na próxima campanha.
</tarefa>

<tratamento_de_incerteza>
Use apenas números que estejam nos arquivos e informe de qual arquivo e coluna cada número saiu. Quando uma conclusão exigir um dado que não está nos arquivos, diga qual é o dado e não estime o valor. Lembre que o Meta Ads usa a própria janela de atribuição: se as conversões do relatório não baterem com as vendas da loja, mostre a diferença e não trate nenhuma das duas fontes como verdade absoluta. Trate coincidência no tempo como hipótese, não como causa.
</tratamento_de_incerteza>

<formato_de_saida>
Escreva em português, com uma seção para cada etapa da tarefa. Use tabelas para comparar números e texto corrido para a interpretação. A conclusão final cabe em no máximo dois parágrafos.
</formato_de_saida>
```

**PREMISSAS / LACUNAS**
- indefinido: quais são os dois anos. Hoje é 17/10/2026, então novembro de 2026 ainda não aconteceu. O mais provável é que você esteja comparando 2024 com 2025. O prompt não depende dos anos.
- assumido: "fracasso" foi medido contra o ano anterior. Se você tinha uma meta de receita ou de ROAS, coloque o número no `<contexto>`. Ele vira o critério principal.
- assumido: a análise roda no chat (claude.ai, Projects ou Cowork), com os três arquivos anexados na mesma mensagem.
- indefinido: o nível de detalhe do relatório do Meta Ads. Sem a quebra por criativo e por conjunto de anúncios, a etapa 2 fica limitada ao total da campanha.

**AJUSTES OPCIONAIS**
- Se você tiver dados do Google Analytics ou da plataforma da loja (sessões, origem do tráfego, abandono de carrinho), anexe-os e acrescente ao `<contexto>`: "também anexei dados de tráfego por origem". Com isso, as causas fora da mídia paga podem ser testadas de verdade em vez de ficarem só como hipótese.

---

## O que observar

- **Pressuposto não declarado.** `Por que fracassou` já afirma o fracasso. A skill põe a medição antes da explicação e manda dizer claramente se os números não mostram fracasso, sem descartar a pergunta do usuário (padrão 1 da auditoria).
- **Avaliação simétrica de causas.** Cada causa vem com os dados que a apoiam e os que a enfraquecem, classificada como sustentada, plausível ou descartada (padrões 3 e 5).
- **Instrução tendenciosa evitada.** Causas fora da mídia paga (preço, sortimento, estoque, concorrência) entram obrigatoriamente, com o dado que faltaria para testá-las (padrão 6).
- **Risco de alucinação alto, tratado.** Todo número cita arquivo e coluna; conversões do Meta Ads e vendas da loja não são tratadas como verdade absoluta; coincidência no tempo é hipótese, não causa.
- **Lacuna percebida pela data.** A skill nota que, em 17/10/2026, novembro de 2026 ainda não aconteceu, e escreve o prompt com "ano anterior" e "ano da campanha" para não depender dos anos.
