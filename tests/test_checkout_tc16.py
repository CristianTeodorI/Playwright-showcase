#TC-16 Validate all checkout fields empty
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_tc16_checkout_fields_empty(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Reach checkout-step-one with an item in the cart
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.get_cart_locator().click()
    cart.checkout()

    # Leave all fields blank, click Continue
    checkout.get_continue_button().click()

    # Stays on step-one, error shown, overview not reached
    expect(page).to_have_url(re.compile(r"/checkout-step-one\.html$"))
    expect(checkout.get_error()).to_be_visible()
    expect(checkout.get_error()).to_contain_text("First Name is required")
    expect(checkout.get_summary_container()).to_have_count(0)