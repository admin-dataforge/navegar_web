## ADDED Requirements

### Requirement: Linting with Ruff
El sistema DEBE ejecutar ruff para validar el código Python en cada verificación de calidad.

#### Scenario: Ruff reports no errors
- **WHEN** se ejecuta `ruff check .` sin configuración adicional
- **THEN** el comando termina con código de salida 0 y no muestra errores

#### Scenario: Ruff detects style violations
- **WHEN** ruff encuentra violaciones de estilo (e.g., import no usado, variable no usada)
- **THEN** muestra los errores con ubicación exacta (archivo:línea) y código de error

### Requirement: Type checking with Mypy
El sistema DEBE ejecutar mypy para validar tipos estáticos en el código Python.

#### Scenario: Mypy passes type checking
- **WHEN** se ejecuta `mypy src/` en código sin errores de tipo
- **THEN** el comando termina con código de salida 0

#### Scenario: Mypy detects type errors
- **WHEN** mypy encuentra errores de tipo (e.g., tipo incompatible)
- **THEN** muestra el error con archivo, línea, y descripción del problema

### Requirement: Code formatting check
El sistema DEBE verificar que el código cumple con las reglas de formato configuradas.

#### Scenario: Code is properly formatted
- **WHEN** se ejecuta `ruff format --check .` en código formateado
- **THEN** el comando termina con código de salida 0

#### Scenario: Code needs formatting
- **WHEN** el código no cumple con el formato de ruff
- **THEN** el comando muestra las diferencias y sugiere formatear con `ruff format .`

### Requirement: Quality check script
El sistema DEBE proporcionar un script unificado que ejecute todas las verificaciones de calidad.

#### Scenario: Quality check passes
- **WHEN** se ejecuta el script de verificación y todo el código cumple las reglas
- **THEN** el script termina con código de salida 0 y muestra "All checks passed"

#### Scenario: Quality check fails
- **WHEN** al menos una verificación falla
- **THEN** el script termina con código de salida 1 y muestra qué verificaciones fallaron