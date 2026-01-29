from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class InventoryPage:

    PRODUCT_SORT= (By.XPATH,'//select[@data-test="product-sort-container"]')
    SHOPPING_CART_ICON=(By.XPATH,'//a[@data-test="shopping-cart-link"]')
    ADD_TO_CART_BUTTON =(By.ID,"add-to-cart-sauce-labs-backpack")


    def __init__(self,driver):
        self.driver=driver

    def select_sort_by_name_az(self):
        dropdown = Select(self.driver.find_element(*self.PRODUCT_SORT))
        dropdown.select_by_value("az")

    def select_sort_by_name_za(self):
        dropdown = Select(self.driver.find_element(*self.PRODUCT_SORT))
        dropdown.select_by_value("za")


    def select_sort_by_price_lh(self):
        dropdown = Select(self.driver.find_element(*self.PRODUCT_SORT))
        dropdown.select_by_value("lohi")


    def select_sort_by_price_hl(self):
        dropdown = Select(self.driver.find_element(*self.PRODUCT_SORT))
        dropdown.select_by_value("hilo")

    def is_inventory_page_loaded(self):
        return "inventory.html" in self.driver.current_url