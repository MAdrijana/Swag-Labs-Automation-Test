import time
from selenium.webdriver.common.by import By

class Cart_Update(): 
    def __init__(self, driver):
        self.driver=driver
        self.cart_badge_xpath ="//*[@id='shopping_cart_container']/a"

    def runAssertion(self): 
            
            cart_icon = self.driver.find_element(By.XPATH, self.cart_badge_xpath)
            time.sleep(0.5)
            if cart_icon and cart_icon.text =="6":
               assert True
            else:
                self.driver.save_screenshot("CartBadge.png")
                print ("Error occurred! Cart is not well updated")