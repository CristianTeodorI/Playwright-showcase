from pages.base_page import BasePage

class CartPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)

    
    def continue_shopping(self):
        self.page.locator("[data-test='continue-shopping']").click()

    def click_checkout(self):
        self.page.locator("[data-test='checkout']").click()

    def remove_product(self, product_name):
        self.page.locator(".cart_item") \
            .filter(has_text=product_name) \
            .get_by_role("button", name="Remove").click()

    def get_items(self):
        return self.page.locator(".cart_item")

    def get_item_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def get_name(self, product_name):
        return self.page.locator(".cart_item") \
            .filter(has_text=product_name) \
            .locator(".inventory_item_name").inner_text()

    def get_description(self, product_name):
        return self.page.locator(".cart_item") \
            .filter(has_text=product_name) \
            .locator(".inventory_item_desc").inner_text()

    def get_price(self, product_name):
        return self.page.locator(".cart_item") \
            .filter(has_text=product_name) \
            .locator(".inventory_item_price").inner_text()

    def get_quantity(self, product_name):
        return self.page.locator(".cart_item") \
            .filter(has_text=product_name) \
            .locator(".cart_quantity").inner_text()

    def continue_shopping(self):
        self.page.locator("[data-test='continue-shopping']").click()

    def remove_product(self, product_name):
        self.page.locator(f"[data-test='remove-{product_name}']").click()

    def get_name_price_map(self):
        result = {}
        for item in self.page.locator(".cart_item").all():
            name = item.locator(".inventory_item_name").inner_text()
            price = item.locator(".inventory_item_price").inner_text()
            result[name] = price
        return result

    def checkout(self):
        self.page.locator("[data-test='checkout']").click()