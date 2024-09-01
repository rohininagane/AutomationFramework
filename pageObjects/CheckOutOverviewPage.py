from selenium.webdriver.common.by import By
class CheckOutOverviewPage():
    # Checkout Overview Page
    pagetitle_checkoutover_xpath = "//span[text()='Checkout: Overview']"
    text_quantity_xpath = "//div[text()='QTY']"
    text_description_xpath = "//div[text()='Description']"
    frame_cartitem_xpath = "//div[@class='cart_item']"
    text_productname_xpath = "//div[@class='inventory_item_name']"
    text_productdesc_xpath = "//div[@class='inventory_item_desc']"
    text_productprice_xpath = "//div[@data-test='inventory-item-price']"
    button_finish_id="finish"
    img_greentick_xpath="//img[@alt='Pony Express']"
    header_complete_xpath="//h2[@class='complete-header']"
    headertext_complete_xpath="//div[@ class ='complete-text']"
    button_back_id="back-to-products"
    field_payment_xpath="//div[@data-test='payment-info-label']"
    field_shipping_xpath= "//div[@data-test='shipping-info-label']"
    field_pricetotal_xpath="//div[@data-test='total-info-label']"
    button_cancel_id="cancel"

    def __init__(self, driver):
        self.driver = driver

    def verifyWebelements(self):
        flag = True
        dict = {
            self.pagetitle_checkoutover_xpath: By.XPATH,
            self.frame_cartitem_xpath: By.XPATH,
            self.button_finish_id:By.ID,
            self.frame_cartitem_xpath:By.XPATH,
            self.field_payment_xpath: By.XPATH,
            self.field_shipping_xpath: By.XPATH,
            self.field_pricetotal_xpath: By.XPATH,
            self.button_cancel_id: By.ID
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

    def getSuccessMessage(self):
        ele = self.driver.find_element(By.XPATH, self.header_complete_xpath)
        text=ele.text
        return text

    def getDetailedSuccessMessage(self):
        ele = self.driver.find_element(By.XPATH, self.headertext_complete_xpath)
        text = ele.text
        return text

    def clickFinish(self):
        self.driver.find_element(By.ID,self.button_finish_id).click()





