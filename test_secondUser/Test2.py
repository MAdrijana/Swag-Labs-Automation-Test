import unittest
from selenium import webdriver
import time
from loginPage import Login_Page

class SwagLabsTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        super().setUp(cls)
        cls.driver = webdriver.Chrome()
        cls.base_url="https://www.saucedemo.com/"
        time.sleep(0.5)
        driver=cls.driver
        driver.get(cls.base_url)
        driver.maximize_window()
        time.sleep(0.5)
    def tearDown(self):
        super().tearDown()
             
    def test_User2 (self):
        driver= self.driver 
        login=Login_Page(driver)
        login.enter_username("locked_out_user")
        login.enter_password("secret_sauce")
        login.click_login()
 
if __name__ == '__main__':
   
    unittest.main()        
    