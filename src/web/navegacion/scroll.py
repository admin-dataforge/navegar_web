import asyncio
import random


async def scroll_page(
    page,
    scroll_delay_min_ms: int = 500,
    scroll_delay_max_ms: int = 2000,
    wheel_delta_min: int = 500,
    wheel_delta_max: int = 3000,
    max_scrolls: int = 30,
    no_change_threshold: int = 3,
):
    previous_count = 0
    no_change_count = 0

    for i in range(max_scrolls):
        cards = await page.query_selector_all(".property-card__container")
        current_count = len(cards)

        print(f"Scroll {i}: {current_count}")

        if current_count == previous_count:
            no_change_count += 1
        else:
            no_change_count = 0

        if no_change_count >= no_change_threshold:
            print("No cargan más resultados")
            break

        previous_count = current_count

        if wheel_delta_max > wheel_delta_min:
            wheel_delta = random.randint(wheel_delta_min, wheel_delta_max)
        else:
            wheel_delta = wheel_delta_min

        await page.mouse.wheel(0, wheel_delta)

        try:
            await page.wait_for_function(
                f"document.querySelectorAll('.property-card__container').length > {previous_count}",
                timeout=5000,
            )
        except Exception:
            pass

        if i < max_scrolls - 1:
            current_delay_range = scroll_delay_max_ms - scroll_delay_min_ms
            if current_delay_range > 0:
                current_delay_ms = random.randint(0, current_delay_range) + scroll_delay_min_ms
            else:
                current_delay_ms = scroll_delay_min_ms
            await asyncio.sleep(current_delay_ms / 1000)
