from selenium.webdriver.common.by import By
import time

class cart_Badge():
    def __init__ (self, driver):
        self.driver=driver
        self.button="shopping_cart_container"
        self.checkout="checkout"
    def Cart (self):
        cart_button=self.driver.find_element(By.ID,self.button)  
        cart_button.click()
        time.sleep(0.5)
    def Checkout (self):
        checkout_button=self.driver.find_element(By.ID,self.checkout)   
        checkout_button.click()  
        time.sleep(0.5) 
