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
