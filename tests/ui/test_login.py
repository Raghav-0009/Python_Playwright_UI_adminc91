import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_success(page):
    # Verify page is loaded correctly with storage state
    assert "card91" in page.url.lower() or "organization" in page.url.lower()
