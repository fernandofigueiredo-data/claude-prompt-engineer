# Agente autônomo de longa duração

## Entrada

> quero que o Claude Code migre sozinho os testes do meu projeto python de unittest pra pytest enquanto eu durmo, sem quebrar nada

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**

Você quer um prompt de tarefa agêntica para o Claude Code. Ele roda sem supervisão, com acesso a shell e ao git, e no fim deixa o projeto com os testes em estilo pytest e com o mesmo comportamento observável de antes. A maior dificuldade é a expressão "sem quebrar nada". Ela precisa virar um critério verificável: a mesma lista de testes passando, falhando e pulados antes e depois, e nenhuma alteração fora dos arquivos de teste. Como ninguém vai estar acordado para aprovar nada, o prompt também precisa isolar o trabalho do seu diretório atual, dizer o que fazer quando um arquivo não converte bem e definir quando parar.

**PROMPT FINAL**

```
<contexto>
Este repositório é um projeto Python cujos testes usam unittest. Quero que eles passem a usar o estilo pytest. Vou estar dormindo enquanto você trabalha e ninguém vai acompanhar em tempo real nem responder perguntas. Por isso, execute a tarefa inteira até o fim, sem parar para pedir confirmação e sem encerrar com um relato de progresso. Quando surgir uma dúvida, tome a decisão mais conservadora e registre-a no relatório final.
</contexto>

<tarefa>
Migre todos os arquivos de teste do projeto de unittest para o estilo pytest, preservando exatamente o que cada teste verifica. A migração vale para todos os arquivos de teste do repositório, não apenas para o primeiro ou para os mais simples.
</tarefa>

<isolamento>
Antes de editar qualquer coisa, crie um git worktree em um diretório irmão do repositório, a partir do commit atual, em uma branch nova chamada migracao-pytest. Faça todo o trabalho dentro desse worktree. Assim, o meu diretório de trabalho e qualquer alteração minha ainda não commitada ficam intocados.

Faça um commit por arquivo migrado, com uma mensagem que diga o nome do arquivo. Não faça push, merge, rebase nem reset em nenhuma branch existente, e não apague o worktree no final. Quero revisar tudo de manhã antes de integrar.

Se pytest não estiver instalado, instale-o no ambiente virtual do projeto. Se o projeto declarar dependências de desenvolvimento, acrescente-o à lista. Não instale nem atualize nenhum outro pacote.
</isolamento>

<linha_de_base>
1. Rode a suíte atual com o executor de testes que o projeto já usa (unittest) e salve a lista completa de identificadores de teste, cada um com seu resultado: passou, falhou, erro ou pulado.
2. Rode a mesma suíte com pytest, ainda sem alterar nada, e confirme que pytest coleta os mesmos testes. Se houver diferença, registre-a e investigue a causa antes de migrar.

Essa linha de base é a referência do critério de sucesso. Testes que já falhavam antes continuam falhando depois. Não tente corrigi-los: corrigir código de produção está fora do escopo.
</linha_de_base>

<regras_de_conversao>
Trabalhe um arquivo de teste por vez. Para cada arquivo:
- troque self.assertX por assert simples ou por pytest.raises, pytest.approx e equivalentes, mantendo os mesmos valores esperados e as mesmas condições;
- converta setUp, tearDown e setUpClass em fixtures quando a conversão for direta. Quando houver estado compartilhado entre testes, herança entre classes de teste ou ordem de execução que importe, mantenha a estrutura de classe sem herdar de TestCase e registre o motivo;
- converta subTest em parametrização somente se cada caso continuar verificando a mesma coisa. Nesse caso a contagem de testes sobe, então registre o número antigo e o novo para aquele arquivo;
- mantenha unittest.mock como está. Ele funciona normalmente com pytest.

O escopo de alteração se limita a arquivos de teste, conftest.py e à configuração do pytest, se ela for necessária. Código de produção, CI, scripts de build e documentação ficam como estão. Se algum deles precisar mudar para a migração funcionar, não altere: anote no relatório.

Cada assertion original deve continuar existindo de forma equivalente. Uma conversão só é aceitável se o teste continuar capaz de falhar nas mesmas situações em que falhava antes. Por isso, não remova assertions, não afrouxe valores esperados, não acrescente skip nem xfail e não reduza a cobertura de nenhum teste para fazê-lo passar.
</regras_de_conversao>

<verificacao_por_arquivo>
Depois de converter um arquivo, rode com pytest esse arquivo e a suíte inteira. O arquivo só é commitado quando:
- cada teste dele tem o mesmo resultado que tinha na linha de base;
- a quantidade de testes coletados é a mesma, ou a diferença se explica por subTest convertido e está registrada;
- nenhum teste de outro arquivo mudou de resultado.

Se o arquivo não cumprir essas condições depois de três tentativas de correção, descarte as alterações nele, deixe-o em unittest, registre o motivo e passe para o próximo. Um arquivo deixado em unittest é um resultado aceitável. Uma conversão que muda o comportamento de um teste não é.
</verificacao_por_arquivo>

<encerramento>
O trabalho termina quando todos os arquivos de teste tiverem sido convertidos ou registrados como mantidos. Nesse ponto:
1. rode a suíte completa com pytest uma última vez e compare o resultado com a linha de base, teste a teste;
2. crie na raiz do worktree o arquivo MIGRACAO_PYTEST.md e faça o commit dele. O arquivo deve conter:
   - os totais de testes que passaram, falharam, deram erro e foram pulados, na linha de base e no final, lado a lado;
   - os arquivos convertidos;
   - os arquivos mantidos em unittest, cada um com o motivo;
   - as mudanças na contagem de testes e a explicação de cada uma;
   - os ajustes necessários fora do escopo (CI, dependências, configuração), que você não fez;
   - os comandos para eu revisar e integrar a branch.
</encerramento>
```

**PREMISSAS / LACUNAS**

- assumido: o projeto está versionado em git e o commit atual é um bom ponto de partida.
- assumido: "estilo pytest" significa trocar a sintaxe e a estrutura dos testes, e não só passar a rodar os testes unittest com o executor pytest, que já faria isso sem mudar nada.
- assumido: existe um ambiente virtual do projeto e ele pode receber o pacote pytest.
- assumido: o modelo-alvo é Claude Opus 5.5 no Claude Code, rodando sem ninguém aprovando ações.
- indefinido: se a CI usa um comando unittest. O prompt não altera a CI, só registra o que precisaria mudar.
- indefinido: se o projeto tem testes lentos ou que dependem de rede ou banco de dados. Se tiver, a suíte completa rodada a cada arquivo pode levar a noite inteira.

**AJUSTES OPCIONAIS**

- Para rodar sem ninguém acordado, o Claude Code não pode parar esperando aprovação de comandos. Rode em modo não interativo, com permissões liberadas para editar arquivos e executar pytest, git e o gerenciador de pacotes. Por exemplo: `claude -p "$(cat prompt.txt)" --permission-mode acceptEdits`, com git, pytest e pip ou uv permitidos no `settings.json`. Sem isso, ele trava no primeiro pedido de permissão.
- Se a suíte for lenta, troque "o arquivo e a suíte inteira" por "o arquivo convertido". Mantenha a suíte completa só a cada cinco arquivos e no final.

---

## O que observar

- **Arquitetura G para execução sem supervisão.** O prompt diz que ninguém acompanha em tempo real e pede que o modelo não encerre com um relato de progresso, que é exatamente a parada indesejada documentada para Opus 5.5 em execuções sem supervisão.
- **`Sem quebrar nada` virou critério verificável.** Linha de base com resultado por teste antes de qualquer edição e comparação teste a teste depois de cada arquivo.
- **Isolamento e ações irreversíveis.** Trabalho num git worktree separado, um commit por arquivo, sem push, merge, rebase ou reset, sem tocar em código de produção.
- **Precedência e critério de parada.** Três tentativas por arquivo; depois disso o arquivo fica em unittest com o motivo registrado. Arquivo mantido é aceitável, teste com comportamento alterado não é.
- **Lacuna operacional apontada.** Nos opcionais, a skill avisa que sem permissões liberadas o Claude Code trava no primeiro pedido de aprovação.
