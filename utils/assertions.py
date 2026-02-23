def assert_url_contains(page, text):
    assert text.lower() in page.url.lower(), \
        f"Expected '{text}' in URL but got {page.url}"

def assert_element_visible(page, locator):
    assert page.is_visible(locator), \
        f"Element {locator} is not visible"
