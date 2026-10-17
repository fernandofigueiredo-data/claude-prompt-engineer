# Pedido sem informação suficiente

## Entrada

> faz um prompt pro relatório

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**

A entrada traz o artigo definido ("o relatório") mas nenhum referente: não há conversa anterior, arquivo ou projeto neste ambiente que identifique de que relatório se trata. "Relatório" é justamente o caso-escola de ambiguidade lexical — pode ser uma página de status ou trinta de análise, pode partir de dados colados ou de pesquisa. O assunto e a origem do conteúdo não são detalhe: decidem se o prompt tem bloco de entrada, se precisa de tratamento de incerteza e qual arquitetura usar. Qualquer prompt escrito agora seria um molde genérico, não um prompt executável. Três perguntas fechadas resolvem.

**PERGUNTAS**

1. **Assunto e origem do conteúdo.** Qual o tema, e o material vem de: (a) dados ou documentos que você cola no prompt, (b) pesquisa na web feita pelo modelo, ou (c) conhecimento geral do modelo sobre o tema?

2. **Destinatário e extensão.** Quem lê: (a) você mesmo, (b) chefe, cliente ou diretoria que decide algo com base nele, ou (c) outro sistema que processa a saída? E o tamanho: (a) uma a duas páginas, ou (b) documento longo com seções?

3. **Modo de uso.** É (a) um relatório pontual, ou (b) um modelo reutilizável que roda sobre entradas novas a cada rodada — mensal, por cliente, por projeto?

Respondendo essas três, entrego o prompt final na mesma rodada.

---

## O que observar

- **Única situação em que a skill não entrega prompt.** `O relatório` não tem referente, e assunto, origem dos dados, destinatário e modo de uso mudam a arquitetura inteira, então são lacunas bloqueantes.
- **No máximo três perguntas, fechadas, com opções.** Cada uma decide a forma da saída, não um detalhe.
- **Nada de prompt genérico de consolação.** Um molde vazio seria pior do que perguntar, e a skill diz isso no diagnóstico.
