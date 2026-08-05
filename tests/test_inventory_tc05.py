#TC-05 Sort products alphabetically (A-Z and Z-A)
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import Inventory


def test_tc05_sort_alphabetically(page: Page):
    page.goto("")
    LoginPage(page).login("standard_user", "secret_sauce")
    inventory = Inventory(page)

    inventory.sort_items("az")
    names_az = inventory.get_item_names()
    assert names_az == sorted(names_az, key=str.lower), f"A-Z sort wrong: {names_az}"

    inventory.sort_items("za")
    names_za = inventory.get_item_names()
    assert names_za == sorted(names_za, key=str.lower, reverse=True), f"Z-A sort wrong: {names_za}"

    assert len(names_az) == 6
    #----Check if the same products are present on the page
    assert set(names_az) == set(names_za), "Sort changed the set of products"