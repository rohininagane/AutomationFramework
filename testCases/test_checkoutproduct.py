import os
import time
import traceback
import pytest
from pageObjects.ProductsPage import ProductsPage
from pageObjects.CartPage import CartPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.CheckOutOverviewPage import CheckOutOverviewPage
from utilities.customLogger import LogGen

class Test_CheckoutProduct:

    @pytest.mark.parametrize("firstname,lastname,postalcode,productname", [("Kate", "Wilson", "2150","Sauce Labs Backpack")])
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.ui
    def test_checkoutproduct(self, login, firstname, lastname, postalcode,productname):
        """
        Test the product checkout functionality from adding to cart to successful order completion.
         """
        logger = LogGen.loggen("CheckoutProduct")
        logger.info("************* Verify product checkout functionality **********")
        self.driver = login
        logger.info("************* Login successful **********")

        try:
            self.product = ProductsPage(self.driver)
            self.product.clickAddToCart()
            logger.info("************* Clicked on add to cart for product: %s **********",productname)

            self.product.clickOnCart()
            logger.info("************* Clicked on cart symbol **********")

            self.cart = CartPage(self.driver)
            self.cart.clickOnCheckout()
            logger.info("************* Clicked on checkout **********")

            self.checkout = CheckoutPage(self.driver)
            self.checkout.setFirstName(firstname)
            logger.info("************* Entered first name:%s **********",firstname)

            self.checkout.setLastName(lastname)
            logger.info("************* Entered last name:%s **********",lastname)

            self.checkout.setPostalCode(postalcode)
            logger.info("************* Entered postal code:%s **********",postalcode)

            self.checkout.clickContinue()
            logger.info("************* Clicked on continue **********")

            self.finalcheckout = CheckOutOverviewPage(self.driver)
            flag = self.finalcheckout.verifyWebelements()
            assert flag, "Failed to verify UI elements on checkout overview page"
            logger.info("************* Verified product name on chekcout page:%s **********",productname)
            logger.info("************* Verified firstname:%s , lastname:%s, postalcode:%s on checkout page.*************",firstname,lastname,postalcode)
            logger.info("************* Verified payment,shipping info and price total *************")
            logger.info("************* Verified all UI elements on checkout overview page **********")

            self.finalcheckout.clickFinish()
            logger.info("************* Clicked on Finish button **********")

            successmsg = self.finalcheckout.getSuccessMessage()
            detailedmsg = self.finalcheckout.getDetailedSuccessMessage()

            assert successmsg == "Thank you for your order!", "Success message did not match"
            assert detailedmsg == "Your order has been dispatched, and will arrive just as fast as the pony can get there!", "Detailed success message did not match"
            logger.info("************* Verified success messages header:%s **********",successmsg)
            logger.info("************* Verified detailed success messages:%s **********", detailedmsg)

        except Exception as e:
            screenshot_path = os.path.join(".\\Screenshots\\", "test_checkoutproduct.png")
            self.driver.save_screenshot(screenshot_path)
            logger.error("Error occurred: %s", e)
            logger.error("Traceback: %s", traceback.format_exc())
            raise

        finally:
            logger.info("************* Finishing Test case. **********")
