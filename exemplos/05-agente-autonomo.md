# Agente autônomo de longa duração

## Entrada

> quero que o Claude Code migre sozinho os testes do meu projeto python de unittest pra pytest enquanto eu durmo, sem quebrar nada

## Resposta da skill

Saída integral, sem edição. Modelo: `claude-opus-5` · Claude Code `claude -p` · 17/10/2026.

**DIAGNÓSTICO**

Tarefa agêntica de migração de código, em execução desatendida e sem possibilidade de pergunta durante o percurso: o prompt precisa carregar antecipadamente toda a política de decisão que você daria ao vivo. O ponto que mais condiciona a qualidade é que "sem quebrar nada" só é verificável se existir uma linha de base coletada **antes** de qualquer conversão — e coletada pelo próprio pytest, que já executa classes `unittest.TestCase` nativamente, o que torna a comparação antes/depois do mesmo tipo. O segundo ponto é a precedência: em trabalho autônomo, a pressão por completar 100% dos arquivos é o que produz suíte quebrada, então o prompt declara que arquivo não convertido é resultado aceitável e teste quebrado não é. Arquitetura agêntica com procedimento por arquivo, reversão local em caso de divergência e condições de parada enumeradas.

**PROMPT FINAL**

```
Migre a suíte de testes deste projeto Python de unittest para pytest.

Estou dormindo e não vou responder a nada durante a execução. Tome as decisões necessárias, registre cada uma e siga até concluir. Não interrompa o trabalho para pedir confirmação nem para relatar progresso no meio do caminho: só volte a falar comigo no relatório final.

<precedencia>
Preservar o comportamento da suíte vale mais do que concluir a migração. Um arquivo que ficou sem converter, com o motivo anotado, é um resultado aceitável. Um teste que passou a falhar, que deixou de ser coletado ou que virou skip silencioso não é.
</precedencia>

<linha_de_base>
Antes de alterar qualquer arquivo de teste:

1. Descubra como a suíte roda hoje, procurando por pytest.ini, setup.cfg, pyproject.toml, tox.ini, Makefile, configuração de CI, README e dependências de desenvolvimento. Identifique o gerenciador de ambiente do projeto e use o ambiente que já existe.
2. Garanta que pytest está disponível. Se não estiver, instale-o apenas nas dependências de desenvolvimento e registre essa alteração.
3. Rode a suíte completa pelo comando atual do projeto e salve a saída bruta em arquivo.
4. Rode a suíte completa pelo pytest, sem converter nada, e salve a saída bruta em arquivo. Compare os dois conjuntos de testes coletados: se o pytest coletar menos testes, ajuste apenas a configuração de coleta, como conftest.py, testpaths ou rootdir, até os conjuntos coincidirem, e registre o que ajustou.
5. A execução do pytest sobre o código ainda em unittest é a linha de base. Registre, por nome, todos os testes coletados e o resultado de cada um, incluindo os que já falham, os que são pulados e os marcados como esperados a falhar.
6. Se não conseguir estabelecer essa linha de base, pare aqui, não altere nenhum arquivo de teste e escreva o relatório explicando o que impediu.
7. Se o projeto está sob git, crie um branch novo para o trabalho. Se não está, copie a árvore de testes para um diretório de backup antes de começar.
</linha_de_base>

<migracao>
Trabalhe arquivo por arquivo, cobrindo todos os arquivos de teste do projeto e não apenas o primeiro. Para cada arquivo:

- Converta classes que herdam de unittest.TestCase em funções de teste simples; assert do Python no lugar dos métodos assertAlgo; fixtures do pytest no lugar de setUp, tearDown, setUpClass e tearDownClass; pytest.raises no lugar de assertRaises; pytest.mark.parametrize no lugar de subTest e de laços sobre listas de casos; monkeypatch ou unittest.mock conforme o estilo que o arquivo já usa.
- Preserve o estado de cada teste pulado ou esperado a falhar, com o marcador equivalente do pytest e a mesma condição.
- Mantenha os nomes dos testes reconhecíveis. Quando um nome mudar, anote o mapeamento de antes e depois.
- Rode apenas os testes desse arquivo e compare com a linha de base: os mesmos testes devem existir, com o mesmo resultado.
- Se houver qualquer divergência, desfaça a conversão desse arquivo, devolva-o ao estado original e anote o motivo.
- Commite o arquivo convertido isoladamente, adicionando ao commit apenas os caminhos que você mesmo alterou, nunca o diretório inteiro.

Arquivos de apoio da suíte, como helpers e fábricas de dados usados só pelos testes, podem ser adaptados quando a conversão exigir.
</migracao>

<regras>
- Não altere código de produção. Se um teste só passa no pytest mediante mudança em código de produção, deixe o arquivo sem converter e descreva o caso no relatório.
- Não escreva testes novos, não amplie cobertura, não refatore o que não faz parte da migração e não reformate arquivos inteiros de passagem.
- Não apague teste nenhum, mesmo que pareça redundante ou morto.
- Na configuração de CI, no Makefile e no README, troque apenas o comando de execução da suíte, e mostre o diff dessas trocas no relatório.
- Mantenha tudo local: nada de git push, git reset --hard, force de qualquer tipo, ou git checkout em arquivos que você não alterou.
- Toda afirmação sua sobre teste passando vem de saída realmente executada, nunca de inferência sobre o código. Se não rodou, diga que não rodou.
</regras>

<paradas>
Interrompa a conversão e vá direto ao relatório quando:
- a suíte completa divergir da linha de base e você não conseguir identificar qual arquivo causou a divergência, situação em que também devolve o branch ao último commit em que a suíte estava igual à linha de base;
- o mesmo obstáculo bloquear três arquivos seguidos pelo mesmo motivo, caso em que descreve o padrão em vez de insistir arquivo por arquivo;
- for preciso instalar, atualizar ou remover qualquer dependência que não seja o próprio pytest e seus plugins estritamente necessários.
</paradas>

<fechamento>
Ao terminar a conversão, rode a suíte completa uma última vez pelo pytest e compare teste por teste com a linha de base. Depois escreva o relatório em um arquivo markdown na raiz do projeto, chamado migracao-pytest.md, com estas seções:

- Resultado: nome do branch, quantidade de commits, e os números de coletados, passando, falhando e pulados na linha de base e no fim.
- Diferenças por nome: todo teste que mudou de resultado ou deixou de ser coletado, com o nome antigo e o que aconteceu. Se não houver nenhum, diga isso em uma linha.
- Arquivos convertidos: a lista.
- Arquivos não convertidos: cada um com o motivo em uma frase.
- Mudanças fora dos arquivos de teste: configuração, dependências, CI, documentação, com o diff de cada uma.
- Nomes de teste alterados: o mapeamento, quando houver.
- Decisões que precisam de mim: o que você resolveu por conta própria e que eu talvez queira revisar.

Encerre sua última mensagem com um resumo de no máximo cinco linhas e o caminho do relatório. Escreva em português do Brasil.
</fechamento>
```

**PREMISSAS / LACUNAS**

- `assumido` — Migração idiomática completa, não apenas troca do executor: classes convertidas em funções com assert e fixtures. O caminho de menor risco (só trocar o comando de execução) está em Ajustes opcionais.
- `assumido` — Escopo é a suíte inteira, com reversão por arquivo em caso de divergência.
- `assumido` — Commits locais em branch novo, sem push, e instalação de pytest permitida nas dependências de desenvolvimento.
- `assumido` — A linha de base é medida com pytest sobre o código ainda em unittest, para que antes e depois sejam comparáveis.
- `indefinido` — Se o CI precisa continuar verde na mesma execução: o prompt troca o comando e mostra o diff, mas não valida o pipeline.
- `indefinido` — Modelo e nível de esforço. O prompt foi escrito para rodar igual em Opus 5.5 e Sonnet 5.5, com escopo por extenso e exigência de verificação real.

**AJUSTES OPCIONAIS**

Variante de risco mínimo, se você preferir acordar com a suíte rodando em pytest sem reescrita de estilo: troque o bloco `<migracao>` por

```
Não reescreva os testes. Faça o pytest executar a suíte unittest existente: ajuste a configuração de coleta, converta o comando de execução no CI, Makefile e README, e adote como pytest os plugins estritamente necessários para que todos os testes da linha de base continuem coletados e com o mesmo resultado. Ao fim, liste quais arquivos seriam candidatos a conversão idiomática futura e qual o obstáculo de cada um.
```

Para repositórios com suíte lenta, acrescente ao bloco `<linha_de_base>` uma linha pedindo que registre também o tempo total de execução, e ao `<fechamento>` a comparação desse tempo — regressão de tempo é a forma de quebra que passa despercebida numa comparação só de resultados.

---

## O que observar

- **Arquitetura G para execução sem supervisão.** O prompt carrega de antemão toda a política de decisão: o usuário está dormindo e não pode responder no meio da tarefa.
- **`Sem quebrar nada` virou critério verificável.** Linha de base coletada pelo próprio pytest antes de qualquer conversão, comparação teste a teste e reversão por arquivo em caso de divergência.
- **Precedência declarada.** Arquivo não convertido é resultado aceitável; teste quebrado não é. Isso resolve o conflito entre completar e preservar.
- **Política para ações irreversíveis e critério de parada.** Sem push, sem reset, sem alterar código de produção, e três condições enumeradas de interrupção.
- **Verificação real, não inferida.** `Toda afirmação sobre teste passando vem de saída realmente executada` é a calibração para modelos que, em esforço baixo, declaram pronto sem rodar.
