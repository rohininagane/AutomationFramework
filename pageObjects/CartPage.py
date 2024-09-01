from selenium.webdriver.common.by import By


class CartPage():
    # Add customer Page
    title_cartpage_xpath = "//span[text()='Your Cart']"
    text_quantity_xpath="//div[text()='QTY']"
    text_description_xpath = "//div[text()='Description']"
    frame_cartitem_xpath="//div[@class='cart_item']"
    text_productname_xpath="//div[@class='inventory_item_name']"
    text_productdesc_xpath="//div[@class='inventory_item_desc']"
    text_productprice_xpath="//div[@data-test='inventory-item-price']"
    button_remove_xpath = "//button[@class='btn btn_secondary btn_small cart_button']"
    button_checkout_id="checkout"

    def __init__(self, driver):
        self.driver = driver

    def verifyWebelements(self):
        flag = True
        dict = {
            self.title_cartpage_xpath: By.XPATH,
            self.text_quantity_xpath: By.XPATH,
            self.text_description_xpath:By.XPATH,
            self.frame_cartitem_xpath:By.XPATH,
            self.text_productname_xpath: By.XPATH
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

    def clickOnCheckout(self):
        self.driver.find_element(By.ID,self.button_checkout_id).click()

    def getProductName(self):
        text = self.driver.find_element(By.XPATH,self.text_productname_xpath).text
        return text


