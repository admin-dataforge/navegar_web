## Context

The current `scroll_page()` function in `src/web/navegacion/scroll.py` uses:
- Fixed 5000ms timeout after each scroll
- Fixed 2000px wheel delta per scroll
- Perfectly predictable timing between scrolls

This mechanical pattern is easily detectable by anti-bot systems.

## Goals / Non-Goals

**Goals:**
- Add random delays between scroll operations (500ms-2000ms range)
- Add random variation to wheel delta (500px-3000px range)
- Make timing configurable without code changes
- Keep backward compatibility with existing behavior

**Non-Goals:**
- Not adding anti-detection measures beyond timing
- Not modifying the scroll stop detection logic
- Not changing the core scrolling algorithm

## Decisions

1. **Random delay implementation**: Use Python's `random.uniform()` for delay range
   - Alternative: Could use numpy random, butstdlib is sufficient
   - Decision: Use `random.uniform(min_ms, max_ms) / 1000` for seconds

2. **Wheel delta randomization**: Use `random.randint(min, max)` for integer pixels
   - Default range: 500-3000 (instead of fixed 2000)
   - Can be configured via parameters

3. **Configuration approach**: Add configurable parameters to function signature
   - `scroll_delay_min_ms`: Minimum delay (default: 500)
   - `scroll_delay_max_ms`: Maximum delay (default: 2000)
   - `wheel_delta_min`: Minimum wheel delta (default: 500)
   - `wheel_delta_max`: Maximum wheel delta (default: 3000)

## Risks / Trade-offs

- [Risk]: Slower overall execution → [Mitigation]: Configurable ranges allow tuning for use case
- [Risk]: Too much randomness may cause scroll to miss content → [Mitigation]: Default ranges are conservative
- [Risk]: Backward compatibility → [Mitigation]: Use sensible defaults that match roughly the original timing
