from selenium.webdriver.common.by import By

class WebLocators:

    def __init__(self):
        """this method to the locate the username, password text boxes, the drop down button and the login and logout buttons """
        self.usernameLocator = "username"
        self.passwordLocator = "password"
        self.buttonLocator = "button"
        self.dropDownLocator = "oxd-userdropdown-name"
        self.logoutLocator = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"

    def enterText(self, driver, locator, textValue):
        """ this method is to locate the element using NAME and enter the text """
        element =driver.find_element(by=By.NAME, value=locator)
        element.clear()
        element.send_keys(textValue)

    def clickButton(self, driver, locator):
        """this method is to locate and click the login button"""
        driver.find_element(by=By.TAG_NAME, value=locator).click()

    def dropDown(self, driver, locator):
        """this method is to locate and click the dropdown list using the class name"""
        driver.find_element(by= By.CLASS_NAME, value=locator).click()

    def logOut(self, driver, ):
        """ this method is to locate and click the logout button from the drop down list"""
        driver.find_element(by = By.XPATH, value=self.logoutLocator).click()
