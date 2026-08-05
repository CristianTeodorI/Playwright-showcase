#TC-01 Log in with valid standard user

import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory

def test_tc01_login_valid_standard_user(page: Page):

    page.goto("") 

    ##Log-in 
    LogIn = LoginPage(page)
    InventoryPage = Inventory(page)
    LogIn.login("standard_user", "secret_sauce")

    expect(InventoryPage.get_inventory_list()).to_be_visible()

    expect(InventoryPage.get_all_items()).to_have_count(6)
   
    expect(InventoryPage.get_cart_locator()).to_be_visible()

    expect(LogIn.get_error_locator()).to_have_count(0)

