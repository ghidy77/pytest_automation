"""
# @package base

This should contain methods common to all pages
This class needs to be inherited by all the page classes
Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
import time

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        # self.util = Util()

    def verifyCurrentUrl(self, expected):
        """
                Verify current URL

                Parameters:
                    expected: string expected to be part of URL
                """
        # url should contain expected string
        assert (self.driver.current_url.find(expected) >= 0) == True

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def sleep(self, seconds):
        time.sleep(seconds)
        self.log.info("Waiting for " + str(seconds) + " seconds")