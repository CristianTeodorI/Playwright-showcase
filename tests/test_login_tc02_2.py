#TC-02 Log in with invalid user/right pass

import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory


def test_tc02_login_invalid_standard_user(page: Page):

    page.goto("") 
   
    ##Log-in 
    LogIn = LoginPage(page)
    InventoryPage = Inventory(page)
    LogIn.login("_not_standard_user", "secret_sauce")

    expect(InventoryPage.get_inventory_list()).not_to_be_visible()

    expect(InventoryPage.get_all_items()).not_to_have_count(6)

    expect(InventoryPage.get_cart_locator()).not_to_be_visible()

    #error message is present
    expect(LogIn.get_error_locator()).to_have_count(1)
