# Revisão de um prompt que não funciona

## Entrada

> esse prompt não tá funcionando, os posts saem genéricos e enormes:
>
> Você é um especialista de nível mundial em marketing digital. CRÍTICO: você DEVE SEMPRE pensar passo a passo e mostrar todo o seu raciocínio. Escreva um post para LinkedIn sobre IA no trabalho. Máximo 150 palavras. NÃO use emojis. NÃO use hashtags. NUNCA seja genérico. Verifique sua resposta antes de enviar.

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**

O pedido é um prompt reutilizável para posts de LinkedIn em primeira pessoa, uso em chat, arquétipo de escrita. Os dois sintomas têm causas distintas: o tamanho vem de `mostrar todo o seu raciocínio`, técnica descontinuada que infla a resposta com o raciocínio que já é interno e adaptativo, agravada por um limite em contagem de palavras, que os modelos cumprem mal; a genericidade vem da ausência de matéria-prima, porque `NUNCA seja genérico` é critério não inspecionável e nenhum modelo consegue ser específico sobre uma categoria como "IA no trabalho" sem um caso concreto para contar. Os demais defeitos são de técnica: ênfase agressiva em caixa alta, que dispara verificação e cautela em excesso; proibições sem prescrição equivalente; instrução de autoverificação herdada; e um papel de especialista em marketing digital que produz exatamente o tom de peça publicitária que você não quer. A correção estrutural é trocar a proibição de ser genérico por um slot de entrada que exige o caso concreto, mais um critério de especificidade conferível frase a frase.

**PROMPT FINAL**

```
<contexto>
Este post será publicado no perfil pessoal de LinkedIn de quem escreve. O leitor é um profissional rolando o feed, que abandona em duas linhas qualquer texto com cara de conselho geral sobre tecnologia.
</contexto>

<material>
[Cole aqui uma situação concreta que você viveu ou observou envolvendo IA no trabalho: o que aconteceu, com quem, em que contexto, e qualquer número, prazo ou resultado real que você conheça. Inclua o que te surpreendeu ou fez mudar de opinião.]
</material>

<tarefa>
Escreva um post de LinkedIn a partir do material acima, na primeira pessoa, mantendo o ponto de vista e o vocabulário de quem relatou a situação.
</tarefa>

<regras>
Use apenas o que está no material. Se faltar um dado que o post pediria, como número, nome ou resultado, escreva o post sem ele em vez de estimar: dado inventado em post público custa credibilidade.
Se o material não trouxer nenhuma situação concreta, não escreva o post. Responda com as duas ou três perguntas que faltam para escrevê-lo.
Escreva em texto corrido, só palavras e pontuação, sem emojis, sem hashtags, sem marcadores e sem negrito. O registro é de alguém contando algo, não de peça de marketing.
</regras>

<formato_de_saida>
Apenas o texto do post, pronto para colar, sem título e sem nenhum comentário antes ou depois.
Primeira frase entrega a situação, e não uma pergunta retórica nem uma tese sobre o futuro do trabalho.
Corpo em dois a quatro parágrafos, no máximo três frases cada.
Fechamento em uma frase.
</formato_de_saida>

<criterios_de_sucesso>
Nenhuma frase do post continua verdadeira se trocar o setor, a empresa, a pessoa ou o ano: toda afirmação está amarrada ao caso relatado.
O post não contém nenhuma frase que seja observação geral sobre IA, produtividade ou futuro do trabalho.
Quem conhece o autor reconhece a história como dele.
Aplique os três critérios ao post inteiro, não apenas ao primeiro parágrafo.
</criterios_de_sucesso>
```

**PREMISSAS / LACUNAS**

- `assumido` Post no perfil pessoal, em primeira pessoa; perfil de empresa ou marca pediria outro registro e outro fechamento.
- `assumido` Uso repetido, com material diferente a cada post; daí o slot `<material>` em vez de um tema fixo no prompt.
- `assumido` Escrito para rodar em chat, sem controle de esforço, compatível com Opus 5.5 e Sonnet 5.5.
- `indefinido` O assunto real. "IA no trabalho" é categoria, não assunto: o que o post diz passa a ser definido a cada execução pelo material colado.
- `indefinido` Objetivo do post, como autoridade, atração de clientes ou recrutamento. Havendo um, ele muda o fechamento.

**AJUSTES OPCIONAIS**

- **Uso único:** substitua o bloco `<material>` pelo relato escrito direto e apague a segunda linha de `<regras>`, que só existe para o caso de slot vazio.
- **Objetivo comercial declarado:** acrescente em `<formato_de_saida>` qual porta o fechamento abre, por exemplo `A última frase convida a comentar com uma experiência parecida, sem pedir contato`. Sem isso o fechamento sai neutro.
- **Cortado do original e por quê:** o papel de especialista em marketing, que produzia o tom publicitário; o pedido de raciocínio visível, descontinuado e causa do excesso de texto; o limite de 150 palavras, trocado por limite em frases, que é conferível por inspeção; a autoverificação final, que em modelos atuais só adiciona cautela; e as quatro proibições, convertidas em uma prescrição positiva de texto corrido.

---

## O que observar

- **Defeitos nomeados por categoria e ligados aos sintomas.** O tamanho vem do pedido de raciocínio visível e do limite em palavras; a genericidade vem da falta de matéria-prima, não de falta de instrução.
- **Antipadrões removidos:** papel superlativo (`especialista de nível mundial`), ênfase em caixa alta, `pense passo a passo e mostre todo o seu raciocínio` (que a família 5.5 pode recusar), contagem de palavras, autoverificação herdada e quatro proibições sem alternativa.
- **`Nunca seja genérico` virou critério inspecionável.** Nenhuma frase do post continua verdadeira se trocar setor, empresa, pessoa ou ano.
- **Instrução positiva.** As proibições de emoji, hashtag e marcadores viraram `texto corrido, só palavras e pontuação`.
- **O que foi cortado e por quê** aparece em AJUSTES OPCIONAIS, como o formato de saída exige em revisões.
