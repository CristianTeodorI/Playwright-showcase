#TC-06 Sort products by price (low-high and high-low)
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import Inventory


def test_tc06_sort_by_price(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)

    inventory.sort_items("lohi")
    prices_lohi = inventory.get_item_prices()
    assert prices_lohi == sorted(prices_lohi), f"Low-high sort wrong: {prices_lohi}"

    inventory.sort_items("hilo")
    prices_hilo = inventory.get_item_prices()
    assert prices_hilo == sorted(prices_hilo, reverse=True), f"High-low sort wrong: {prices_hilo}"

    assert len(prices_lohi) == 6
    #----Check if the same prudocts are present on the page
    assert sorted(prices_lohi) == sorted(prices_hilo), "Sort changed the set of prices"