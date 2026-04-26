import pytest
from unittest.mock import AsyncMock
from src.web.navegacion.render import get_rendered_html


@pytest.mark.asyncio
async def test_get_rendered_html_returns_expanded_html():
    mock_page = AsyncMock()

    expected_html = "<html><body><div class='expanded'>Content</div></body></html>"
    mock_page.evaluate = AsyncMock(return_value=expected_html)

    result = await get_rendered_html(mock_page)

    assert result == expected_html
    mock_page.evaluate.assert_called_once()

    call_args = mock_page.evaluate.call_args[0][0]
    assert "expand" in call_args
    assert "shadowRoot" in call_args


@pytest.mark.asyncio
async def test_get_rendered_html_expands_shadow_dom():
    mock_page = AsyncMock()

    html_with_shadow = "<html><body><custom-element shadowroot><template>Shadow Content</template></custom-element></body></html>"
    expected_expanded = "<html><body><custom-element>Shadow Content</custom-element></body></html>"
    mock_page.evaluate = AsyncMock(return_value=expected_expanded)

    result = await get_rendered_html(mock_page)

    assert "Shadow Content" in result


@pytest.mark.asyncio
async def test_get_rendered_html_calls_document_outerhtml():
    mock_page = AsyncMock()

    mock_page.evaluate = AsyncMock(return_value="<html>Document</html>")

    result = await get_rendered_html(mock_page)

    call_args = mock_page.evaluate.call_args[0][0]
    assert "document.documentElement.outerHTML" in call_args