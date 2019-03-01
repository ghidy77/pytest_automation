import utilities.custom_logger as cl
from pages.media_library_page import MediaLibraryPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ml = MediaLibraryPage(driver)

    # Locators
    email_field = "loginEmail"
    password_field = "loginPassword"
    login_button = "login-btn"
    facebook_login_link = "a[href*='facebook']"
    google_login_link = "a[href*='google']"
    signup_link = "#signup"
    signup_email_field = "input[name='signupEmail']"
    forgot_password_link = ".forgot-password"
    forgot_password_email_field = ".forget-password input[name='email']"
    item = "item"


    def clickFacebookLoginLink(self):
        self.elementClick(self.facebook_login_link)

    def clickGoogleLoginLink(self):
        self.elementClick(self.google_login_link)

    def clickSignupLink(self):
        self.waitForElement(self.signup_link)
        self.elementClick(self.signup_link)
        self.waitForElement(self.signup_email_field)

    def clickForgotPasswordLink(self):
        self.elementClick(self.forgot_password_link)
        self.waitForElement(self.forgot_password_email_field)

    def enterEmail(self, email):
        self.sendKeys(email, self.email_field, locatorType="name")

    def enterPassword(self, password):
        self.sendKeys(password, self.password_field, locatorType="name")

    def clickLoginButton(self):
        self.elementClick(self.login_button)

    def login(self, email, password):
        self.driver.get("https://example.com/login")
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement(self.item)
        assert (self.isElementPresent(self.item)) == True
        self.verifyCurrentUrl("library")

    def verifyLoginWithSocialMedia(self):
        self.driver.get("https://example.com/login")
        self.clickFacebookLoginLink()
        self.verifyCurrentUrl("www.facebook.com/login.php")
        self.driver.back()
        self.clickGoogleLoginLink()
        self.verifyCurrentUrl("accounts.google.com")

    def verifyLinksForgotPasswordAndSignup(self):
        self.driver.get("https://example.com/login")
        self.clickForgotPasswordLink()
        self.verifyCurrentUrl("/forgot-password")
        self.driver.back()
        self.clickSignupLink()
        self.verifyCurrentUrl("/signup")

    def verifyLogoutSuccessful(self):
        self.ml.logout()
        assert (self.isElementPresent(self.item)) == False
        self.verifyCurrentUrl("/login")
