from pages.base_page import BasePage

class Inventory(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def add_to_cart(self, product_name):
        self.page.locator(f"[data-test=add-to-cart-{product_name}]").click()  #eg. data-test="add-to-cart-sauce-labs-backpack"

    def remove_product(self, product_name):
        self.page.locator(f"[data-test=remove-{product_name}]").click()  #eg. data-test="add-to-cart-sauce-labs-backpack"

    def get_add_button(self, product):
        return self.page.locator(f"[data-test='add-to-cart-{product}']")

    def get_remove_button(self, product):
        return self.page.locator(f"[data-test=remove-sauce-labs-backpack-{product}]")

    def get_price(self, product_name):
        return self.page.locator(".inventory_item") \
            .filter(has_text=product_name) \
            .locator(".inventory_item_price") \
            .inner_text()

    def expand_item(self, product_name):
        self.page.locator(".inventory_item").filter(has_text=product_name).locator(".inventory_item_name").click()

    def get_cart_locator(self):
        return self.page.locator("[data-test='shopping-cart-link']")

    def get_cart_count(self):
        badge = self.page.locator(".shopping_cart_badge")
        if badge.count() == 0:          # badge absent = empty cart
            return "0"
        return badge.inner_text()
                
    def sort_items(self, sort_type):
        self.page.locator("[data-test='product-sort-container']").select_option(sort_type)  #sort_type = az / za / lohi / hilo

    def get_inventory_list(self):
        return self.page.locator("[data-test='inventory-list']")

    def get_all_items(self):
        return self.page.locator(".inventory_item")

    def get_item_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def get_remove_button(self, product):
        return self.page.locator(f"[data-test='remove-{product}']")

    def get_cart_badge(self):
        return self.page.locator("[data-test='shopping-cart-badge']")

    def get_name(self, product_name):
        return self.page.locator(".inventory_item") \
            .filter(has_text=product_name) \
            .locator(".inventory_item_name").inner_text()

    def get_description(self, product_name):
        return self.page.locator(".inventory_item") \
            .filter(has_text=product_name) \
            .locator(".inventory_item_desc").inner_text()

    def get_name_price_map(self):
        result = {}
        for item in self.page.locator(".inventory_item").all():
            name = item.locator(".inventory_item_name").inner_text()
            price = item.locator(".inventory_item_price").inner_text()
            result[name] = price
        return result

    def get_item_prices(self):
        texts = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    