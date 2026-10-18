# Pedido sem informação suficiente

## Entrada

> faz um prompt pro relatório

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**

O pedido não diz qual relatório é. Não há conversa anterior nem arquivos na pasta de trabalho que indiquem isso. O tipo de relatório decide quase tudo no prompt: a estrutura, as fontes que o modelo pode usar, o tamanho e o tom. Qualquer palpite meu teria grande chance de errar o formato da saída, então preciso de três respostas antes de escrever.

**PERGUNTAS**

1. **Que tipo de relatório é?**
   a) Desempenho ou resultados, como vendas, marketing ou KPIs de um período
   b) Status de projeto, com andamento, riscos e próximos passos
   c) Análise ou pesquisa sobre um tema, um mercado ou concorrentes
   d) Técnico, como incidente, auditoria ou diagnóstico
   e) Outro: descreva em uma linha

2. **De onde vêm as informações?**
   a) Dados ou documentos que você vai colar ou anexar, como planilha, anotações ou transcrição
   b) Pesquisa do próprio modelo na web
   c) Uma mistura das duas fontes

3. **Quem vai ler e de que tamanho deve ser?**
   a) Diretoria ou cliente: resumo executivo de uma a duas páginas
   b) Equipe interna: relatório completo, com seções e detalhes
   c) Um sistema ou planilha: saída estruturada para processar depois

Se o relatório se repete, por exemplo toda semana com dados novos, diga também. Nesse caso eu faço um prompt reutilizável com espaço para colar os dados de cada edição.

---

## O que observar

- **Única situação em que a skill não entrega prompt.** `O relatório` não tem referente, e tipo, fonte dos dados, leitor e extensão mudam a arquitetura inteira, então são lacunas bloqueantes.
- **No máximo três perguntas, fechadas, com opções.** Cada uma decide a forma da saída, não um detalhe.
- **Modo de uso antecipado.** A skill avisa que, se o relatório for recorrente, o prompt será reutilizável, com espaço para colar os dados de cada edição.
