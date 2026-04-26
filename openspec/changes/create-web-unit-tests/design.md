## Context

The web module (`src/web/`) contains three Python modules:
- `navegacion/render.py` - Async function to expand Shadow DOM and get rendered HTML
- `navegacion/scroll.py` - Async function to scroll a page and load property cards
- `utilidades/config.py` - Sync function to read YAML configuration files

Currently there are no tests. All functions are either async (Playwright page operations) or sync (file I/O).

## Goals / Non-Goals

**Goals:**
- Add unit tests for all public functions in the web module
- Achieve >80% code coverage
- Enable CI/CD testing

**Non-Goals:**
- Integration tests (require browser/Playwright)
- End-to-end tests
- Performance/load testing

## Decisions

1. **Pytest as test framework**
   - Chosen for simplicity, async support via `pytest-asyncio`, and ecosystem
   - Alternative: `unittest` (built-in but less flexible)

2. **Mocking strategy for async functions**
   - Use `unittest.mock.AsyncMock` for Playwright page operations
   - Test behavior, not implementation details

3. **Test organization**
   - Tests colocated with modules: `src/web/navegacion/test_render.py`
   - Follows Python convention (`test_<module>.py`)

4. **Config tests use temporary files**
   - Use `tempfile` for isolation
   - Test both success and error cases (file not found, invalid YAML)

## Risks / Trade-offs

- [Risk] Async mocking complexity → [Mitigation] Use pytest-asyncio with properly configured mocks
- [Risk] Code with hard-to-test dependencies → [Mitigation] Refactor if needed to improve testability