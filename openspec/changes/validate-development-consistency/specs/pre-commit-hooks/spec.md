## ADDED Requirements

### Requirement: Pre-commit installation
El sistema DEBE permitir la instalación de hooks de pre-commit en el repositorio local.

#### Scenario: Pre-commit is installed
- **WHEN** se ejecuta `pre-commit install`
- **THEN** se crea el archivo `.git/hooks/pre-commit` que ejecuta los hooks configurados

### Requirement: Ruff pre-commit hook
El sistema DEBE incluir un hook de pre-commit que ejecute ruff antes de cada commit.

#### Scenario: Ruff hook passes
- **WHEN** el código pasa las verificaciones de ruff antes de un commit
- **THEN** el commit se completa normalmente

#### Scenario: Ruff hook fails
- **WHEN** ruff encuentra errores en el código antes de un commit
- **THEN** el commit es bloqueado y se muestran los errores

### Requirement: Mypy pre-commit hook
El sistema DEBE incluir un hook de pre-commit que ejecute mypy antes de cada commit.

#### Scenario: Mypy hook passes
- **WHEN** el código pasa las verificaciones de tipo antes de un commit
- **THEN** el commit se completa normalmente

#### Scenario: Mypy hook fails
- **WHEN** mypy encuentra errores de tipo antes de un commit
- **THEN** el commit es bloqueado y se muestran los errores

### Requirement: Avoid fixing on commit
El sistema DEBE ejecutar ruff y mypy en modo check-only en pre-commit (sin auto-fix) para no modificar código automáticamente.

#### Scenario: No auto-fix during commit
- **WHEN** se ejecuta pre-commit y ruff tiene errores que podría auto-corregir
- **THEN** el hook NO modifica los archivos, solo reporta errores

### Requirement: Skip pre-commit temporarily
El sistema DEBE permitir omitir los hooks de pre-commit cuando sea necesario.

#### Scenario: Skip hooks with --no-verify
- **WHEN** se hace commit con `git commit --no-verify`
- **THEN** los hooks de pre-commit no se ejecutan y el commit se completa