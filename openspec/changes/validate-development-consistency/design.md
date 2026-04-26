## Context

El proyecto `navegar_web` es un scraper de propiedades Python que usa Playwright. Actualmente no tiene validación automática de calidad de código. El desarrollo es realizado por un único desarrollador (Luis Diaz), pero se busca mantener consistencia y calidad para facilitar futuras colaboraciones.

## Goals / Non-Goals

**Goals:**
- Implementar linting con ruff para verificar estilo y errores comunes
- Implementar type checking con mypy para validación de tipos estáticos
- Configurar pre-commit hooks para validación automática antes de commits
- Crear script de verificación de calidad para CI/CD

**Non-Goals:**
- Reescribir código existente para cumplir con las nuevas reglas (se permitirá que las reglas evolucionen)
- Agregar tests unitarios (ya existen con pytest)
- Implementar análisis de seguridad (fuera de scope inicial)

## Decisions

1. **Ruff vs Flake8/Pylint**: Ruff fue elegido por su velocidad (escrito en Rust) y porque combina linting, formatting e importación en una sola herramienta. Es 10-100x más rápido que herramientas tradicionales.

2. **Mypy para type checking**: Herramienta estándar de facto para Python con soporte excelente para tipos estáticos. Integración nativa con la mayoria de editores.

3. **Pre-commit para hooks**: Herramienta popular y configurable que permite definir hooks en YAML. Facilita compartir configuración entre desarrolladores.

4. **Nivel de strictness inicial**: Se usará configuración laxa inicialmente para no bloquear el desarrollo, permitiendo endurecer las reglas gradualmente.

## Risks / Trade-offs

- **[Riesgo] Falso sentido de seguridad**: Linting y type checking no reemplazan testing. → Mitigación: Mantener pytest como principal herramienta de calidad.
- **[Riesgo] Configuración demasiado permisiva**: Si las reglas son muy laxas, no aportan valor. → Mitigación: Revisar configuración después de 2 semanas de uso.
- **[Trade-off] Curva de aprendizaje**: Los desarrolladores deben instalar pre-commit y ejecutar `pre-commit install`. → Mitigación: Documentar en README.

## Migration Plan

1. Agregar dependencias al `pyproject.toml` (ruff, mypy, pre-commit)
2. Crear archivo de configuración `ruff.toml`
3. Crear `.pre-commit-config.yaml`
4. Ejecutar `pre-commit install` en el repo local
5. Correr `ruff check .` y `mypy src/` para ver estado actual
6. Ajustar reglas según resultados
7. Agregar script de verificación en CI

**Rollback**: Si hay problemas, se puede desinstalar pre-commit con `pre-commit uninstall` y remover las dependencias de `pyproject.toml`.

## Open Questions

- ¿Qué nivel de strictness queremos para mypy? (strict vs basic)
- ¿queremos integrar con GitHub Actions para CI?
- ¿Necesitamos configurar editores (VSCode, PyCharm) automáticamente?