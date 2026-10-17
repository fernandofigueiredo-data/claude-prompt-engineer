# Prompt engineering for Claude (Portuguese skill)

[![validar](https://github.com/fernandofigueiredo-data/claude-prompt-engineer/actions/workflows/validar.yml/badge.svg)](https://github.com/fernandofigueiredo-data/claude-prompt-engineer/actions/workflows/validar.yml)

A Claude skill that takes a raw, vague idea and returns the prompt that produces the intended result, with the fewest instructions needed and every assumption stated. The skill, its documentation and the prompts it writes are in **Brazilian Portuguese** by default; it writes the prompt in whatever language the output should be in when you ask for it.

**What it does:** diagnoses gaps, ambiguities, hidden premises, hallucination risk and nine bias patterns before writing; asks at most three closed questions, and only when the answer would change the shape of the output; picks one of seven prompt architectures (direct, structured, example-driven, long document, persistent instruction, pipeline, agentic); runs ten robustness checks; and calibrates the text for Claude Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable 5.1, based on Anthropic's model-specific prompting guides (checked 2026-10-17). It never performs the task itself: it writes the prompt that would make a model perform it.

**Every answer has the same shape:** a short diagnosis, the final prompt in one copyable code block, the assumptions it made, and optional variants.

## Install

Claude Code plugin:

```bash
claude plugin marketplace add fernandofigueiredo-data/claude-prompt-engineer
```

```bash
claude plugin install engenharia-de-prompt@claude-prompt-engineer
```

claude.ai: download `engenharia-de-prompt.zip` from the [latest release](https://github.com/fernandofigueiredo-data/claude-prompt-engineer/releases/latest) and upload it in the Skills section of your settings.

Projects or Cowork without skills: paste [`instrucoes/INSTRUCOES-PROJECT-COWORK.md`](instrucoes/INSTRUCOES-PROJECT-COWORK.md) into the Instructions field.

## More

Full documentation, the method, real input/output examples and the model calibration notes are in the [Portuguese README](README.md) and in [`exemplos/`](exemplos/). Calibration changes need an official source with a date; see [CONTRIBUTING.md](CONTRIBUTING.md). MIT licensed.
