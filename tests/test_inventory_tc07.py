#TC-07 Add one product to cart
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage


def test_tc07_add_one_product(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)

    inventory.add_to_cart("sauce-labs-backpack")

    # Button in that card became "Remove"
    expect(inventory.get_remove_button("sauce-labs-backpack")).to_be_visible()

    # Cart badge reads "1"
    expect(inventory.get_cart_badge()).to_have_text("1")

    # Open the cart
    inventory.get_cart_locator().click()

    # Exactly one item, and it's the backpack
    expect(cart.get_items()).to_have_count(1)
    assert cart.get_item_names() == ["Sauce Labs Backpack"]