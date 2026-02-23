import pytest
import os
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

STORAGE_STATE = "storage_state.json"


# -----------------------------
# Browser Fixture
# -----------------------------
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


# -----------------------------
# Create Storage State (Login Once)
# -----------------------------
@pytest.fixture(scope="session")
def create_storage_state(browser):
    if os.path.exists(STORAGE_STATE):
        return

    context = browser.new_context()
    page = context.new_page()

    login = LoginPage(page)
    login.open()
    login.login()
    login.wait(3000)  # Wait for login to complete
    
    # Verify login was successful
    assert "card91" in login.get_url().lower() or login.is_dashboard_visible()

    # Save authenticated state
    context.storage_state(path=STORAGE_STATE)

    context.close()


# -----------------------------
# Page Fixture (Reuse Login)
# -----------------------------
@pytest.fixture(scope="function")
def page(browser, create_storage_state, request):
    context = browser.new_context(storage_state=STORAGE_STATE)
    page = context.new_page()
    
    # Navigate to dashboard to ensure authenticated session is active
    page.goto("https://ppi-admin-portal.qual.card91.in/app/organization/list/all")
    page.wait_for_load_state("networkidle")
    
    # Check for login modal (session expired but URL didn't change)
    login_modal = page.locator("#login-back")
    if login_modal.is_visible():
        # Modal appeared - refresh and do fresh login
        page.goto("https://ppi-admin-portal.qual.card91.in/")
        page.wait_for_load_state("networkidle")
        login = LoginPage(page)
        login.login()
        login.wait(3000)
        # Navigate to org list after login
        page.goto("https://ppi-admin-portal.qual.card91.in/app/organization/list/all")
        page.wait_for_load_state("networkidle")
    
    # Verify we're still logged in (not redirected to login page)
    if "login" in page.url.lower() or page.url == "https://ppi-admin-portal.qual.card91.in/":
        # Session expired - perform fresh login
        login = LoginPage(page)
        login.login()
        login.wait(3000)
        # Re-verify after login
        if not ("card91" in page.url.lower() or login.is_dashboard_visible()):
            raise Exception("Re-login failed - could not authenticate")
    
    yield page

    # Screenshot if failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path=f"screenshots/{request.node.name}.png")

    context.close()


# -----------------------------
# Hook for failure detection
# -----------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
