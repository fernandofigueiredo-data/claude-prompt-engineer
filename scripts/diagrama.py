#!/usr/bin/env python3
"""Gera docs/metodologia.svg e docs/metodologia-dark.svg a partir das seis etapas do SKILL.md."""

from pathlib import Path

ETAPAS = [
    ("1", "Entender", ["resultado observável", "consumidor e modo", "de uso · arquétipo"]),
    ("2", "Diagnosticar", ["lacunas · ambiguidades", "premissas · alucinação", "conflitos · 9 vieses"]),
    ("3", "Estruturar", ["9 blocos canônicos;", "só entra o bloco", "que muda a saída"]),
    ("4", "Projetar", ["7 arquiteturas, do", "direto ao agêntico,", "calibradas por modelo"]),
    ("5", "Testar", ["10 testes de", "robustez; falhou em", "um, reescreve"]),
    ("6", "Entregar", ["diagnóstico", "prompt final", "premissas · ajustes"]),
]

TEMAS = {
    "metodologia.svg": dict(texto="#1f2328", suave="#59636e", caixa="#f6f8fa", borda="#d0d7de",
                            destaque="#c15f3c", destaque_fundo="#fbeee8", linha="#8c959f"),
    "metodologia-dark.svg": dict(texto="#e6edf3", suave="#9198a1", caixa="#161b22", borda="#3d444d",
                                 destaque="#e08a68", destaque_fundo="#2b1d17", linha="#6e7681"),
}

L, ESP, X0, Y0, A = 122, 18, 4, 34, 112


def svg(c: dict) -> str:
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 832 252" width="832" height="252" '
         f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" '
         f'role="img" aria-labelledby="t d">',
         '<title id="t">Metodologia da skill engenharia-de-prompt</title>',
         '<desc id="d">Seis etapas em sequência: entender, diagnosticar, estruturar, projetar, testar e entregar. '
         'Lacuna bloqueante no diagnóstico interrompe o fluxo com até três perguntas fechadas. '
         'Falha em um dos dez testes devolve o rascunho à etapa de projeto.</desc>',
         f'<defs><marker id="s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         f'<path d="M0 0L10 5L0 10z" fill="{c["linha"]}"/></marker></defs>',
         f'<text x="{X0}" y="18" font-size="12" fill="{c["suave"]}">Etapas 1 a 5 são internas · '
         f'só a etapa 6 aparece na resposta</text>']
    for i, (num, titulo, linhas) in enumerate(ETAPAS):
        x = X0 + i * (L + ESP)
        final = i == len(ETAPAS) - 1
        fundo, borda = (c["destaque_fundo"], c["destaque"]) if final else (c["caixa"], c["borda"])
        p.append(f'<rect x="{x}" y="{Y0}" width="{L}" height="{A}" rx="10" fill="{fundo}" stroke="{borda}" stroke-width="1.2"/>')
        p.append(f'<circle cx="{x + 18}" cy="{Y0 + 20}" r="10" fill="{c["destaque"]}"/>')
        p.append(f'<text x="{x + 18}" y="{Y0 + 24}" font-size="11.5" font-weight="700" fill="#fff" text-anchor="middle">{num}</text>')
        p.append(f'<text x="{x + 34}" y="{Y0 + 25}" font-size="13" font-weight="700" fill="{c["texto"]}">{titulo}</text>')
        for j, linha in enumerate(linhas):
            p.append(f'<text x="{x + 10}" y="{Y0 + 56 + j * 17}" font-size="10.5" fill="{c["suave"]}">{linha}</text>')
        if not final:
            xa = x + L + 2
            p.append(f'<line x1="{xa}" y1="{Y0 + A / 2}" x2="{xa + ESP - 4}" y2="{Y0 + A / 2}" stroke="{c["linha"]}" stroke-width="1.4" marker-end="url(#s)"/>')
    # Desvio: lacuna bloqueante na etapa 2.
    x2 = X0 + (L + ESP) + L / 2
    p.append(f'<line x1="{x2}" y1="{Y0 + A}" x2="{x2}" y2="{Y0 + A + 34}" stroke="{c["linha"]}" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#s)"/>')
    p.append(f'<rect x="{x2 - 96}" y="{Y0 + A + 38}" width="250" height="44" rx="8" fill="none" stroke="{c["borda"]}" stroke-dasharray="4 3"/>')
    p.append(f'<text x="{x2 - 84}" y="{Y0 + A + 56}" font-size="11" font-weight="600" fill="{c["texto"]}">Lacuna bloqueante?</text>')
    p.append(f'<text x="{x2 - 84}" y="{Y0 + A + 72}" font-size="10.5" fill="{c["suave"]}">até 3 perguntas fechadas, e o fluxo para</text>')
    # Retorno: falha nos testes volta ao projeto.
    x4 = X0 + 3 * (L + ESP) + L / 2
    x5 = X0 + 4 * (L + ESP) + L / 2
    yb = Y0 + A
    p.append(f'<path d="M{x5} {yb} V{yb + 30} H{x4} V{yb + 6}" fill="none" stroke="{c["linha"]}" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#s)"/>')
    p.append(f'<text x="{(x4 + x5) / 2}" y="{yb + 46}" font-size="10.5" fill="{c["suave"]}" text-anchor="middle">falhou em um teste: reescreve</text>')
    p.append('</svg>')
    return "\n".join(p) + "\n"


destino = Path(__file__).resolve().parent.parent / "docs"
for nome, cores in TEMAS.items():
    (destino / nome).write_text(svg(cores), encoding="utf-8")
    print(f"docs/{nome}")
