from lib import *

class LoginPage:

    locators = {
        "email":("id","Email"),
        "password":("id","Password"),
        "login":("xpath","//*[@value='Log in']")
    }
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        obj1 = wrapper(self.driver)
        obj1.enterring(self.locators['email'], username)
        obj1.enterring(self.locators['password'], password)
        obj1.clicking(self.locators['login'])
