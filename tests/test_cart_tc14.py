#TC-14 Validate all selected products present in cart
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage


def test_tc14_all_selected_present(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)

    products = [
        ("Sauce Labs Backpack", "sauce-labs-backpack"),
        ("Sauce Labs Bike Light", "sauce-labs-bike-light"),
        ("Sauce Labs Bolt T-Shirt", "sauce-labs-bolt-t-shirt"),
    ]

    # Capture name -> price for the selected products from inventory
    inventory_map = inventory.get_name_price_map()
    selected = {name: inventory_map[name] for name, _ in products}

    # Add each
    for _, slug in products:
        inventory.add_to_cart(slug)

    # Open cart, read its name -> price map
    inventory.get_cart_locator().click()
    cart_map = cart.get_name_price_map()

    # Exact match: same names, same prices, no extras, no dupes
    assert cart_map == selected, f"Cart mismatch.\nExpected: {selected}\nActual: {cart_map}"
    expect(cart.get_items()).to_have_count(len(products))