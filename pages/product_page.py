from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def add_item(self):
        self.page.locator("[data-test='add-to-cart']").click()

    def remove_item(self):
        self.page.locator("[data-test='remove']").click()

    def get_price(self):
        return self.page.locator("[data-test='inventory-item-price']")

    def get_name(self):
        return self.page.locator("[data-test='inventory-item-name']")

    def back_to_products(self):
        self.page.locator("[data-test='back-to-products']").click()
        