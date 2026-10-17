# Como contribuir

Contribuições são bem-vindas, desde que preservem o princípio central da skill: cada instrução precisa mudar a saída do modelo, e cada regra de calibração precisa de fonte.

## Ajuste de calibração por modelo

O comportamento dos modelos muda entre versões, e esta é a parte que mais envelhece.

1. Abra uma issue ou PR citando a página oficial da Anthropic que sustenta a mudança, com a data em que você a consultou.
2. Edite `plugins/engenharia-de-prompt/skills/engenharia-de-prompt/references/calibracao-por-modelo.md`, mantendo a regra por modelo e atualizando a tabela de decisão e a seção de fontes.
3. Se a mudança alterar o resumo do `SKILL.md` ou de `instrucoes/INSTRUCOES-PROJECT-COWORK.md`, atualize os três arquivos no mesmo PR, para que nenhum deles contradiga os outros.
4. Observações pessoais sem fonte entram como pergunta na issue, não como regra.

## Novo exemplo

1. Rode a skill sobre uma entrada nova, preferencialmente de um arquétipo ou arquitetura ainda não coberto em `exemplos/`.
2. Crie `exemplos/NN-nome-curto.md` no mesmo formato dos existentes: entrada, comando usado, saída integral sem edição, modelo e data, e uma nota curta sobre quais regras aparecem.
3. Acrescente uma linha na tabela de `exemplos/README.md`.

## Antes de abrir o PR

```bash
python3 scripts/validar.py
claude plugin validate .
```

Os dois rodam no CI. Atualize o `CHANGELOG.md` na seção de próxima versão.

## Estilo

Português do Brasil, prosa direta, instrução positiva. Blocos de prompt dentro de bloco de código. Sem caixa alta para ênfase, pela mesma razão que a skill proíbe isso nos prompts que gera.
