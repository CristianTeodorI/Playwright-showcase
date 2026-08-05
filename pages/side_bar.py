from pages.base_page import BasePage

class SideBar(BasePage):
    def __init__(self,page):
        super().__init__(page)

    def open_sidebar(self):
        self.page.locator(".bm-burger-button").click()

    def close_sideabr(self):
        self.page.locator(".bm-cross-button").click()

    def click_all_items(self):
        self.page.locator("[data-test='inventory-sidebar-link']").click()

    def logout(self):
        self.page.locator("[data-test='logout-sidebar-link']").click()

    def reset(self):
        self.page.locator("[data-test='reset-sidebar-link']").click()