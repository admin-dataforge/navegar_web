async def get_rendered_html(page):
    # 🔥 Expandir Shadow DOM
    html = await page.evaluate("""
    () => {
        function expand(element) {
            if (element.shadowRoot) {
                element.innerHTML = element.shadowRoot.innerHTML;
            }
            element.querySelectorAll('*').forEach(el => {
                if (el.shadowRoot) {
                    el.innerHTML = el.shadowRoot.innerHTML;
                }
            });
        }

        expand(document.documentElement);
        return document.documentElement.outerHTML;
    }
    """)
    return html
