# Pedido vago de uso único

## Entrada

> quero um texto pra mandar pro meu chefe pedindo home office às sextas

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**

O resultado pretendido é uma mensagem única, pronta para copiar e enviar ao gestor, propondo trabalho remoto nas sextas-feiras — arquétipo de escrita persuasiva em contexto corporativo, modo de uso único. O ponto que mais condiciona a qualidade é o risco de fabricação: a mensagem vai para uma pessoa real que conhece a rotina do usuário, e qualquer número de produtividade inventado, política de empresa presumida ou colega citado por suposição se transforma em contradição na resposta do chefe. O segundo ponto é que nenhuma das informações decisivas (motivo real, política vigente, compromissos oferecidos) está no pedido, e todas são dados do usuário, não da forma da saída — por isso entram como bloco preenchível em vez de perguntas.

**PROMPT FINAL**

```
<tarefa>
Redija a mensagem que eu vou enviar ao meu gestor solicitando trabalho remoto nas sextas-feiras, usando apenas as informações do bloco <entrada>. Escreva na primeira pessoa, como se eu fosse o autor.
</tarefa>

<entrada>
Canal: [e-mail / mensagem de chat de trabalho / roteiro para conversa presencial]
Meu primeiro nome: [...]
Como me dirijo ao meu gestor no dia a dia: [ex.: "Oi, João" / "Prezado Sr. Silva"]
O que existe hoje de política de trabalho remoto na empresa: [não há / há para alguns times / é caso a caso / não sei]
Colegas do meu time ou da empresa que já fazem isso: [quem e em que formato / nenhum / não sei]
Por que eu quero: [o motivo real, nas minhas palavras]
Que tipo de trabalho eu faço nas sextas hoje: [ex.: reuniões, atendimento, execução individual]
O que eu me comprometo a manter: [ex.: horário, tempo de resposta, presença em reuniões específicas]
Formato que quero propor: [permanente / período de teste de X semanas / a combinar]
</entrada>

<regras>
Use somente o que está em <entrada>. Esta mensagem vai para uma pessoa real que conhece minha rotina: um dado inventado sobre minha produtividade, sobre a política da empresa ou sobre o que colegas fazem me deixa exposto a ser contrariado na resposta.
Enquadre o pedido como proposta de trabalho, não como favor pessoal, e trate de forma explícita a objeção que o gestor provavelmente tem, que é perda de disponibilidade e de cobertura na sexta-feira, usando o que eu declarei em "O que eu me comprometo a manter".
Mantenha o motivo que eu declarei em "Por que eu quero", sem trocá-lo por uma justificativa de negócio que eu não dei.
Peça uma decisão ou uma conversa de forma direta no fechamento.
Escreva em tom de colega fazendo um pedido razoável: sem pedir desculpas pelo pedido, sem agradecer antecipadamente pela aprovação e sem linguagem de exigência ou prazo imposto.
Escreva em prosa corrida, sem títulos, sem negrito e sem listas, porque é uma mensagem de trabalho e não um documento.
Quando veracidade e força de persuasão entrarem em conflito, prefira a veracidade.
</regras>

<formato_de_saida>
Entregue apenas a mensagem, pronta para copiar, nesta ordem: assunto (somente se o canal for e-mail), saudação, o pedido com o formato que estou propondo, o tratamento da objeção de disponibilidade, fechamento com pedido de decisão ou de conversa, assinatura com meu primeiro nome.
No máximo quatro parágrafos entre a saudação e a assinatura.
Não escreva comentários, explicações, alternativas ou observações antes ou depois da mensagem, com a única exceção prevista em <tratamento_de_incerteza>.
</formato_de_saida>

<tratamento_de_incerteza>
Se algum campo de <entrada> estiver vazio ou marcado como "não sei", não preencha com suposição: escreva a mensagem sem aquele elemento e, depois da assinatura, sob a linha "FALTA DEFINIR", liste em uma linha cada informação que eu preciso acrescentar antes de enviar. Se não faltar nada, não escreva essa linha.
</tratamento_de_incerteza>
```

**PREMISSAS / LACUNAS**

- `assumido` o gestor direto é quem decide, e o pedido é negociação de um arranjo, não invocação de direito já garantido
- `assumido` canal padrão e-mail, razão pela qual o assunto entra como elemento condicional em vez de obrigatório
- `assumido` o usuário quer persuadir, e não apenas comunicar uma decisão já tomada — advocacia declarada, mantida
- `indefinido` motivo real, política da empresa, precedentes e compromissos oferecidos: preenchidos pelo usuário no bloco de entrada
- `indefinido` modelo alvo não informado; o prompt foi escrito para funcionar em chat, em Opus 5.5 e Sonnet 5.5

**AJUSTES OPCIONAIS**

Se você não souber como seu chefe reage a esse tipo de pedido, troque a primeira linha de `<formato_de_saida>` por: `Entregue duas versões da mensagem, separadas pelas linhas "VERSÃO DIRETA" e "VERSÃO CONSERVADORA", idênticas no conteúdo e diferentes apenas no grau de firmeza do pedido e na extensão da justificativa.` Mantenha o limite de quatro parágrafos em cada uma.

Se a empresa tiver política formal de trabalho remoto e você quiser citá-la, acrescente ao bloco `<entrada>` o campo `Trecho exato da política que se aplica ao meu caso: [cole aqui]` e a `<regras>` a linha `Cite a política apenas pelo trecho que eu colei, sem parafrasear o que ela permite.`

---

## O que observar

- **Lacuna não vira interrogatório.** Faltam motivo, política da empresa e compromissos, mas são dados do usuário, não da forma da saída. A skill não pergunta: cria um bloco `<entrada>` preenchível e declara as lacunas como `indefinido` (regra *Sobre perguntar*).
- **Não fabricação com motivo.** A regra contra inventar números de produtividade ou política vem acompanhada do porquê: o chefe conhece a rotina e pode contradizer (princípio 3, *contexto com motivo*).
- **Advocacia declarada é mantida.** A mensagem é persuasiva por natureza; a auditoria registra isso como premissa em vez de neutralizar o pedido (padrão 3 da auditoria de vieses).
- **Formato verificável.** `No máximo quatro parágrafos`, ordem fixa dos elementos, e uma saída de emergência `FALTA DEFINIR` para campos vazios.
