#TC-18 Accept valid checkout information
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_tc18_accept_valid_checkout_info(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Reach checkout-step-one with a product
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.get_cart_locator().click()
    cart.checkout()

    # Fill valid info and continue
    checkout.fill_and_continue("Cristian", "Ilie", "40210")

    # No error, advanced to overview, product still present
    expect(checkout.get_error()).to_have_count(0)
    expect(page).to_have_url(re.compile(r"/checkout-step-two\.html$"))
    assert "Sauce Labs Backpack" in checkout.get_list_items()