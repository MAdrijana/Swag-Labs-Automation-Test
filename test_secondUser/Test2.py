import unittest
from selenium import webdriver
import time
from loginPage import Login_Page

class SwagLabsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url="https://www.saucedemo.com/"
        time.sleep(0.5)
        driver=self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        time.sleep(0.5)   
    def test_User2 (self):
        driver= self.driver 
        login=Login_Page(driver)
        login.enter_username("locked_out_user")
        login.enter_password("secret_sauce")
        login.click_login()

    def tearDown(self):
        self.driver.quit()
        
 
if __name__ == '__main__':
   
    unittest.main()        
    