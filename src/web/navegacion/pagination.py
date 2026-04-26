import asyncio


async def has_next_page(page):
    """Verifica si existe botón 'siguiente página'"""
    try:
        next_button = await page.query_selector(
            'button[aria-label="next page"].rc-pagination-item-link'
        )
        is_disabled = await next_button.is_disabled()
        return next_button is not None and not is_disabled
    except Exception:
        return False


async def click_next_page(page, delay_ms: int = 2000):
    """Hace clic al botón de siguiente página"""
    try:
        await page.click('button[aria-label="next page"].rc-pagination-item-link')
        # Esperar a que se cargue la nueva página
        await asyncio.sleep(delay_ms / 1000)
        return True
    except Exception as e:
        print(f"❌ Error al hacer clic en siguiente página: {e}")
        return False
