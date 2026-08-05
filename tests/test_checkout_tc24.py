#TC-24 Cancel from checkout overview
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_tc24_cancel_from_overview(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # One product, proceed to the overview
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.get_cart_locator().click()
    cart.checkout()
    checkout.fill_and_continue("Cristian", "Ilie", "40210")

    # Confirm we're on the overview before cancelling
    expect(page).to_have_url(re.compile(r"/checkout-step-two\.html$"))

    # Cancel
    checkout.cancel()

    # Returns to inventory, no order completed
    expect(page).to_have_url(re.compile(r"/inventory\.html$"))
    expect(checkout.get_confirmation_header()).to_have_count(0)

    # Cart still holds the item (SauceDemo keeps the cart on cancel)
    expect(inventory.get_cart_badge()).to_have_text("1")