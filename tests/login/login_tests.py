from pages.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.run()
    def test_validLogin(self):

        USER = "username"
        PASSWORD = "password"
        self.lp.login(USER, PASSWORD)

        self.lp.verifyLoginSuccessful()
        self.lp.verifyLogoutSuccessful()

    @pytest.mark.run()
    def test_verifyLoginWithSocialMedia(self):
        self.lp.verifyLoginWithSocialMedia()

    @pytest.mark.login
    @pytest.mark.run()
    def test_verifyLinksForgotPasswordAndSignup(self):
        self.lp.verifyLinksForgotPasswordAndSignup()