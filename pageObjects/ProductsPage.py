import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:
    # Products Page
    button_menu_id="react-burger-menu-btn"
    button_cart_id="shopping_cart_container"
    title_product_xpath = "//span[text()='Products']"
    select_filter_xpath="//select[@data-test='product-sort-container']"
    list_product_xpath="////div[@class='inventory_item']"
    text_productname_xpath="//div[@class='inventory_item_name ']"
    text_productprice_xpath="//div[@class='inventory_item_price']"
    text_productdescription_xpath="//div[@class='inventory_item_desc']"
    button_bagaddtocart_xpath="//button[@name='add-to-cart-sauce-labs-backpack']"

    def __init__(self, driver):
        self.driver = driver

    def verifyWebelements(self):
        flag = True
        dict = {
            self.button_menu_id: By.ID,
            self.button_cart_id:By.ID,
            self.title_product_xpath:By.XPATH,
            self.select_filter_xpath:By.XPATH,
            self.list_product_xpath: By.XPATH
        }
        for key,locator in dict.items():
            print(locator)
            print(key)
            element=self.driver.find_element(locator,key)
            if(element.is_displayed()):
                flag=True
            else:
                flag = False
            return flag

    def getProductDetailsList(self,key):
        time.sleep(5)
        list = []
        global text
        if key=="ProductName":
            text=self.driver.find_elements(By.XPATH,self.text_productname_xpath)
        elif key=="ProductPrice":
            text = self.driver.find_elements(By.XPATH, self.text_productprice_xpath)
        elif key=="ProductDescription":
            text = self.driver.find_elements(By.XPATH, self.text_productdescription_xpath)
        for ele in text:
            list.append(ele.text)
        return list

    def selectSortingMethod(self,value):
        ele = self.driver.find_element(By.XPATH,self.select_filter_xpath)
        select = Select(ele)
        select.select_by_visible_text(value)

    def clickAddToCart(self):
        self.driver.find_element(By.XPATH,self.button_bagaddtocart_xpath).click()

    def clickOnCart(self):
        self.driver.find_element(By.ID, self.button_cart_id).click()



