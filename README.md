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
