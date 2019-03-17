import unittest
from tests.login.login_tests import LoginTests
from tests.login.get_info_tests import GetItemTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
api = unittest.TestLoader().loadTestsFromTestCase(GetItemTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([api])

unittest.TextTestRunner(verbosity=2).run(smokeTest)