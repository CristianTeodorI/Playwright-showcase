#TC-13 Remove product from cart page
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage


def test_tc13_remove_from_cart_page(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)

    # Precondition: two products in cart
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    expect(inventory.get_cart_badge()).to_have_text("2")

    # Open cart, capture the item we'll keep, then remove the other
    inventory.get_cart_locator().click()
    kept_price = cart.get_price("Sauce Labs Bike Light")

    cart.remove_product("sauce-labs-backpack")

    # Removed item gone, one item left, badge dropped
    expect(cart.get_items()).to_have_count(1)
    assert cart.get_item_names() == ["Sauce Labs Bike Light"]
    expect(inventory.get_cart_badge()).to_have_text("1")

    # Remaining item unchanged (price intact)
    assert cart.get_price("Sauce Labs Bike Light") == kept_price

    # Back on inventory, removed item shows "Add to cart"
    cart.continue_shopping()
    expect(inventory.get_add_button("sauce-labs-backpack")).to_be_visible()