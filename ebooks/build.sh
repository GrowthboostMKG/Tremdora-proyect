#!/usr/bin/env bash
# Serie "Sigue Contigo" — genera el HTML de cada libro y lo imprime a PDF con
# Chromium headless (mismo pipeline usado en "Edad Dorada" y "Hogar en Calma").
#
#   ./build.sh          construye los tres complementos
#   ./build.sh libro4   construye solo uno
set -euo pipefail
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$DIR/pdf"

# slug            | generador          | nombre de entrega
BOOKS=(
  "libro2-diario-del-oleaje|libro2_diario.py|2. Sigue Contigo - Diario del Oleaje"
  "libro3-plan-8-semanas|libro3_plan.py|3. Sigue Contigo - Plan Practico 8 Semanas"
  "libro4-ellos-tambien-se-despiden|libro4_ellos.py|4. Sigue Contigo - Ellos Tambien se Despiden"
)

want=${1:-all}
for row in "${BOOKS[@]}"; do
  IFS='|' read -r slug gen out <<< "$row"
  [[ "$want" == "all" || "$slug" == *"$want"* ]] || continue
  ( cd "$DIR/src" && python3 "$gen" >/dev/null )
  "$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$DIR/pdf/$out.pdf" "$DIR/src/$slug.html" 2>/dev/null
  echo "OK  pdf/$out.pdf"
done

echo
python3 "$DIR/check_overflow.py" "$DIR"/src/libro*.html
