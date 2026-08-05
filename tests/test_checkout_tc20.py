#TC-20 Cancel from customer information page
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_tc20_cancel_from_info_page(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Product in cart, reach checkout-step-one
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.get_cart_locator().click()
    cart.checkout()

    # Enter partial data, then Cancel
    checkout.fill_info("Cris", "", "")
    checkout.cancel()

    # Back on cart, contents unchanged, no confirmation
    expect(page).to_have_url(re.compile(r"/cart\.html$"))
    expect(cart.get_items()).to_have_count(1)
    assert cart.get_item_names() == ["Sauce Labs Backpack"]
    expect(checkout.get_confirmation_header()).to_have_count(0)