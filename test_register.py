from HomePage import *
from RegisterPage import *
import pytest


data = [('female','Meenakshi','R','Meenu@gmail.com',
         'Meenu','Meenu'),('female','Chandana','C','Chandhu@gmail.com','Chandu','Chandu')]
args = ("gender,FName,LName,Email,Password,ConfirmPassword")


@pytest.mark.parametrize(args,data)
def test_register(sam,gender,FName,LName,Email,Password,ConfirmPassword):
    obj3 = HomePage(sam)
    obj3.register()

    obj4 = RegisterPage(sam)
    obj4.register(gender,FName,LName,Email,Password,ConfirmPassword)
