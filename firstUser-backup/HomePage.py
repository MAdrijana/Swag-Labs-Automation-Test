from selenium.webdriver.common.by import By
import time
from os import path, makedirs, getcwd

class homePage():
    def __init__(self, driver):
        self.driver=driver
        self.add_button ="add-to-cart-sauce-labs-backpack"
        self.cart_badge_xpath="/html/body/div/div/div/div[1]/div[1]/div[3]/a"
        self.item_backPack="item_4_title_link"
        self.itemTwo="//*[@id='add-to-cart-sauce-labs-bike-light']"
        self.itemTree="add-to-cart-sauce-labs-bolt-t-shirt"
        self.itemFour="add-to-cart-sauce-labs-fleece-jacket"
        self.itemFive="add-to-cart-sauce-labs-onesie"
        self.itemSix="add-to-cart-test.allthethings()-t-shirt-(red)"
    # We are adding an item to the cart
    def click_AddToCart(self):
        item_backPack=self.driver.find_element(By.ID,self.item_backPack)
        item_backPack.click()
        add_button=self.driver.find_element(By.ID, self.add_button)
        add_button.click()
        time.sleep(2)
    def second_item(self):
        item_bikeLight=self.driver.find_element(By.XPATH, self.itemTwo)    
        item_bikeLight.click()
        time.sleep(0.5)
    def third_item(self):
        item_boltTshirt=self.driver.find_element(By.ID, self.itemTree)    
        item_boltTshirt.click()
        time.sleep(0.5)
    def Four_item(self):
        item_FleeeJacket=self.driver.find_element(By.ID, self.itemFour)    
        item_FleeeJacket.click()
        time.sleep(0.5)
    def Five_item(self):
        item_LabsOnesie=self.driver.find_element(By.ID, self.itemFive)    
        item_LabsOnesie.click()
        time.sleep(0.5)
    def Six_item(self):
        item_FleeeJacket=self.driver.find_element(By.ID, self.itemSix)    
        item_FleeeJacket.click()
        time.sleep(0.5)    

    #We check that the cart badge has been successfully updated, and we're getting a response at the terminal
    def runAssertion(self):   
        cart_icon = self.driver.find_element(By.XPATH, self.cart_badge_xpath)
        time.sleep(0.5)
        if cart_icon and cart_icon.text==str(6):
            assert True
            print("Cart badge is update correctly ")
            time.sleep(0.5)
        else:
            #testName="CartBadge" 
            #Folder=path.join(getcwd(), testName)
            self.driver.save_screenshot("CartBadge.png")
            #if not path.exists(Folder):
                #makedirs(Folder)
                #self.driver.save_screenshot("CartBadge.png")
           
