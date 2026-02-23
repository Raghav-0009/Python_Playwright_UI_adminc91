from utils.base_page import BasePage
from config.config import get_config

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.config = get_config()

        self.username_input = self.page.locator("#userEmail")
        self.password_input = self.page.locator("#passwordBoxForLogin")
        self.login_button = self.page.locator("#loginBtn")

    def open(self):
        self.navigate(self.config["base_url"])

    def login(self):
        self.fill(self.username_input, self.config["username"])
        self.fill(self.password_input, self.config["password"])
        self.click(self.login_button)

    def is_dashboard_visible(self):
        return self.page.get_by_role("link", name="All Businesses").is_visible()
