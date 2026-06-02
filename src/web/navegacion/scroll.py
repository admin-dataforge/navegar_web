import asyncio
import random


async def scroll_page(
    page,
    expected_cards: int,
    scroll_delay_min_ms: int = 800,
    scroll_delay_max_ms: int = 2500,
    wheel_delta_min: int = 400,
    wheel_delta_max: int = 900,
    max_scrolls: int = 100,
    no_change_threshold: int = 8,
):
    """
    Realiza scroll hasta cargar la cantidad esperada de cards.

    Args:
        page: Página Playwright.
        expected_cards: Cantidad de cards que deberían cargarse.
        scroll_delay_min_ms: Tiempo mínimo entre scrolls.
        scroll_delay_max_ms: Tiempo máximo entre scrolls.
        wheel_delta_min: Tamaño mínimo del scroll.
        wheel_delta_max: Tamaño máximo del scroll.
        max_scrolls: Máximo número de scrolls.
        no_change_threshold: Intentos sin cambios antes de detenerse.

    Returns:
        int: Cantidad final de cards encontradas.
    """

    previous_count = 0
    no_change_count = 0

    print(f"Objetivo: {expected_cards} cards")

    for i in range(max_scrolls):

        current_count = await page.locator(
            ".property-card__container"
        ).count()

        print(
            f"Scroll {i + 1:03d} | "
            f"Cards: {current_count}/{expected_cards}"
        )

        # Se alcanzó el objetivo
        if current_count >= expected_cards:
            print(
                f"✓ Objetivo alcanzado: "
                f"{current_count}/{expected_cards}"
            )
            break

        # Validar si hubo crecimiento
        if current_count == previous_count:
            no_change_count += 1
            print(
                f"Sin cambios "
                f"({no_change_count}/{no_change_threshold})"
            )
        else:
            no_change_count = 0

        # Demasiados intentos sin cambios
        if no_change_count >= no_change_threshold:
            print(
                f"⚠ No fue posible alcanzar "
                f"{expected_cards} cards."
            )
            break

        previous_count = current_count

        # Scroll aleatorio
        wheel_delta = random.randint(
            wheel_delta_min,
            wheel_delta_max
        )

        await page.mouse.wheel(0, wheel_delta)

        # Esperar a que carguen nuevas cards
        try:
            await page.wait_for_function(
                f"""
                () => document.querySelectorAll(
                    '.property-card__container'
                ).length > {current_count}
                """,
                timeout=10000,
            )
        except:
            pass

        # Pausa aleatoria para simular usuario
        delay_ms = random.randint(
            scroll_delay_min_ms,
            scroll_delay_max_ms
        )

        await asyncio.sleep(delay_ms / 1000)

    # Scroll final hasta abajo por si queda algún lazy-load pendiente
    await page.evaluate(
        "window.scrollTo(0, document.body.scrollHeight)"
    )

    await asyncio.sleep(2)

    final_count = await page.locator(
        ".property-card__container"
    ).count()

    print(
        f"\nResultado final: "
        f"{final_count}/{expected_cards}"
    )

    return final_count