## Why

Currently, the scroll function executes with perfect mechanical timing - fixed delays and consistent wheel movements. This predictable pattern can be detected by anti-bot systems. Adding configurable random timers and randomized scroll behavior will simulate human scrolling patterns.

## What Changes

- **Modify** `src/web/navegacion/scroll.py`: Add random delays and randomized wheel delta
- Add configurable timing parameters for human-like behavior
- Add random variation to scroll wheel amount

## Capabilities

### New Capabilities
- `scroll-human-timers`: Random delays between scroll operations to simulate human reading/pausing behavior
- `scroll-wheel-randomization`: Random wheel delta values to mimic natural human scrolling patterns

### Modified Capabilities
- None - this is a new behavior addition

## Impact

- **Modified**: `src/web/navegacion/scroll.py`
- **Configuration**: New timing parameters in function or config section
