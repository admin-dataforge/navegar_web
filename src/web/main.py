import os
from datetime import datetime
from typing import Optional

from playwright.async_api import async_playwright

from web.navegacion.pagination import click_next_page, has_next_page

# paquetes del desarrollo
from web.navegacion.render import get_rendered_html
from web.navegacion.scroll import scroll_page

# configurar el screping para una pagina


async def scrape_single_page(url, page, page_number: int):
    """Realiza scroll y guarda HTML de una página específica"""
    # Esperar contenido inicial
    await page.wait_for_selector(".property-card__container")

    # Scroll para cargar todo
    await scroll_page(page)

    # Obtener HTML renderizado
    html = await get_rendered_html(page)

    # Guardar archivo
    fecha = datetime.now().strftime("%Y-%m-%d")
    from urllib.parse import urlparse

    dominio = urlparse(url).netloc.replace("www.", "")
    path = f"data/raw/{dominio}/{fecha}"
    os.makedirs(path, exist_ok=True)

    file_path = f"{path}/pagina_{page_number}_rendered.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Página {page_number} guardada en: {file_path}")
    return True


async def main(url, max_pages: Optional[int] = None):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()

        await page.goto(url)

        page_number = 1

        while True:
            print(f"\n📄 Procesando página {page_number}...")

            # Scraping de la página actual
            await scrape_single_page(url, page, page_number)

            # Validar límite de páginas
            if max_pages and page_number >= max_pages:
                print(f"✋ Límite de páginas alcanzado: {max_pages}")
                break

            # Verificar si hay siguiente página
            has_next = await has_next_page(page)
            if not has_next:
                print("✅ No hay más páginas disponibles")
                break

            # Ir a siguiente página
            await click_next_page(page)
            page_number += 1

        await browser.close()
