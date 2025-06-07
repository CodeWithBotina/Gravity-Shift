#!/bin/bash

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Función para procesar cada directorio
create_gitkeep_in_empty_dirs() {
    local base_dir="$1"
    local count=0
    
    if [[ ! -d "$base_dir" ]]; then
        echo -e "${RED}Error: El directorio '$base_dir' no existe${NC}"
        return 1
    fi
    
    echo -e "${YELLOW}Procesando directorio: $base_dir${NC}"
    
    # Buscar todas las subcarpetas vacías (excluyendo .git)
    while IFS= read -r -d '' dir; do
        # Verificar si el directorio está realmente vacío (sin archivos ocultos ni visibles)
        if [[ -z "$(find "$dir" -mindepth 1 -maxdepth 1 2>/dev/null)" ]]; then
            echo "  Creando .gitkeep en: $dir"
            touch "$dir/.gitkeep"
            ((count++))
        fi
    done < <(find "$base_dir" -type d -not -path "*/.*" -print0)
    
    echo -e "${GREEN}  ✓ Archivos .gitkeep creados: $count${NC}"
    return 0
}

# Directorios a procesar
directories=("src" "assets")

echo "=== Creador de archivos .gitkeep para directorios vacíos ==="
echo ""

total_created=0

# Procesar cada directorio
for dir in "${directories[@]}"; do
    if create_gitkeep_in_empty_dirs "$dir"; then
        # Contar archivos .gitkeep creados en este directorio
        count=$(find "$dir" -name ".gitkeep" -type f 2>/dev/null | wc -l)
        total_created=$((total_created + count))
    fi
    echo ""
done

echo "=== Resumen ==="
echo -e "${GREEN}Total de archivos .gitkeep creados: $total_created${NC}"

# Mostrar estructura final
echo ""
echo "Estructura actual de directorios con .gitkeep:"
for dir in "${directories[@]}"; do
    if [[ -d "$dir" ]]; then
        echo -e "${YELLOW}$dir/${NC}"
        find "$dir" -name ".gitkeep" -type f 2>/dev/null | sed 's/^/  /'
    fi
done