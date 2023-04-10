import unittest
from selenium import webdriver
import time
from login import LogInPage
from Addtocart import Add

class Test_User4(unittest.TestCase):
    @classmethod
    def setUp(cls):
        super().setUp(cls)
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.saucedemo.com/"
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()
        time.sleep(0.5) 
    def tearDown(self):
        super().tearDown()

    def test_User4 (self):
        driver = self.driver 
        login = LogInPage(driver)
        login.enter_username("performance_glitch_user")
        login.enter_password("secret_sauce")
        login.click_login()

        driver = self.driver
        add= Add(driver)
        add.Add_Cart()
            

    def tearDown(self):
        super().tearDown()

if __name__ == '__main__':
    unittest.main()        