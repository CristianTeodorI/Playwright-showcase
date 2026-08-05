#TC-15 Start checkout with populated cart
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_tc15_start_checkout(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Precondition: one product in cart
    inventory.add_to_cart("sauce-labs-backpack")
    expect(inventory.get_cart_badge()).to_have_text("1")

    # Open cart, start checkout
    inventory.get_cart_locator().click()
    cart.checkout()

    # On checkout-step-one
    expect(page).to_have_url(re.compile(r"/checkout-step-one\.html$"))

    # All three fields visible
    expect(checkout.get_first_name_field()).to_be_visible()
    expect(checkout.get_last_name_field()).to_be_visible()
    expect(checkout.get_postal_code_field()).to_be_visible()

    # Continue and Cancel visible
    expect(checkout.get_continue_button()).to_be_visible()
    expect(checkout.get_cancel_button()).to_be_visible()

    # Cart badge still reflects the item count
    expect(inventory.get_cart_badge()).to_have_text("1")