#!/bin/bash

set -e

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
VENV_DIR="$PROJECT_ROOT/.venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Entorno virtual no encontrado en .venv"
    exit 1
fi

RUFF="$VENV_DIR/bin/ruff"
MYPY="$VENV_DIR/bin/mypy"

cd "$PROJECT_ROOT"

echo "🔍 Ejecutando verificaciones de calidad..."
echo ""

echo "📋 Ruff: Verificando estilo y errores..."
$RUFF check . || { echo "❌ Ruff encontró errores"; exit 1; }

echo "📋 Ruff: Verificando formato..."
$RUFF format --check . || { echo "❌ Hay archivos que necesitan formato. Ejecuta: ruff format ."; exit 1; }

echo "📋 Mypy: Verificando tipos..."
$MYPY src/ || { echo "❌ Mypy encontró errores de tipo"; exit 1; }

echo ""
echo "✅ All checks passed!"
exit 0