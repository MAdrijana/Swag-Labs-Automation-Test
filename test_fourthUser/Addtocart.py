from selenium.webdriver.common.by import By
import time

class Add():
    def __init__(self, driver):
        self.driver=driver
        self.item1="add-to-cart-sauce-labs-backpack"
        self.item2="add-to-cart-sauce-labs-bike-light"
        self.item3="add-to-cart-sauce-labs-bolt-t-shirt"
        self.item4="add-to-cart-sauce-labs-fleece-jacket"
        self.item5="add-to-cart-sauce-labs-onesie"
        self.item6="add-to-cart-test.allthethings()-t-shirt-(red)"
    def Add_Cart(self):
        self.driver.find_element(By.NAME, self.item1).click()
        self.driver.find_element(By.ID, self.item2).click()
        self.driver.find_element(By.NAME, self.item3).click()
        self.driver.find_element(By.NAME, self.item4).click()
        self.driver.find_element(By.NAME, self.item5).click()
        self.driver.find_element(By.NAME, self.item6).click()
        time.sleep(2)    









