from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
    
    def fill_info(self, first, last, postal):
        self.get_first_name_field().fill(first)
        self.get_last_name_field().fill(last)
        self.get_postal_code_field().fill(postal)

    def fill_and_continue(self,first="", last="", postal=""):
        # self.page.locator("[data-test='firstName']").fill(first_name)
        # self.page.locator("[data-test='lastName']").fill(last_name)
        # self.page.locator("[data-test='postalCode']").fill(zip_code)

        self.fill_info(first, last, postal)
        self.page.locator("[data-test='continue']").click()

    def cancel(self):
        self.get_cancel_button().click()

    def get_confirmation_header(self):
        return self.page.locator("[data-test='complete-header']")

    def get_errorMessage(self):
        return self.page.locator("[data-test='error']").inner_text()

    def finish_process(self):
        self.page.locator("[data-test='finish']").click()

    def get_list_items(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()  #returns a list of plain strings

    def get_subtotal(self):
        text = self.page.locator("[data-test='subtotal-label']").inner_text()
        # "Item total: $29.99" → 29.99
        return float(text.split("$")[1])

    def get_confirmation(self):
        return self.page.locator("[data-test='complete-text']").inner_text()

    def get_last_name_field(self):
        return self.page.locator("[data-test='lastName']")

    def get_postal_code_field(self):
        return self.page.locator("[data-test='postalCode']")

    def get_continue_button(self):
        return self.page.locator("[data-test='continue']")

    def get_first_name_field(self):
        return self.page.locator("[data-test='firstName']")

    def get_cancel_button(self):
        return self.page.locator("[data-test='cancel']")

    def get_error(self):
        return self.page.locator("[data-test='error']")

    def get_summary_container(self):
        return self.page.locator("[data-test='checkout-summary-container']")

    def get_name_price_map(self):
        result = {}
        for item in self.page.locator(".cart_item").all():
            name = item.locator(".inventory_item_name").inner_text()
            price = item.locator(".inventory_item_price").inner_text()
            result[name] = price
        return result

    def get_payment_info(self):
        return self.page.locator("[data-test='payment-info-value']")

    def get_shipping_info(self):
        return self.page.locator("[data-test='shipping-info-value']")

    def get_subtotal_label(self):
        return self.page.locator("[data-test='subtotal-label']")

    def get_tax_label(self):
        return self.page.locator("[data-test='tax-label']")

    def get_total_label(self):
        return self.page.locator("[data-test='total-label']")

    def cancel(self):
        self.get_cancel_button().click()

    def get_back_home_button(self):
        return self.page.locator("[data-test='back-to-products']")

   