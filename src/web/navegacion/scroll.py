async def scroll_page(page):
    previous_count = 0
    no_change_count = 0

    for i in range(30):
        cards = await page.query_selector_all(".property-card__container")
        current_count = len(cards)

        print(f"Scroll {i}: {current_count}")

        if current_count == previous_count:
            no_change_count += 1
        else:
            no_change_count = 0

        if no_change_count >= 3:
            print("No cargan más resultados")
            break

        previous_count = current_count

        # scroll más natural
        await page.mouse.wheel(0, 2000)

        try:
            await page.wait_for_function(
                f"document.querySelectorAll('.property-card__container').length > {previous_count}",
                timeout=5000
            )
        except:
            pass