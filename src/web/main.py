# modulos de python
from playwright.async_api import async_playwright
from datetime import datetime
import os

# paquetes del desarrollo
from web.navegacion.render import get_rendered_html
from web.navegacion.scroll import scroll_page

async def main(URL):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()

        await page.goto(URL)

        # esperar contenido inicial
        await page.wait_for_selector(".property-card__container")

        # 🔁 scroll para cargar todo
        await scroll_page(page)

        # 💾 obtener HTML renderizado con Shadow DOM expandido
        html = await get_rendered_html(page)

        # 📦 estructura tipo data lake
        fecha = datetime.now().strftime("%Y-%m-%d")
        path = f"data/raw/metrocuadrado/{fecha}"
        os.makedirs(path, exist_ok=True)

        file_path = f"{path}/pagina_1_rendered.html"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"\n✅ HTML renderizado guardado en:\n{file_path}")

        await browser.close()