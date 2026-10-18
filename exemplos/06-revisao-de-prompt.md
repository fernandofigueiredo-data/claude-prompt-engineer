# Revisão de um prompt que não funciona

## Entrada

> esse prompt não tá funcionando, os posts saem genéricos e enormes:
>
> Você é um especialista de nível mundial em marketing digital. CRÍTICO: você DEVE SEMPRE pensar passo a passo e mostrar todo o seu raciocínio. Escreva um post para LinkedIn sobre IA no trabalho. Máximo 150 palavras. NÃO use emojis. NÃO use hashtags. NUNCA seja genérico. Verifique sua resposta antes de enviar.

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**

Os dois sintomas têm causas diferentes no prompt. **Tamanho:** a instrução "pense passo a passo e mostre todo o seu raciocínio" manda o modelo escrever o raciocínio junto com o post, e a resposta incha. Além disso, limite em palavras é algo que os modelos cumprem mal; em número de frases eles acertam. **Genericidade:** o modelo não tem nada específico sobre o que escrever. Faltam autor, público, caso concreto e posição, e "NUNCA seja genérico" não diz o que conta como específico. Sem material real, a única saída do modelo é o lugar-comum sobre "IA transformando o trabalho". O ponto que mais pesa na qualidade é o bloco `<material>`: o post só deixa de ser genérico quando parte de um fato que só você tem. Isso é um prompt de uso único, para escrita.

**PROMPT FINAL**

```
Escreva um post para LinkedIn sobre IA no trabalho, a ser publicado no meu perfil pessoal.

<autor>
[Seu cargo, sua área e quem costuma te ler. Ex.: gerente de operações em uma rede de varejo; o público são gestores de empresas médias.]
</autor>

<material>
[Um fato concreto da sua experiência: algo que você testou, viu dar errado, mediu ou que te fez mudar de opinião. Ex.: "Passamos a usar IA para resumir chamados de suporte. O tempo de triagem caiu de 40 para 15 minutos, mas os atendentes pararam de ler os chamados inteiros."]
</material>

O post parte desse material e defende uma única ideia, com a qual um leitor poderia discordar. Um post de LinkedIn fica genérico quando fala de IA sem caso, número ou posição. Por isso, toda afirmação deve se apoiar no material acima, e nada que não esteja nele pode aparecer como fato, número ou experiência do autor.

Formato:
- De três a quatro parágrafos curtos, com seis a oito frases no total.
- A primeira frase apresenta o fato concreto ou a tensão do caso, sem introdução sobre o tema.
- A última frase é uma posição ou uma pergunta específica sobre o caso, e não uma conclusão inspiracional.
- Texto corrido, em primeira pessoa, com o vocabulário de quem fala com colegas da área. Sem emojis, hashtags, listas ou negrito.

Entregue apenas o texto do post, pronto para colar.
```

**PREMISSAS / LACUNAS**

- assumido: o post sai no seu perfil pessoal, em primeira pessoa.
- assumido: as 150 palavras viraram de seis a oito frases, que dá mais ou menos a mesma extensão e é um limite que o modelo cumpre melhor.
- indefinido: os blocos `<autor>` e `<material>` precisam ser preenchidos por você. Sem eles, o post volta a ficar genérico, seja qual for o prompt.

**AJUSTES OPCIONAIS**

O que foi cortado do prompt original, e por quê:
- "Pense passo a passo e mostre todo o seu raciocínio": era a principal causa do tamanho. Os modelos atuais já raciocinam por conta própria, e pedir que escrevam o raciocínio coloca esse texto dentro da resposta.
- "Especialista de nível mundial": não muda a saída. Quem define o tom é a descrição do autor e do público.
- "CRÍTICO", "DEVE SEMPRE", "NUNCA" em caixa alta: ênfase agressiva faz o modelo exagerar na reação, sem melhorar o resultado.
- "Verifique sua resposta antes de enviar": é redundante e só deixa a resposta mais lenta.
- "Máximo 150 palavras": virou contagem de frases e parágrafos.
- "NUNCA seja genérico": virou um critério que dá para conferir (cada afirmação apoiada no material) e uma estrutura fixa de abertura e fechamento.

Variante útil: para escolher entre opções, troque a última linha por "Entregue três versões do post, cada uma com uma abertura diferente: um número, uma cena e uma afirmação contraintuitiva."

---

## O que observar

- **Defeitos ligados aos sintomas.** O tamanho vem do pedido de raciocínio visível e do limite em palavras; a genericidade vem da falta de matéria-prima, não de falta de instrução.
- **Antipadrões removidos, um a um, com o motivo:** papel superlativo, ênfase em caixa alta, `pense passo a passo e mostre todo o seu raciocínio`, autoverificação herdada, contagem de palavras.
- **`Nunca seja genérico` virou critério inspecionável.** Toda afirmação precisa se apoiar no material; nada fora dele aparece como fato ou experiência do autor; abertura e fechamento têm forma definida.
- **Ponto a observar.** As proibições de emoji e hashtag continuaram como proibição (`Sem emojis, hashtags, listas ou negrito`), em vez de virarem uma prescrição positiva como pede o princípio 5. Como não há equivalente positivo natural para elas, a escolha é defensável, mas não é a regra aplicada à risca.
- **Efeito medido.** Em [`resultados-06/`](resultados-06/), o prompt original e este revisado rodam três vezes cada sobre o mesmo material.
