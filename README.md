# web - Scraper de Propiedades

Scraper de propiedades basado en Playwright que extrae HTML renderizado de páginas web de bienes raíces.

## Descripción

Este proyecto utiliza Playwright para navegar páginas web de propiedades, realizar scroll infinito para cargar todo el contenido, y guardar el HTML completamente renderizado (incluyendo Shadow DOM expandido) para su posterior análisis.

## Requisitos

- Python 3.9+
- Playwright
- pytest (para pruebas)

## Instalación

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -e .

# Instalar navegadores de Playwright
playwright install chromium
```

## Uso

```python
import asyncio
from web.main import main

asyncio.run(main("https://ejemplo.com/propiedades"))
```

O desde la línea de comandos:

```bash
python -m web.main "https://ejemplo.com/propiedades"
```

El script guardará el HTML renderizado en `data/raw/<dominio>/YYYY-MM-DD/pagina_1_rendered.html`.

## scroll_page

Función located in `src/web/navegacion/scroll.py`.

### Parámetros

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `page` | Playwright Page | - | Objeto de página de Playwright |
| `scroll_delay_min_ms` | int | 500 | Delay mínimo entre scrolls (ms) |
| `scroll_delay_max_ms` | int | 2000 | Delay máximo entre scrolls (ms) |
| `wheel_delta_min` | int | 500 | Delta mínimo de scroll (px) |
| `wheel_delta_max` | int | 3000 | Delta máximo de scroll (px) |
| `max_scrolls` | int | 30 | Máximo número de scrolls |
| `no_change_threshold` | int | 3 | Consecutivos sin cambio antes de parar |

### Uso

```python
# Uso por defecto (comportamiento humano)
await scroll_page(page)

# Configuración personalizada (más rápido)
await scroll_page(
    page,
    scroll_delay_min_ms=250,
    scroll_delay_max_ms=500,
    wheel_delta_min=1000,
    wheel_delta_max=1500,
)

# Modo determinista (para testing)
await scroll_page(
    page,
    scroll_delay_min_ms=100,
    scroll_delay_max_ms=100,  # Fijo
    wheel_delta_min=2000,
    wheel_delta_max=2000,  # Fijo
)
```

## Estructura del Proyecto

```
├── README.md
├── pyproject.toml
├── src/
│   └── web/
│       ├── __init__.py
│       ├── main.py              # Punto de entrada
│       ├── navegacion/
│       │   ├── __init__.py
│       │   ├── scroll.py        # Scroll infinito
│       │   └── render.py        # Extracción de HTML renderizado
│       └── utilidades/
│           ├── __init__.py
│           └── config.py        # Configuración
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_navegacion_scroll.py
│   ├── test_navegacion_render.py
│   └── test_utilidades_config.py
└── data/                        # Carpeta para datos de salida
```

## Pruebas

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar pruebas específicas
pytest tests/test_navegacion_scroll.py
pytest tests/test_navegacion_render.py
```

## Autor

Luis Diaz
