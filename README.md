# README
This is an working example of python automation framework, using pytest

# Prerequisites
    brew install python
*This will install the latest version of Python 3*
- Download latest chromedriver: http://chromedriver.chromium.org/downloads and add it in a PATH directory.

> Example: **cp /Users/your_user/Downloads/chromedriver /usr/local/bin/chromedriver**

*This will add chromedriver executable in PATH*
- Change chromedriver variable in base/webdriver_factory.py to actual executable: /usr/local/bin/chromedriver

# Install
    pip3 install pytest
    pip3 install selenium
    pip3 install requests
    pytest --version #make sure it was properly installed
    

# Run example
    pytest tests/test_suite_demo.py --browser chrome --junitxml=result.xml
    
# other parameters
    -m smoke #selects tests that are marked with the same fixture: example @pytest.mark.smoke 

I'm using PyCharm as IDE: https://www.jetbrains.com/pycharm/download/

You must set in PyCharm (or IntelliJ) the default SDK: 

> SDK - add new (+) - Python SDK - System Interpreter - Pyhton 3.7

# Intro
- base/basepage.py is the template that should be extended by every page of the project. It should contain common methods
- pages/page_example.py any page should contain: locator found specific into that page, methods (actions) available in the page and methods (validations), step scenarios for the page
- tests/test_suite_demo.py will define testsuites to be executed by selecting test files
- tests/directory/example_tests.py is the test file that will be executed.
- screenshots/ will be populated with screenshots taken by selenium webdriver during test execution. it can be customized (only at failure)
- utilities/ this should contain helpers or external methods
- conftest.py must be in project root and it can contain plugins or settings
