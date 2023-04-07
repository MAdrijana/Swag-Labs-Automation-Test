import unittest
from selenium import webdriver
import time
from LoginPage import loginPage
from HomePage import homePage
from CartBadge import cart_Badge
from CompleteOrder import Complete_Order
from selenium.webdriver.common.by import By

class Test_User1(unittest.TestCase):
    @classmethod
    def setUp(cls):
        super().setUp(cls)
        cls.driver = webdriver.Chrome()
        cls.base_url="https://www.saucedemo.com/"
        time.sleep(1)
        driver=cls.driver
        driver.get(cls.base_url)
        driver.maximize_window()
        time.sleep(0.5) 
    def tearDown(self):
        super().tearDown() 

    def test_User1 (self):
        driver= self.driver 
        login=loginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

    # We are adding an item to the cart
        addToCart=homePage(self.driver)
        addToCart.click_AddToCart()
    # Back to Home Page    
        self.driver.find_element(By.NAME, "back-to-products").click()
        time.sleep(1) 
        secItem=homePage(self.driver)
        secItem.second_item()
        trdItem=homePage(self.driver)
        trdItem.third_item()   
        FourItem=homePage(self.driver)
        FourItem.Four_item()  
        FiveItem=homePage(self.driver)
        FiveItem.Five_item() 
        SixItem=homePage(self.driver)
        SixItem.Six_item()
               
    #We check that the cart badge has been successfully updated, and we're getting a response at the terminal
        Cart=homePage(self.driver)
        Cart.runAssertion()

    # Go to cart badge
        cart=cart_Badge(self.driver)
        cart.Cart()
        cart.Checkout()
   
    # Continue to the Checkout page and Complete the checkout form
        completeOrder=Complete_Order(self.driver)
        completeOrder.complete_the_order()
        finish=Complete_Order(self.driver)
        finish.Finish()
        completed=Complete_Order(self.driver)
        completed.RunAssertion()
 
if __name__ == '__main__':
   
    unittest.main()        
