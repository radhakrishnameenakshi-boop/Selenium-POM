# class RegisterPage:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def register(self):
#         self.driver.find_element("id","gender-female").click()
#         self.driver.find_element("id","FirstName").send_keys("Meenakshi")
#         self.driver.find_element("id","LastName").send_keys("R")
#         self.driver.find_element("id","Email").send_keys("Meenakshi@gmail.com")
#         self.driver.find_element("id","Password").send_keys("Meenu")
#         self.driver.find_element("id","ConfirmPassword").send_keys("Meenu")


# class RegisterPage:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def register(self,gender,FName,LName,Email,Password,ConfirmPassword):
#         if gender.lower() =='male':
#             self.driver.find_element("id", "gender-male").click()
#         else:
#             self.driver.find_element("id","gender-female").click()
#
#         self.driver.find_element("id","FirstName").send_keys(FName)
#         self.driver.find_element("id","LastName").send_keys(LName)
#         self.driver.find_element("id","Email").send_keys(Email)
#         self.driver.find_element("id","Password").send_keys(Password)
#         self.driver.find_element("id","ConfirmPassword").send_keys(ConfirmPassword)

# from lib import *
# class RegisterPage:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     def register(self,gender,FName,LName,Email,Password,ConfirmPassword):
#         obj1 = wrapper(self.driver)
#         if gender.lower() =='male':
#             obj1.clicking(("id", "gender-male"))
#         else:
#             obj1.clicking(("id","gender-female"))
#
#         obj1.enterring(("id","FirstName"), FName)
#         obj1.enterring(("id","LastName"), LName)
#         obj1.enterring(("id","Email"),Email)
#         obj1.enterring(("id","Password"), Password)
#         obj1.enterring(("id","ConfirmPassword"),ConfirmPassword)


from lib import *
class RegisterPage:
    locators = {
        "male_rdb":("id","gender-male"),
        "female_rdb":("id","gender-female"),
        "fname":("id","FirstName"),
        "lname":("id","LastName"),
        "email":("id","Email"),
        "password":("id","Password"),
        "confirm_password":("id","ConfirmPassword")
    }
    def __init__(self,driver):
        self.driver = driver
    def register(self,gender,FName,LName,Email,Password,ConfirmPassword):
        obj1 = wrapper(self.driver)
        if gender.lower() =='male':
            obj1.clicking(self.locators["male_rdb"])
        else:
            obj1.clicking(self.locators["female_rdb"])

        obj1.enterring(self.locators["fname"], FName)
        obj1.enterring(self.locators["lname"], LName)
        obj1.enterring(self.locators["email"],Email)
        obj1.enterring(self.locators["password"], Password)
        obj1.enterring(self.locators["confirm_password"],ConfirmPassword)
