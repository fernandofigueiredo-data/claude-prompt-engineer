#!/usr/bin/env python3
"""Confere a integridade do repositório: manifestos, frontmatter da skill e links internos.

Uso: python3 scripts/validar.py
Sai com código 1 e lista os problemas se alguma verificação falhar.
"""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLUGIN = RAIZ / "plugins" / "engenharia-de-prompt"
SKILL = PLUGIN / "skills" / "engenharia-de-prompt"

erros: list[str] = []
verificacoes = 0


def checar(condicao: bool, mensagem: str) -> None:
    global verificacoes
    verificacoes += 1
    if not condicao:
        erros.append(mensagem)


def ler_json(caminho: Path) -> dict:
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as erro:
        checar(False, f"{caminho.relative_to(RAIZ)}: JSON inválido ({erro})")
        return {}


def frontmatter(texto: str) -> dict[str, str]:
    bloco = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not bloco:
        return {}
    campos = {}
    for linha in bloco.group(1).splitlines():
        chave, _, valor = linha.partition(":")
        campos[chave.strip()] = valor.strip().strip('"')
    return campos


# Manifestos: nomes coerentes entre marketplace e plugin.
marketplace = ler_json(RAIZ / ".claude-plugin" / "marketplace.json")
plugin = ler_json(PLUGIN / ".claude-plugin" / "plugin.json")
entradas = {p.get("name"): p for p in marketplace.get("plugins", [])}
checar("engenharia-de-prompt" in entradas, "marketplace.json não lista o plugin engenharia-de-prompt")
checar(plugin.get("name") == "engenharia-de-prompt", "plugin.json: name diferente da entrada do marketplace")
fonte = entradas.get("engenharia-de-prompt", {}).get("source", "")
checar((RAIZ / fonte).resolve() == PLUGIN, f"marketplace.json: source '{fonte}' não aponta para {PLUGIN.relative_to(RAIZ)}")
checar(bool(re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", ""))), "plugin.json: version fora do formato x.y.z")

# Frontmatter da skill: limites aceitos pelo carregador de skills.
texto_skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
campos = frontmatter(texto_skill)
checar(campos.get("name") == "engenharia-de-prompt", "SKILL.md: name ausente ou diferente da pasta")
descricao = campos.get("description", "")
checar(0 < len(descricao) <= 1024, f"SKILL.md: description com {len(descricao)} caracteres (limite 1024)")

# Toda referência citada no SKILL.md existe, e toda referência existente é citada.
citadas = set(re.findall(r"`(references/[\w.-]+\.md)`", texto_skill))
existentes = {f"references/{p.name}" for p in (SKILL / "references").glob("*.md")}
for ref in sorted(citadas - existentes):
    checar(False, f"SKILL.md cita {ref}, que não existe")
for ref in sorted(existentes - citadas):
    checar(False, f"{ref} existe mas não é citada no SKILL.md")
checar(bool(citadas), "SKILL.md não cita nenhuma referência")

# Links relativos em Markdown resolvem para arquivos ou pastas reais.
LINK = re.compile(r"\]\(([^)\s]+)\)|(?:src|srcset|href)=\"([^\"]+)\"")
for md in sorted(RAIZ.rglob("*.md")):
    if ".git" in md.parts:
        continue
    conteudo = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
    for grupos in LINK.findall(conteudo):
        alvo = next(g for g in grupos if g)
        if re.match(r"^(https?:|mailto:|#)", alvo):
            continue
        caminho = (md.parent / alvo.split("#")[0]).resolve()
        checar(caminho.exists(), f"{md.relative_to(RAIZ)}: link quebrado para {alvo}")

if erros:
    print(f"{len(erros)} problema(s) em {verificacoes} verificações:")
    for erro in erros:
        print(f"  ✗ {erro}")
    sys.exit(1)
print(f"✔ {verificacoes} verificações, nenhum problema")
