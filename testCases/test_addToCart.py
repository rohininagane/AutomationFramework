import os
import traceback
import pytest
from pageObjects.ProductsPage import ProductsPage
from pageObjects.CartPage import CartPage
from utilities.customLogger import LogGen

class Test_AddToCart:
    @pytest.mark.parametrize("productname", ["Sauce Labs Backpack"])
    @pytest.mark.regression
    @pytest.mark.ui
    def test_addtocart(self, login, productname):
        """
        Test to verify the 'Add to Cart' functionality.
        """
        logger = LogGen.loggen("AddToCart")
        self.driver = login
        try:
            logger.info("************* Starting Test: Verify add to cart functionality **********")

            logger.info("************* Clicking 'Add to Cart' for product: %s **********",productname)
            self.product = ProductsPage(self.driver)
            self.product.clickAddToCart()

            # Navigate to the Cart page
            logger.info("************* Navigating to Cart page **********")
            self.product.clickOnCart()
            self.cart = CartPage(self.driver)

            # Verify product in the cart
            product = self.cart.getProductName()
            flag = self.cart.verifyWebelements()
            assert flag and product == productname, "UI element verification on cart page failed or product name mismatch."
            logger.info("************* Product added to cart successfully. Product name on cart page: %s **********",product)
            logger.info("************* Add To Cart Test case passed. **********")
        except Exception as e:
            screenshot_path = os.path.join(".\\Screenshots\\", "test_addtocart.png")
            self.driver.save_screenshot(screenshot_path)
            logger.error("Error occurred: %s", e)
            logger.error("Traceback: %s", traceback.format_exc())
            raise
        finally:
            logger.info("************* Finishing Test case. **********")

