from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username  = page.locator("[data-test='username']")
        self.password  = page.locator("[data-test='password']")
        self.login_btn = page.locator("[data-test='login-button']")

    def login(self, user, pw):
        self.navigate("")
        self.username.fill(user)
        self.password.fill(pw)
        self.login_btn.click()

    def get_error_locator(self):
        return self.page.locator("[data-test='error']")

    # def get_error_message(self):
    #     return self.page.locator("[data-test='error']").inner_text()

