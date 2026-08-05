#TC-25 Finish order successfully E2E test
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_tc25_finish_order(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Full flow: add -> cart -> checkout -> fill -> overview
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.get_cart_locator().click()
    cart.checkout()
    checkout.fill_and_continue("Max", "Mustermann", "40210")

    # Finish the order
    checkout.finish_process()

    # On the confirmation page
    expect(page).to_have_url(re.compile(r"/checkout-complete\.html$"))
    expect(checkout.get_confirmation_header()).to_contain_text("Thank you for your order")
    expect(checkout.get_back_home_button()).to_be_visible()
    expect(checkout.get_summary_container()).to_have_count(0)