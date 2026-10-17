# Análise com premissa embutida

## Entrada

> por que a campanha de black friday da minha loja fracassou? tenho os dados de vendas de novembro de 2025 e de 2026 e o relatório do meta ads

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**

A entrada pede um diagnóstico causal de desempenho de campanha a partir de dois conjuntos de vendas comparáveis e um relatório de mídia paga — arquétipo de diagnóstico sobre dados anexados, em uso único de conversa. O que mais condiciona a qualidade do prompt é que a pergunta já traz o veredito embutido: "por que fracassou" afirma o fracasso, convida a uma causa única e, como o Meta Ads é a única fonte de mídia disponível, induz o modelo a culpar o canal que ele consegue ver. O prompt abaixo inverte a ordem — verifica a cobertura temporal, depois testa se houve fracasso e em qual métrica, e só então busca causas — e separa explicitamente o que os dados sustentam do que fica fora do alcance deles. Risco de alucinação alto por conta de benchmarks de setor, que o prompt bloqueia nominalmente.

**PROMPT FINAL**

```
<papel>
Você é analista de dados de e-commerce. Você separa o que os dados mostram do que você supõe, e não apresenta hipótese como achado.
</papel>

<contexto>
Sou dono de uma loja online e acredito que minha campanha de Black Friday teve desempenho ruim. Isso é meu julgamento inicial, não um fato verificado. Estou anexando o que tenho: as vendas de dois novembros consecutivos e o relatório de desempenho da campanha no Meta Ads.
</contexto>

<dados>
[anexe aqui as planilhas de vendas dos dois períodos e o relatório do Meta Ads]
</dados>

<tarefa>
Produza um diagnóstico do desempenho da campanha em quatro movimentos, nesta ordem.

1. Cobertura dos dados. Informe a data inicial e a data final de cada arquivo e diga se o período da Black Friday está integralmente coberto nos dois anos. Se um dos períodos estiver parcial ou em curso, aponte isso antes de qualquer comparação e marque como provisória toda comparação afetada.

2. Verificação do fracasso. Compare os dois períodos em todas as métricas que os arquivos permitirem calcular, entre elas receita, número de pedidos, ticket médio, taxa de conversão, investimento em mídia, retorno sobre o investimento em anúncios, custo por aquisição e mix de produtos vendidos. Diga em quais métricas houve queda, em quais houve estabilidade e em quais houve melhora. Conclua se a campanha piorou, ficou estável ou melhorou, e em qual dimensão especificamente. Se os dados não sustentarem a hipótese de fracasso, diga isso de forma direta.

3. Localização da perda. Para cada métrica que piorou, percorra a sequência investimento, alcance, cliques, sessões, carrinhos, pedidos, receita, e identifique em qual elo a perda aparece. Pule os elos que os arquivos não medem e diga quais foram pulados. Distinga queda no volume de entrada de queda na eficiência de conversão.

4. Causas. Liste as causas candidatas em duas categorias: as que os arquivos anexados sustentam, cada uma acompanhada dos números específicos que a sustentam, e as que os arquivos não permitem testar, apresentadas como hipótese com a informação que falta nomeada. Percorra ao menos estas frentes, dizendo explicitamente quando uma delas estiver fora do alcance dos dados: desempenho da mídia paga, conversão no site, preço e profundidade de desconto, disponibilidade de estoque, mix e margem dos produtos, outros canais de aquisição, e a base de comparação do ano anterior.
</tarefa>

<regras>
Todo número que você citar deve vir dos arquivos anexados. Não use médias de mercado, benchmarks de setor nem valores típicos de referência, porque não tenho como auditar sua procedência e uma comparação contra número inventado leva a decisão errada.

Não atribua a causa principal ao Meta Ads apenas porque é a única fonte de mídia que anexei. Se a perda estiver em um elo que os arquivos não medem, diga que está fora do alcance dos dados.

Trate queda de retorno sobre investimento e queda de taxa de conversão como sintomas a explicar, não como causas.

Quando a evidência admitir mais de uma causa, apresente todas, ordenadas pela força da evidência, e diga qual é a mais provável e por quê.

Quando duas instruções entrarem em conflito, a prioridade é não afirmar o que os dados não mostram.
</regras>

<formato_de_saida>
Quatro seções, nomeadas Cobertura dos dados, Verificação do fracasso, Localização da perda e Causas, na ordem da tarefa.

Em Verificação do fracasso, use uma tabela com uma linha por métrica e colunas para o primeiro período, o segundo período e a variação.

Em Causas, use uma lista em que cada item começa pelo rótulo sustentado pelos dados ou hipótese a verificar.

Encerre com uma seção chamada O que eu precisaria enviar, com no máximo cinco informações que fechariam as lacunas mais relevantes, cada uma com uma frase dizendo qual pergunta ela responderia.
</formato_de_saida>

<tratamento_de_incerteza>
Quando um cálculo depender de um campo que não existe nos arquivos, escreva não calculável com os dados enviados e nomeie o campo que falta, em vez de estimar.

Quando uma métrica admitir mais de uma forma de cálculo a partir dos arquivos, declare qual definição você usou.

Terminar com três causas sustentadas e quatro lacunas declaradas é melhor que terminar com oito causas das quais metade é suposição.
</tratamento_de_incerteza>
```

**PREMISSAS / LACUNAS**

- `assumido` O critério de fracasso não foi declarado; em vez de fixar uma métrica, o prompt manda medir todas as calculáveis e localizar onde a queda está.
- `assumido` Os arquivos anexados são a única fonte admissível de números, sem autorização para dados externos.
- `assumido` Uso em conversa com arquivos anexados, não chamada programática; escrito para funcionar em Opus 5.5 e Sonnet 5.5.
- `indefinido` Qual par de anos é o comparativo real. Hoje é 17 de outubro de 2026, então a Black Friday de 2026 ainda não ocorreu e "novembro de 2026" não pode estar completo. O prompt não fixa anos e trata isso no primeiro movimento, mas vale conferir se os arquivos são 2024 e 2025.
- `indefinido` Se houve outros canais de aquisição além do Meta Ads; o prompt obriga declarar o que fica fora do alcance dos dados em vez de assumir canal único.
- `indefinido` A janela de datas que você considera "Black Friday"; o prompt deriva dos arquivos.

**AJUSTES OPCIONAIS**

- Se você também tiver dados de comportamento no site (GA4, Shopify analytics ou equivalente), anexe-os e troque, no movimento 3, "Pule os elos que os arquivos não medem" por "Use os dados de navegação para medir a queda entre sessões, carrinhos e pedidos". É o que converte a maior parte das hipóteses do movimento 4 em causas sustentadas.
- Se a intenção for repetir esta análise a cada campanha, o mesmo conteúdo funciona como instrução persistente de Project: remova o bloco `<contexto>`, troque `<dados>` por uma instrução de que os arquivos de cada rodada virão anexados, e mantenha o resto.

---

## O que observar

- **Pressuposto não declarado.** `Por que fracassou` já afirma o fracasso. A skill transforma a verificação em segunda etapa da tarefa e manda dizer de forma direta se os dados não sustentam a hipótese (padrão 1 da auditoria).
- **Instrução tendenciosa evitada.** Como o Meta Ads é a única fonte de mídia anexada, o prompt proíbe culpá-lo só por ser o canal visível (padrão 6).
- **Ordem evidência → interpretação → causa.** Quatro movimentos fixos, com causas rotuladas como *sustentadas pelos dados* ou *hipótese a verificar* (padrão 5, conclusão precipitada).
- **Risco de alucinação alto, tratado.** Benchmarks de setor proibidos nominalmente, campo ausente vira `não calculável`.
- **Lacuna percebida pela data.** A skill nota que, em 17/10/2026, a Black Friday de 2026 ainda não aconteceu, e registra como `indefinido` em vez de presumir os anos.
