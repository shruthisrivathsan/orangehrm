from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

class Test:
    # create test cases to check the boot of webpage
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    # create test case to check login
    @pytest.mark.html
    def testSearch(self, boot):
        self.driver.get(data.WebData().url)
        assert self.driver.current_url == data.WebData().dashboardURL
        print("Successful login")





