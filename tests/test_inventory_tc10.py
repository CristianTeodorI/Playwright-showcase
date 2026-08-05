#TC-10 Remove product from inventory
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage


def test_tc10_remove_from_inventory(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)

    # Precondition: two products in cart
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    expect(inventory.get_cart_badge()).to_have_text("2")

    # Remove the backpack from inventory
    inventory.remove_product("sauce-labs-backpack")

    # Its button returns to "Add to cart"
    expect(inventory.get_add_button("sauce-labs-backpack")).to_be_visible()
    expect(inventory.get_remove_button("sauce-labs-backpack")).to_have_count(0)

    # Badge decreases 2 -> 1
    expect(inventory.get_cart_badge()).to_have_text("1")

    # Cart: backpack gone, bike light remains
    inventory.get_cart_locator().click()
    expect(cart.get_items()).to_have_count(1)
    assert cart.get_item_names() == ["Sauce Labs Bike Light"]