#TC-21 Verify checkout overview content
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_tc21_overview_content(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Two products in cart
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")

    # Capture the cart's name->price map
    inventory.get_cart_locator().click()
    cart_map = cart.get_name_price_map()

    # Proceed through checkout to the overview
    cart.checkout()
    checkout.fill_and_continue("Cristian", "Ilie", "40210")

    # Overview items match the cart exactly (names + prices)
    assert checkout.get_name_price_map() == cart_map, "Overview does not match cart"

    # Payment and shipping info present and non-empty
    assert checkout.get_payment_info().inner_text().strip(), "Payment info empty"
    assert checkout.get_shipping_info().inner_text().strip(), "Shipping info empty"

    # Subtotal, tax, total labels visible
    expect(checkout.get_subtotal_label()).to_be_visible()
    expect(checkout.get_tax_label()).to_be_visible()
    expect(checkout.get_total_label()).to_be_visible()