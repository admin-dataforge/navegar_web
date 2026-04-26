## Why

The web module currently has no test coverage. Without unit tests, any code changes risk introducing regressions, and it's difficult to refactor with confidence. Adding unit tests will improve code quality and enable continuous integration.

## What Changes

- Add pytest-based unit tests for all modules in `src/web/`
- Create tests for `navegacion/render.py`, `navegacion/scroll.py`, and `utilidades/config.py`
- Add pytest configuration and dependencies

## Capabilities

### New Capabilities
- `web-unit-tests`: Comprehensive unit tests covering all public functions in the web module

### Modified Capabilities
- None

## Impact

- New test files in `src/web/` directory
- New `pytest` dependency in `pyproject.toml`