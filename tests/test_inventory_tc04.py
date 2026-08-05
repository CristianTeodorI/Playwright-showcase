#TC-04 Verify inventory product presentation
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory


def test_tc04_inventory_presentation(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)

    # Card count == 6
    expect(inventory.get_all_items()).to_have_count(6)

    # Every card has exactly one name / desc / price (6 cards -> 6 of each)
    expect(page.locator(".inventory_item_name")).to_have_count(6)
    expect(page.locator(".inventory_item_desc")).to_have_count(6)
    expect(page.locator(".inventory_item_price")).to_have_count(6)

    # Names and descriptions are non-empty
    for name in page.locator(".inventory_item_name").all_inner_texts():
        assert name.strip(), "Empty product name"
    for desc in page.locator(".inventory_item_desc").all_inner_texts():
        assert desc.strip(), "Empty product description"

    # Prices match $X.XX format
    price_pattern = re.compile(r"^\$\d+\.\d{2}$")
    for price in page.locator(".inventory_item_price").all_inner_texts():
        assert price_pattern.match(price), f"Bad price format: {price}"

    # Every card has exactly one add/remove button (6 cards -> 6 buttons)
    expect(page.locator(".inventory_item button")).to_have_count(6)

    # Every image has a non-empty src
    for img in page.locator(".inventory_item img").all():
        src = img.get_attribute("src")
        assert src, "Image missing src"

    # No duplicate product names
    names = page.locator(".inventory_item_name").all_inner_texts()
    assert len(names) == len(set(names)), f"Duplicate names: {names}"