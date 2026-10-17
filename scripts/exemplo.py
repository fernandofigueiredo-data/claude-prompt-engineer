#!/usr/bin/env python3
"""Converte a saída JSON de `claude -p --output-format json` num arquivo de exemplo em exemplos/.

Uso: python3 scripts/exemplo.py <saida.json> <exemplos/NN-nome.md> "<título>" "<entrada>" "<nota>"
A resposta da skill é copiada sem edição.
"""

import json
import sys
from datetime import date
from pathlib import Path

saida, destino, titulo, entrada, nota = sys.argv[1:6]
dados = json.loads(Path(saida).read_text(encoding="utf-8"))
if dados.get("is_error") or dados.get("subtype") != "success":
    sys.exit(f"{saida}: execução sem sucesso ({dados.get('subtype')})")

modelos = ", ".join(f"`{m}`" for m in dados.get("modelUsage", {})) or "não informado"
citacao = "\n".join(f"> {linha}" if linha else ">" for linha in entrada.splitlines())

Path(destino).write_text(f"""# {titulo}

## Entrada

{citacao}

## Resposta da skill

Saída integral, sem edição. Modelo: {modelos} · Claude Code `claude -p` · {date.today():%d/%m/%Y}.

{dados["result"].strip()}

---

## O que observar

{nota}
""", encoding="utf-8")
print(destino)
