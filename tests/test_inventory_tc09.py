#TC-09 Add multiple distinct products
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage


def test_tc09_add_multiple_distinct(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)

    # Add three products, checking the badge after each
    inventory.add_to_cart("sauce-labs-backpack")
    expect(inventory.get_cart_badge()).to_have_text("1")

    inventory.add_to_cart("sauce-labs-bike-light")
    expect(inventory.get_cart_badge()).to_have_text("2")

    inventory.add_to_cart("sauce-labs-bolt-t-shirt")
    expect(inventory.get_cart_badge()).to_have_text("3")

    # Open the cart
    inventory.get_cart_locator().click()

    # Exactly 3 items, and they're exactly the three we added
    expect(cart.get_items()).to_have_count(3)
    assert set(cart.get_item_names()) == {
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
    }