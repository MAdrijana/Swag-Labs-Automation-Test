import unittest
from selenium import webdriver
import time
from logInPage import LogIn_Page
from AddToCart import Add_button

class Test_User3(unittest.TestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.saucedemo.com/"
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()
        time.sleep(0.5) 
        
    def test_login(self):
        driver = self.driver 
        login = LogIn_Page(driver)
        login.enter_username("problem_user")
        login.enter_password("secret_sauce")
        login.click_login()
        time.sleep(2)

    def test_addtocart(self):
        driver = self.driver
        btn = Add_button(driver)
        btn.itemOne()
   
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()