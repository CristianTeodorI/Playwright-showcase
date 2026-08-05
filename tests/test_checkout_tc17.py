#TC-17 Validate mandatory-field combinations (decision table)
import re
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

V = "x"   # any valid non-empty value

@pytest.mark.parametrize("first,last,postal,expected", [
    ("",  "",  "",  "First Name is required"),
    (V,   "",  "",  "Last Name is required"),
    (V,   V,   "",  "Postal Code is required"),
    ("",  V,   V,   "First Name is required"),
    (V,   "",  V,   "Last Name is required"),
    ("",  "",  V,   "First Name is required"),
    ("",  V,   "",  "First Name is required"),
    (V,   V,   V,   None),   # None => advances to overview
])
def test_tc17_mandatory_field_combinations(page: Page, first, last, postal, expected):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Reach checkout-step-one
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.get_cart_locator().click()
    cart.checkout()

    # Fill per the row, then Continue
    checkout.fill_info(first, last, postal)
    checkout.get_continue_button().click()

    if expected is None:
        # All-valid row: should advance to step-two
        expect(page).to_have_url(re.compile(r"/checkout-step-two\.html$"))
    else:
        # Invalid rows: stay on step-one, correct error shown
        expect(page).to_have_url(re.compile(r"/checkout-step-one\.html$"))
        expect(checkout.get_error()).to_contain_text(expected)