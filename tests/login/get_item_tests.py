from utilities.teststatus import TestStatus
import unittest
import pytest
from api.api import ApiMethods

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class GetItemTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.api = ApiMethods(self.driver)
        self.ts = TestStatus(self.driver


    @pytest.mark.api
    @pytest.mark.run()
    def test_getInfoMediaLibrary(self):

        # Create a Plus User
        newUser["email"] = EMAIL
		newUser["password"] = PASSWORD
		ITEM_ID = ID_EXAMPLE

        # Log into API
        self.api.login(newUser["email"], newUser["password"])

        # Get ITEM Details using API
        expectedMediaDetails = self.api.getItem(ITEM_ID)
