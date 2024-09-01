from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    link_logout_linktext = "Logout"
    error_message_xpath = "//h3[@data-test='error']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.ID,self.textbox_username_id).click()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID,self.button_login_id).click()

    def getErrorMessage(self):
        text=self.driver.find_element(By.XPATH,self.error_message_xpath).text
        return text