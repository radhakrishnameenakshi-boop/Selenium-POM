# from HomePage import *
# from LoginPage import *
# import pytest

# def test_login(sam):
#     obj1 = HomePage(sam)
#     obj1.login()
#
#     obj2 = LoginPage(sam)
#     obj2.login()

from HomePage import *
from LoginPage import *
import pytest

data = [('Meenakshi@gmail.com','Meenu'),('Chandana@gmail.com','Chandhu')]
args = "username,password"

@pytest.mark.parametrize(args,data)
def test_login(sam,username,password):
    obj1 = HomePage(sam)
    obj1.login()

    obj2 = LoginPage(sam)
    obj2.login(username,password)