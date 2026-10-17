#!/usr/bin/env bash
# Gera dist/engenharia-de-prompt.zip, pronto para upload em claude.ai (área de Skills das configurações).
# O zip contém a pasta engenharia-de-prompt/ com SKILL.md e references/.
set -euo pipefail

raiz="$(cd "$(dirname "$0")/.." && pwd)"
origem="$raiz/plugins/engenharia-de-prompt/skills"
destino="$raiz/dist/engenharia-de-prompt.zip"

mkdir -p "$raiz/dist"
rm -f "$destino"
(cd "$origem" && zip -rqX "$destino" engenharia-de-prompt -x '*.DS_Store')
echo "Gerado: ${destino#"$raiz"/}"
unzip -l "$destino"
