#TC-08 Prevent duplicate addition
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage


def test_tc08_prevent_duplicate_addition(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    slug = "sauce-labs-backpack"

    # Add the product
    inventory.add_to_cart(slug)

    # After adding, the Remove button exists and the Add button is gone
    expect(inventory.get_remove_button(slug)).to_have_count(1)
    expect(inventory.get_add_button(slug)).to_have_count(0)

    # Navigate to cart and back to inventory
    inventory.get_cart_locator().click()
    page.go_back()

    # Badge still reads "1" (never became "2")
    expect(inventory.get_cart_badge()).to_have_text("1")

    # Cart has exactly one item for that product
    inventory.get_cart_locator().click()
    expect(cart.get_items()).to_have_count(1)
    assert cart.get_item_names() == ["Sauce Labs Backpack"]