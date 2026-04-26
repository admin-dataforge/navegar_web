## Why

El proyecto carece de validación automática de consistencia en el desarrollo. Sin herramientas de linting, type checking o enforcement de convenciones, el código puede divergir en estilo y calidad con el tiempo, dificultando el mantenimiento y la colaboración.

## What Changes

- Agregar configuración de linting con ruff
- Agregar configuración de type checking con mypy
- Agregar pre-commit hooks para validación automática
- Crear script de verificación de calidad en CI

## Capabilities

### New Capabilities
- `code-quality-validation`: Sistema de validación automática de calidad de código (linting, type checking, formatting)
- `pre-commit-hooks`: Hooks de pre-commit para validar cambios antes de cada commit

### Modified Capabilities
- (Ninguno - es una adición)

## Impact

- Archivos nuevos: `pyproject.toml` (actualizado), `.pre-commit-config.yaml`, `ruff.toml`
- Scripts: Scripts de validación de calidad
- Dependencias: ruff, mypy, pre-commit
- Flujo de trabajo: Validación automática en cada commit y CI