import pytest
import os
import traceback
import string
import random
from pageObjects.ProductsPage import ProductsPage
from utilities.customLogger import LogGen

class Test_ProductPage:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.ui
    def test_UIElementsOnPage(self, login):
        """
        Test to verify all UI elements on the Products page.
        """
        logger = LogGen.loggen("UIEleProductPage")
        logger.info("************* Test Scenario: Verify all UI Elements on Products page. **********")
        self.driver = login
        try:
            self.products = ProductsPage(self.driver)
            flag = self.products.verifyWebelements()
            assert flag, "UI element verification on the product page failed."
            logger.info("********* Verify all UI Elements on product page passed. *********")
        except Exception as e:
            screenshot_path = os.path.join(".\\Screenshots\\", "test_UIElementsOnPage.png")
            self.driver.save_screenshot(screenshot_path)
            logger.error("Error occurred: %s", e)
            logger.error("Traceback: %s", traceback.format_exc())
            raise
        finally:
            logger.info("************* Finishing Test case. **********")

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize("data", [
        {"Name (A to Z)": ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"],
         "Name (Z to A)": ["Test.allTheThings() T-Shirt (Red)", "Sauce Labs Onesie", "Sauce Labs Fleece Jacket", "Sauce Labs Bolt T-Shirt", "Sauce Labs Bike Light", "Sauce Labs Backpack"],
         "Price (low to high)": ['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99'],
         "Price (high to low)": ["$49.99", "$29.99", "$15.99", "$15.99", "$9.99", "$7.99"]}])
    def test_Sorting(self, login, data):
        """
        Test to verify sorting options on the product page.
        """
        logger = LogGen.loggen("ProductSorting")
        logger.info("************* Test Scenario: Verify sorting options on the product page. **********")
        self.driver = login
        try:
            self.products = ProductsPage(self.driver)

            # Sorting by Name (A to Z)
            logger.info("********** Verifying sorting by option Name (A to Z). **********")
            self.products.selectSortingMethod("Name (A to Z)")
            productname = self.products.getProductDetailsList("ProductName")
            logger.info("Expected Product name list after sorting: %s", data["Name (A to Z)"])
            logger.info("Actual Product name list after sorting: %s", productname)
            assert productname == data["Name (A to Z)"], "Sorting by Name (A to Z) failed."
            logger.info("********** Sorting by option Name (A to Z) Passed. **********")

            # Sorting by Name (Z to A)
            logger.info("********** Verifying sorting by option Name (Z to A). **********")
            self.products.selectSortingMethod("Name (Z to A)")
            productname = self.products.getProductDetailsList("ProductName")
            logger.info("Expected Product name list after sorting: %s", data["Name (Z to A)"])
            logger.info("Actual Product name list after sorting: %s", productname)
            assert productname == data["Name (Z to A)"], "Sorting by Name (Z to A) failed."
            logger.info("********** Sorting by option Name (Z to A) Passed. **********")

            # Sorting by Price (low to high)
            logger.info("********** Verifying sorting by option Price (low to high). **********")
            self.products.selectSortingMethod("Price (low to high)")
            productprice = self.products.getProductDetailsList("ProductPrice")
            logger.info("Expected Product price list after sorting: %s", data["Price (low to high)"])
            logger.info("Actual Product price list after sorting: %s", productprice)
            assert productprice == data["Price (low to high)"], "Sorting by Price (low to high) failed."
            logger.info("********** Sorting by option Price (low to high) Passed. **********")

            # Sorting by Price (high to low)
            logger.info("********** Verifying sorting by option Price (high to low). **********")
            self.products.selectSortingMethod("Price (high to low)")
            productprice = self.products.getProductDetailsList("ProductPrice")
            logger.info("Expected Product price list after sorting: %s", data["Price (high to low)"])
            logger.info("Actual Product price list after sorting: %s", productprice)
            assert productprice == data["Price (high to low)"], "Sorting by Price (high to low) failed."
            logger.info("********** Sorting by option Price (high to low) Passed. **********")

        except Exception as e:
            screenshot_path = os.path.join(".\\Screenshots\\", "test_Sorting.png")
            self.driver.save_screenshot(screenshot_path)
            logger.error("Error occurred: %s", e)
            logger.error("Traceback: %s", traceback.format_exc())
            raise
        finally:
            logger.info("************* Finishing Test case. **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    """
    Generate a random string of specified size with given characters.
    """
    return ''.join(random.choice(chars) for _ in range(size))
