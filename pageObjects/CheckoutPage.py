from selenium.webdriver.common.by import By


class CheckoutPage():
    # Add customer Page
    pagetitle_checkout_xpath = "//span[text()='Checkout: Your Information']"
    textbox_firstname_id="first-name"
    textbox_lastname_id = "last-name"
    textbox_postal_id="postal-code"
    button_continue_id="continue"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def setPostalCode(self, postalcode):
        self.driver.find_element(By.ID, self.textbox_postal_id).send_keys(postalcode)

    def clickContinue(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()



