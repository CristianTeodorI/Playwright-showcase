#TC-12 Continue Shopping preserves cart
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage


def test_tc12_continue_shopping_preserves_cart(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)

    # Precondition: two products in cart
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    expect(inventory.get_cart_badge()).to_have_text("2")

    # Open cart, then Continue Shopping
    inventory.get_cart_locator().click()
    cart.continue_shopping()

    # Back on inventory
    expect(page).to_have_url(re.compile(r"/inventory\.html$"))

    # Badge still 2, both products still show Remove
    expect(inventory.get_cart_badge()).to_have_text("2")
    expect(inventory.get_remove_button("sauce-labs-backpack")).to_be_visible()
    expect(inventory.get_remove_button("sauce-labs-bike-light")).to_be_visible()

    # Reopen cart, same two items
    inventory.get_cart_locator().click()
    expect(cart.get_items()).to_have_count(2)
    assert set(cart.get_item_names()) == {
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    }