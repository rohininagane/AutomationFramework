import pytest
import os
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    @pytest.mark.ui
    def test_homePageTitle(self, setup):
        """
        Test to verify the title of the home page.
        """
        self.driver = setup
        logger = LogGen.loggen("HomePageTitle")
        logger.info("*************** Test_001_LoginPage *****************")
        try:
            logger.info("**** Started Home page title test ****")
            self.driver.get(self.baseURL)
            WebDriverWait(self.driver, 20).until(EC.title_is("Swag Labs"))
            act_title = self.driver.title
            assert act_title == "Swag Labs", f"Expected title 'Swag Labs', but got '{act_title}'"
            logger.info("**** Login page title is:", f"'{act_title}' It is as expected. ****")
            logger.info("**** Login page title test passed ****")
        except Exception as e:
            screenshot_path = os.path.join(".\\Screenshots\\", "test_homePageTitle.png")
            self.driver.save_screenshot(screenshot_path)
            logger.error("Error occurred: %s", e)
            logger.error("Traceback: %s", traceback.format_exc())
            raise
        finally:
            self.driver.quit()
            logger.info("************* Finishing Test case. **********")

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.ui
    def test_valid_login(self, login):
        """
        Test to verify valid login credentials.
        """
        self.driver = login
        logger = LogGen.loggen("ValidLogin")
        logger.info("*************** Test_002_Valid_Login *****************")
        try:
            act_title = self.driver.title
            assert act_title == "Swag Labs", f"Expected title 'Swag Labs', but got '{act_title}'"
            logger.info("**** Login test with valid credentials passed. ****")
        except Exception as e:
            screenshot_path = os.path.join(".\\Screenshots\\", "test_valid_login.png")
            self.driver.save_screenshot(screenshot_path)
            logger.error("Error occurred: %s", e)
            logger.error("Traceback: %s", traceback.format_exc())
            raise
        finally:
            logger.info("************* Finishing Test case. **********")

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize("username, password", [("1234", "randompassword")])
    def test_invalid_login(self, setup, username, password):
        """
        Test to verify invalid login credentials.
        """
        logger = LogGen.loggen("InvalidLogin")
        logger.info("*************** Test_003_Invalid_Login *****************")
        driver = setup
        try:
            driver.get(self.baseURL)
            driver.maximize_window()
            lp = LoginPage(driver)
            lp.setUserName(username)
            logger.info("*************** Entered username: %s *****************", username)
            lp.setPassword(password)
            logger.info("*************** Entered password: %s *****************", password)
            lp.clickLogin()
            logger.info("*************** Clicked on Login *****************")

            # Explicitly wait for error message to be visible
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
            )
            text = lp.getErrorMessage()
            expected_message = "Epic sadface: Username and password do not match any user in this service"
            assert text == expected_message, f"Expected error message '{expected_message}', but got '{text}'"
            logger.info("*************** Login test for invalid credentials passed. User not able to login. ***************")
            logger.info("*************** Error message displayed: %s ***************", text)
        except Exception as e:
            screenshot_path = os.path.join(".\\Screenshots\\", "test_invalid_login.png")
            driver.save_screenshot(screenshot_path)
            logger.error("Error occurred: %s", e)
            logger.error("Traceback: %s", traceback.format_exc())
            raise
        finally:
            logger.info("************* Finishing Test case. **********")
