# class LoginPage:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def login(self):
#         self.driver.find_element("id","Email").send_keys("Meenakshi@gmail.com)
#         self.driver.find_element("id","Password").send_keys("Meenu)
#         self.driver.find_element("xpath","//*[@value='Log in']").click()

# class LoginPage:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def login(self,username,password):
#         self.driver.find_element("id","Email").send_keys(username)
#         self.driver.find_element("id","Password").send_keys(password)
#         self.driver.find_element("xpath","//*[@value='Log in']").click()
# from lib import *
#
# class LoginPage:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def login(self,username,password):
#         obj1 = wrapper(self.driver)
#         obj1.enterring((id","Email"), username)
#         obj1.enterring(("id","Password"), password)
#         obj1.clicking(("xpath","//*[@value='Log in']"))

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