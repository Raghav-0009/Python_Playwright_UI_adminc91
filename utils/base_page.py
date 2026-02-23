import logging
from pathlib import Path


# -------- Logging Configuration -------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        try:
            logger.info(f"Navigating to URL: {url}")
            self.page.goto(url)
        except Exception as e:
            logger.error(f"Failed to navigate to {url} | Error: {e}")
            self._take_screenshot("navigate_error")
            raise

    def wait_for_element_visible(self, locator, timeout=10000):
        try:
            logger.info(f"Waiting for element to be visible: {locator}")
            locator.wait_for(state="visible", timeout=timeout)
        except Exception as e:
            logger.error(f"Element not visible: {locator} | Error: {e}")
            self._take_screenshot("element_not_visible")
            raise

    def click(self, locator):
        try:
            logger.info(f"Clicking on element: {locator}")
            self.wait_for_element_visible(locator)
            locator.click()
        except Exception as e:
            logger.error(f"Failed to click element: {locator} | Error: {e}")
            self._take_screenshot("click_error")
            raise

    def fill(self, locator, value):
        try:
            logger.info(f"Filling element: {locator} with value: {value}")
            self.wait_for_element_visible(locator)
            locator.fill(value)
        except Exception as e:
            logger.error(f"Failed to fill element: {locator} | Error: {e}")
            self._take_screenshot("fill_error")
            raise

    def wait(self, milliseconds=2000):
        logger.info(f"Waiting for {milliseconds} milliseconds")
        self.page.wait_for_timeout(milliseconds)

    def get_url(self):
        current_url = self.page.url
        logger.info(f"Current URL: {current_url}")
        return current_url

    # -------- Private Screenshot Method -------- #
    def _take_screenshot(self, name):
        try:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_path = screenshots_dir / f"{name}.png"
            self.page.screenshot(path=str(file_path))
            logger.info(f"Screenshot saved: {file_path}")
        except Exception as e:
            logger.error(f"Failed to take screenshot | Error: {e}")
