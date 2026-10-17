# Auditoria epistêmica

Protocolo de detecção e correção de distorções no pedido original. Executado na Etapa 2 da metodologia.

**Princípio governante.** A auditoria não corrige a posição do usuário. Torna explícito o que estava implícito, de modo que a decisão permaneça com ele, mais bem informada. Prompt que silenciosamente neutraliza a tese do autor viola o compromisso de fidelidade tanto quanto prompt que a amplifica.

**Distinção indispensável.** Advocacia declarada é legítima. `Escreva o argumento mais forte a favor de X` é um pedido honesto e não exige correção. O que exige correção é advocacia disfarçada de análise: `Analise se X é a melhor opção`, quando o texto inteiro pressupõe que é.

**Economia da auditoria.** O resultado entra na entrega como uma linha no bloco de premissas, ou como um ajuste estrutural no prompt. Nunca como advertência moral.

---

## Os nove padrões

### 1. Pressuposto não declarado

**Detecção.** A formulação trata como estabelecido algo que ainda não foi verificado. Marcadores: interrogativas que embutem o fato, como `por que X falhou`, `como corrigir o erro de Y`; artigos definidos aplicados a entidades não constituídas, como `o problema do time`.

**Teste.** Negar o pressuposto. Se a pergunta se torna incoerente, o pressuposto é estrutural.

**Correção.** Conforme o caso:
- pressuposto verdadeiro e conhecido: promover a dado explícito no bloco de contexto;
- pressuposto incerto: transformar a verificação em primeira etapa da tarefa;
- pressuposto do usuário, assumido conscientemente: registrar como premissa declarada.

**Exemplo.** `Por que nossa campanha no Instagram não converte` torna-se `Avalie o desempenho de conversão da campanha descrita em <dados>. Primeiro determine se há de fato déficit de conversão frente a [referência]. Se houver, identifique as causas prováveis; se não houver, diga isso.`

---

### 2. Framing enviesado

**Detecção.** Vocabulário avaliativo dentro da descrição do objeto: `o modelo engessado`, `a solução moderna`, `a burocracia atual`. O adjetivo conclui antes da análise.

**Teste.** Substituir cada termo carregado por descrição neutra. Se o pedido perde força retórica mas mantém sentido, o termo era framing.

**Correção.** Substituir por descrição operacional, ou preservar o termo movendo-o para o bloco de contexto marcado como avaliação do usuário, não como fato.

---

### 3. Confirmação de premissa

**Detecção.** Verbos que pedem apoio em vez de teste: `prove que`, `confirme que`, `mostre como X é superior`, `liste as razões pelas quais`.

**Teste.** O prompt admite como saída válida uma conclusão contrária à esperada? Se não admite, é confirmação.

**Correção.** Converter em avaliação simétrica: `Avalie a hipótese de que X é superior a Y quanto a [critérios]. Apresente a evidência favorável e a contrária, e conclua apenas depois.` Quando o usuário realmente quiser advocacia, manter o pedido e registrar no bloco de premissas que a saída é argumentativa, não avaliativa.

---

### 4. Generalização

**Detecção.** Quantificadores universais ou categorias amplas sem escopo: `todos os clientes`, `o mercado brasileiro`, `sempre funciona`, `ninguém faz mais isso`.

**Teste.** Perguntar: qual o universo e qual a fonte? Se não há resposta, a generalização é retórica.

**Correção.** Restringir o escopo ao universo efetivamente conhecido, ou exigir que a saída qualifique a extensão de cada afirmação.

---

### 5. Conclusão precipitada

**Detecção.** O pedido pula da observação ao veredito sem etapa de evidência. Frequente em diagnósticos: `o problema é o preço, escreva a justificativa`.

**Teste.** Existe passo entre dado e conclusão? Se não existe, há salto.

**Correção.** Impor ordem no bloco de tarefa: evidência antes de interpretação, interpretação antes de recomendação. Ordenação de etapas é o instrumento mais eficaz contra esse padrão, mais eficaz que qualquer advertência.

---

### 6. Instrução tendenciosa

**Detecção.** Restrições que tornam impossível uma classe inteira de respostas: `sem considerar custo`, `ignore as objeções jurídicas`, `foque só no lado positivo`.

**Teste.** A restrição exclui informação que mudaria a decisão do usuário?

**Correção.** Manter a restrição, porque pode haver razão legítima, e acrescentar exigência de sinalização: `Se algum fator excluído do escopo puder inverter a conclusão, registre isso em uma linha ao final.` Preserva a intenção sem produzir cegueira.

---

### 7. Critério subjetivo apresentado como fato

**Detecção.** Superlativos e qualificadores sem métrica: `o melhor formato`, `a abordagem mais eficiente`, `o texto mais impactante`.

**Teste.** Duas pessoas competentes chegariam à mesma resposta? Se não, o critério não está operacionalizado.

**Correção.** Operacionalizar em critérios verificáveis, ou pedir que a saída declare o critério antes de aplicá-lo. `Escolha o melhor canal` torna-se `Recomende o canal que maximiza [métrica] dado [restrição]. Declare o critério de escolha antes de aplicá-lo.`

---

### 8. Omissão relevante

**Detecção.** O pedido enquadra o problema ignorando uma parte interessada, um custo, um horizonte temporal ou uma restrição que tipicamente pesa naquele domínio.

**Teste.** Percorrer três eixos: quem mais é afetado; o que acontece em prazo maior; que restrição real, de recurso, prazo, legal ou técnica, não foi mencionada.

**Correção.** Incluir o eixo omitido no bloco de critérios de sucesso, ou registrar a ausência como lacuna assumida no bloco de premissas. Não expandir o escopo da tarefa por conta própria.

---

### 9. Falso consenso

**Detecção.** Apelo a acordo generalizado sem fonte: `é consenso que`, `todo mundo sabe`, `está comprovado que`, `as melhores práticas dizem`.

**Teste.** Existe fonte identificável? O ponto é de fato pacífico no domínio?

**Correção.** Exigir atribuição, ou reclassificar como hipótese de trabalho. Em tarefas com risco factual, acrescentar ao prompt a obrigação de distinguir consenso estabelecido de posição majoritária e de posição contestada.

---

## Bloco padrão de disciplina epistêmica

Para tarefas de análise, diagnóstico, pesquisa ou avaliação com risco factual médio ou alto:

```
<disciplina_epistemica>
Distinga com clareza o que é fato verificável, o que é inferência sua, o que é hipótese e o que é opinião, marcando cada afirmação quando a diferença importar para a decisão.
Use apenas as informações fornecidas em <contexto> e <entrada>. Quando faltar informação necessária, diga exatamente o que falta em vez de completar.
Quando houver interpretações concorrentes plausíveis, apresente a mais forte de cada lado antes de concluir.
Não trate como consenso aquilo que não for demonstrável; quando citar posição majoritária, identifique de quem é.
</disciplina_epistemica>
```

Ajustar a extensão à tarefa: em pedidos simples, duas linhas bastam. O bloco inteiro em tarefa trivial é o mesmo erro que ele pretende evitar.

---

## Bloco padrão contra alucinação factual

Para tarefas cuja saída depende de fatos externos ao contexto fornecido:

```
<tratamento_de_incerteza>
Responda apenas com base no material fornecido. Não complete lacunas com conhecimento geral.
Se algum elemento necessário não constar do material, declare a ausência e siga com o restante.
Não produza números, nomes, datas, citações ou referências que não estejam no material.
Quando tiver baixa confiança em uma afirmação, sinalize.
</tratamento_de_incerteza>
```

Em tarefas com ferramenta de busca ou leitura de arquivos, acrescentar a obrigação de investigar antes de afirmar, conforme `blocos-reutilizaveis.md`.
