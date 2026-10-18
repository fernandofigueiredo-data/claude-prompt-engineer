# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/); versões seguem [SemVer](https://semver.org/lang/pt-BR/). A versão vale para o plugin, a skill e o zip da Release ao mesmo tempo.

## [1.0.1] - 2026-10-17

### Adicionado
- Comparação medida em `exemplos/resultados-06/`: prompt original, original com o mesmo material e prompt revisado, três execuções cada, com as nove saídas e `scripts/comparar.py` para reproduzir a medição.

### Corrigido
- "Blocos testados" passou a "blocos prontos" no README e no SKILL.md: os blocos vêm da documentação oficial, mas não foram testados um a um neste repositório.
- Prompt "antes" do README quebrado em linhas, sem rolagem horizontal.

## [1.0.0] - 2026-10-17

### Adicionado
- Instalação como plugin do Claude Code, por marketplace próprio (`.claude-plugin/marketplace.json`).
- Zip da skill anexado a cada Release, para upload em claude.ai.
- Calibração para Claude Opus 5.5, Sonnet 5.5, Haiku 5.5 e Fable 5.1, com fontes oficiais consultadas em 17/10/2026.
- Blocos novos: busca com data, texto colado por terceiros, continuidade sem alargar escopo, verificação real em código, operação autônoma, prosa maneirista.
- Antipadrões novos: pedir o raciocínio escrito na resposta, `pense com cuidado` em chat, `use ferramentas só quando estritamente necessário`, `pesquise sempre`, `evite visual genérico de IA`.
- Exemplos com entradas e saídas reais em `exemplos/`.
- Validação automática (`scripts/validar.py` e validador oficial de plugins) a cada push.

### Alterado
- Regras de Opus 5 e Sonnet 5 passam a constar como herdadas, com indicação de quando ainda valem.
- A regra sobre verificação deixou de ser universal: remover em Opus, exigir verificação real em Sonnet 5.5 e Haiku 5.5 com esforço baixo em código.
- Instruções para Project e Cowork renomeadas para `instrucoes/INSTRUCOES-PROJECT-COWORK.md` e sincronizadas com a calibração nova.

## [0.1.0] - 2026-10-01

Primeira versão, distribuída como zip: metodologia em 6 etapas, 7 arquiteturas, 10 testes de robustez, auditoria de 9 vieses e calibração para Opus 5 e Sonnet 5 (fontes de 17/09/2026).
