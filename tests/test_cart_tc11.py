#TC-11 Validate inventory-to-cart data consistency
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage


def test_tc11_inventory_to_cart_consistency(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    product = "Sauce Labs Backpack"

    # Capture on inventory
    inv_name = inventory.get_name(product)
    inv_desc = inventory.get_description(product)
    inv_price = inventory.get_price(product)

    # Add and open cart
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.get_cart_locator().click()

    # Compare against cart
    assert cart.get_name(product) == inv_name, "Name changed between inventory and cart"
    assert cart.get_description(product) == inv_desc, "Description changed"
    assert cart.get_price(product) == inv_price, "Price changed"
    assert cart.get_quantity(product) == "1", "Quantity is not 1"