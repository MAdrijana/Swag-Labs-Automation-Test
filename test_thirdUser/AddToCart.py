from selenium.webdriver.common.by import By
import time

class Add_button ():
    def __init__(self, driver):
        self.driver=driver
        self.item_one="//*[@id='remove-sauce-labs-backpack']"
    def itemOne (self):
        item_button=self.driver.find_element(By.XPATH, self.item_one)
        item_button.click()
        time.sleep(1)