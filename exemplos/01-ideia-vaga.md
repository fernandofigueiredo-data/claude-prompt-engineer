# Pedido vago de uso único

## Entrada

> quero um texto pra mandar pro meu chefe pedindo home office às sextas

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**
O resultado esperado é uma mensagem curta e pronta para enviar ao chefe, pedindo home office às sextas. É uma tarefa de escrita persuasiva, usada uma única vez em conversa. O que mais pesa na qualidade é o modelo não ter as razões reais do pedido nem saber como é sua relação com o chefe. Sem isso, ele tende a inventar justificativas genéricas, como "aumento de produtividade", que soam falsas e enfraquecem o pedido. Por isso o prompt tem campos para você preencher e proíbe o modelo de criar argumentos que você não deu.

**PROMPT FINAL**
```
Escreva uma mensagem para eu enviar ao meu chefe pedindo para trabalhar de casa às sextas-feiras.

<contexto>
Canal: [e-mail / WhatsApp / Slack ou Teams]
Relação com o chefe: [formal / próxima e informal]
Por que quero home office às sextas: [suas razões reais]
O que garante que meu trabalho não será prejudicado: [ex.: entregas que faço remotamente, disponibilidade no horário, reuniões de sexta que posso fazer online]
Política da empresa sobre home office, se houver: [existe / não existe / não sei]
Formato do pedido: [definitivo / período de teste, ex.: um mês]
</contexto>

<regras>
- Use apenas as razões e garantias que escrevi acima. Se algum campo estiver vazio, deixe esse ponto fora da mensagem; um argumento genérico que eu não dei soa artificial para quem me conhece.
- O tom deve ser de pedido, não de exigência: deixe claro que estou aberto a ajustar o formato.
- Ajuste o registro ao canal e à relação informados. E-mail tem assunto, saudação e despedida. Mensagem de chat é mais curta e direta.
- Tamanho máximo: três parágrafos curtos para e-mail, ou um parágrafo para chat.
- Termine propondo um próximo passo concreto, como uma conversa rápida ou o início do teste numa data.
</regras>

Entregue só a mensagem pronta para copiar. Se for e-mail, inclua o assunto na primeira linha.
```

**PREMISSAS / LACUNAS**
- assumido: o texto vai em português e tem tom profissional.
- indefinido: canal, nível de formalidade e razões do pedido. Ficaram como campos que você preenche antes de rodar o prompt.

**AJUSTES OPCIONAIS**
- Se quiser escolher entre opções, acrescente ao final: `Escreva duas versões, uma mais formal e outra mais direta.`
- Se o chefe já recusou um pedido parecido antes, acrescente ao contexto: `Já pedi antes e a resposta foi [X]; a mensagem deve responder a essa objeção.`

---

## O que observar

- **Lacuna não vira interrogatório.** Faltam canal, relação com o chefe e motivo, mas são dados do usuário, não da forma da saída. A skill não pergunta: cria campos preenchíveis em `<contexto>` e declara o que ficou `indefinido` (regra *Sobre perguntar*).
- **Não fabricação com motivo.** A regra de usar só as razões fornecidas vem com o porquê: um argumento genérico soa artificial para quem conhece o autor (princípio 3, *contexto com motivo*).
- **Formato verificável e condicional.** Três parágrafos curtos para e-mail, um para chat, assunto na primeira linha só se for e-mail.
- **Arquitetura enxuta.** Uma linha de tarefa, dois blocos e uma linha de entrega: nada de papel, exemplos ou bloco de incerteza, porque não mudariam a saída.
