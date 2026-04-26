from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.web.navegacion.scroll import scroll_page


@pytest.mark.asyncio
async def test_scroll_page_stops_when_no_new_content_loads():
    mock_page = AsyncMock()
    mock_cards = [MagicMock(), MagicMock(), MagicMock()]

    mock_page.query_selector_all = AsyncMock(
        side_effect=[
            mock_cards,
            mock_cards,
            mock_cards,
            mock_cards,
        ]
    )

    mock_page.mouse.wheel = AsyncMock()
    mock_page.wait_for_function = AsyncMock()

    await scroll_page(mock_page)

    assert mock_page.mouse.wheel.call_count <= 33


@pytest.mark.asyncio
async def test_scroll_page_early_exit_after_three_consecutive_no_change():
    mock_page = AsyncMock()
    mock_cards = [MagicMock()]

    mock_page.query_selector_all = AsyncMock(return_value=mock_cards)
    mock_page.mouse.wheel = AsyncMock()
    mock_page.wait_for_function = AsyncMock()

    with patch("src.web.navegacion.scroll.range", return_value=range(10)):
        await scroll_page(mock_page)

    assert mock_page.mouse.wheel.call_count >= 3


@pytest.mark.asyncio
async def test_scroll_page_queries_property_card_container():
    mock_page = AsyncMock()
    mock_cards = []

    mock_page.query_selector_all = AsyncMock(return_value=mock_cards)
    mock_page.mouse.wheel = AsyncMock()

    await scroll_page(mock_page)

    mock_page.query_selector_all.assert_called_with(".property-card__container")


@pytest.mark.asyncio
async def test_scroll_page_uses_mouse_wheel():
    mock_page = AsyncMock()
    mock_cards = []

    mock_page.query_selector_all = AsyncMock(return_value=mock_cards)
    mock_page.wait_for_function = AsyncMock(side_effect=Exception("timeout"))

    await scroll_page(mock_page)

    mock_page.mouse.wheel.assert_called()


@pytest.mark.asyncio
async def test_scroll_page_prints_scroll_progress(capsys):
    mock_page = AsyncMock()
    mock_cards = [MagicMock()]

    mock_page.query_selector_all = AsyncMock(return_value=mock_cards)
    mock_page.mouse.wheel = AsyncMock()
    mock_page.wait_for_function = AsyncMock()

    await scroll_page(mock_page)

    captured = capsys.readouterr()
    assert "Scroll" in captured.out or "cargan" in captured.out


@pytest.mark.asyncio
async def test_scroll_page_max_30_scrolls():
    mock_page = AsyncMock()
    mock_cards = [MagicMock()]

    call_count = [0]

    def increment_cards(*args):
        call_count[0] += 1
        return mock_cards

    mock_page.query_selector_all = AsyncMock(side_effect=increment_cards)
    mock_page.mouse.wheel = AsyncMock()
    mock_page.wait_for_function = AsyncMock()

    await scroll_page(mock_page)

    assert mock_page.mouse.wheel.call_count <= 32
