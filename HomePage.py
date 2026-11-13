from lib import *
class HomePage:

    locators = {
        "Login":("xpath","//*[text()='Log in']"),
        "Register":("xpath","//*[text()='Register']")
    }
    def __init__(self,driver):
        self.driver =driver

    def login(self):
        obj1 = wrapper(self.driver)
        obj1.clicking(self.locators["Login"])

    def register(self):
        obj2 = wrapper(self.driver)
        obj2.clicking(self.locators["Register"])
