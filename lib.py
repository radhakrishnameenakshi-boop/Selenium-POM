class wrapper:

    def __init__(self,driver):
        self.driver = driver

    def clicking(self,locator):
        self.driver.find_element(*locator).click()

    def enterring(self,locator,data):
        self.driver.find_element(*locator).send_keys(data)

