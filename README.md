# README
This is an working example of python automation framework, using pytest

# Prerequisites
- Download latest version of Python 3: https://www.python.org/downloads/
- Download latest chromedriver: http://chromedriver.chromium.org/downloads
- Add chromedriver executable in PATH
- Change chromedriver variable in base/webdriver_factory.py to actual executable

# Install
    pip install py-test
    pytest --version #make sure it was properly installed
    
# Extra
    pip install requests
Requests lib is used for API calls. 
    
# Run example
    pytest tests/test_suite_demo.py --browser chrome --junitxml=result.xml -s
    
# other parameters
    -m smoke #selects tests that are marked with the same fixture: example @pytest.mark.smoke 

I'm using PyCharm as IDE: https://www.jetbrains.com/pycharm/download/

# Intro
- base/basepage.py is the template that should be extended by every page of the project. It should contain common methods
- pages/page_example.py any page should contain: locator found specific into that page, methods (actions) available in the page and methods (validations), step scenarios for the page
- tests/test_suite_demo.py will define testsuites to be executed by selecting test files
- tests/directory/example_tests.py is the test file that will be executed.
- screenshots/ will be populated with screenshots taken by selenium webdriver during test execution. it can be customized (only at failure)
- utilities/ this should contain helpers or external methods
- conftest.py must be in project root and it can contain plugins or settings