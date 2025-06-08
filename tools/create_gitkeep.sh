#!/bin/bash

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Directorios a procesar
directories=("src" "assets")

echo "=== Creador de archivos .gitkeep para directorios vacíos ==="
echo ""

total_created=0

# Procesar cada directorio
for dir in "${directories[@]}"; do
    find "$dir" -type d -empty -exec touch {}/.gitkeep \;
done
echo "Archivos .gitkeep creados en directorios vacíos."

# Mostrar estructura final
echo ""
echo "Estructura actual de directorios con .gitkeep:"
for dir in "${directories[@]}"; do
    if [[ -d "$dir" ]]; then
        echo -e "${YELLOW}$dir/${NC}"
        find "$dir" -name ".gitkeep" -type f 2>/dev/null | sed 's/^/  /'
    fi
done