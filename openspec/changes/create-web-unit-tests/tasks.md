## 1. Setup

- [x] 1.1 Add pytest and pytest-asyncio to pyproject.toml dependencies
- [x] 1.2 Create test directory structure in src/web/

## 2. Config Tests

- [x] 2.1 Create test_utilidades_config.py with leer_config tests
- [x] 2.2 Test successful YAML loading
- [x] 2.3 Test FileNotFoundError for missing file
- [x] 2.4 Test ValueError for directory path

## 3. Render Tests

- [x] 3.1 Create test_navegacion_render.py with get_rendered_html tests
- [x] 3.2 Test HTML expansion of Shadow DOM
- [x] 3.3 Test returning document outerHTML

## 4. Scroll Tests

- [x] 4.1 Create test_navegacion_scroll.py with scroll_page tests
- [x] 4.2 Test scrolling stops when no new content loads
- [x] 4.3 Test early exit after 3 consecutive no-change scrolls

## 5. Finalization

- [x] 5.1 Run tests and verify all pass
- [x] 5.2 Verify code coverage >80%