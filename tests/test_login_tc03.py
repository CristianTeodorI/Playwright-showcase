#TC-03 Log in with locked out user

import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory


def test_tc03_login_locked_out_user(page: Page):

    page.goto("") 
          
    ##Log-in 
    LogIn = LoginPage(page)
    InventoryPage = Inventory(page)
    LogIn.login("locked_out_user", "secret_sauce")

    expect(InventoryPage.get_inventory_list()).not_to_be_visible()

    expect(InventoryPage.get_all_items()).not_to_have_count(6)

    expect(InventoryPage.get_cart_locator()).not_to_be_visible()

    #error message is present
    expect(LogIn.get_error_locator()).to_have_count(1)

    #right error message is present
    expect(LogIn.get_error_locator()).to_contain_text("Epic sadface: Sorry, this user has been locked out.")

