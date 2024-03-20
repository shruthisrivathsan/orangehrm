from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

class LoginPage:

    def __init__(self):
        """method to initialise"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def boot(self):
        """method to access the url and to maximise it"""
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()

    def quit(self):
        """method to quit driver"""
        self.driver.quit()

    def login(self):
        """method created to use the locators to enter the user name and password
            this method also updates the test results in excel sheet"""
        try:
            self.boot()
            for row in range(2, data.WebData().rowCount()+1):
                username = data.WebData().readData(row, 2)
                password = data.WebData().readData(row, 3)

                locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, username)
                locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, password)
                locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
                if self.driver.current_url == data.WebData().dashboardURL:
                    print("Successfully logged in")
                    locator.WebLocators().dropDown(self.driver, locator.WebLocators().dropDownLocator)
                    locator.WebLocators().logOut(self.driver)
                    data.WebData().writeData(row, 7, "passed")
                else:
                    print("Login unsuccessful")
                    data.WebData().writeData(row, 7, "failed")
            test_datetime = datetime.now()
            test_date = test_datetime.strftime("%Y-%m-%d")
            test_time = test_datetime.strftime("%H:%m:%s")

            data.WebData().writeTestDate(row, test_date)
            data.WebData().writeTestTime(row, test_time)

        except NoSuchElementException as e:
            print(f"Error:{e}")

        finally:
            self.quit()

obj = LoginPage()
obj.login()
