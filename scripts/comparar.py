#!/usr/bin/env python3
"""Mede as saídas da comparação antes/depois do exemplo 06 com critérios conferíveis por script.

Uso: python3 scripts/comparar.py exemplos/resultados-06
A pasta contém antes-N, antes_material-N e depois-N, em .md (texto da resposta) ou .json (saída de claude -p).
Imprime uma tabela Markdown com a média e o intervalo de cada variante.
"""

import json
import re
import sys
from pathlib import Path

pasta = Path(sys.argv[1])
VARIANTES = {
    "antes": "Original",
    "antes_material": "Original + o mesmo material",
    "depois": "Revisado pela skill",
}
# Detalhes do material que só aparecem no post se ele usar o caso concreto.
DETALHES = ["47", "12", "Marta", "odontol", "WhatsApp", "4 unidades|quatro unidades", "agosto|setembro"]
# Marcas de texto fora do post: bastidores, checklist de restrições ou aviso ao autor.
FORA_DO_POST = re.compile(r"(?i)(racioc[ií]nio|verifica[çc][ãa]o|conferi|como montei|escolhas que fiz|abordagem|"
                          r"antes de publicar|\b\d+\s+palavras|limite de 150|para fugir do gen[ée]rico)")
INVENTADO = re.compile(r"(?i)(?<!não )(?<!nada )(inventei|inventad[oa]|ilustrativ|fict[ií]ci|troque pel[oa]s? |troque por uma)")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def medir(texto: str) -> dict:
    return {
        "palavras": len(re.findall(r"\w+", texto)),
        "fora_do_post": bool(FORA_DO_POST.search(texto)),
        "inventado": bool(INVENTADO.search(texto)),
        "detalhes": sum(bool(re.search(d, texto, re.I)) for d in DETALHES),
        "emoji_hashtag": bool(EMOJI.search(texto) or re.search(r"(?<!\w)#\w", texto)),
    }


linhas = ["| Variante | Palavras na resposta | Texto além do post | Caso declarado como inventado | Detalhes do relato usados (de 7) | Emoji ou hashtag |",
          "|---|---|---|---|---|---|"]
for chave, nome in VARIANTES.items():
    arquivos = sorted(p for p in pasta.glob(f"{chave}-[0-9].*") if p.suffix in (".json", ".md"))
    medidas = [medir(json.loads(p.read_text())["result"] if p.suffix == ".json" else p.read_text()) for p in arquivos]
    if not medidas:
        continue
    pal = [m["palavras"] for m in medidas]
    det = [m["detalhes"] for m in medidas]
    n = len(medidas)
    linhas.append(f"| {nome} | {round(sum(pal) / n)} ({min(pal)}–{max(pal)}) | {sum(m['fora_do_post'] for m in medidas)} de {n} | {sum(m['inventado'] for m in medidas)} de {n} "
                  f"| {f"{sum(det) / n:.1f}".replace(".", ",")} ({min(det)}–{max(det)}) | {sum(m['emoji_hashtag'] for m in medidas)} de {n} |")
print("\n".join(linhas))
