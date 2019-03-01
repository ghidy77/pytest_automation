import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class MediaLibraryPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    menuButton = "#menu"
    logoutButton = "logout"
    user_settings_icon = "user_settings"


    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self.user_settings_icon, locatorType="name", pollFrequency=1)
        self.elementClick(element=userSettingsElement)

    def logout(self):
        self.elementClick(self.menuButton)
        self.waitForElement(self.logoutButton, "id")
        self.elementClick(self.logoutButton, "id")
