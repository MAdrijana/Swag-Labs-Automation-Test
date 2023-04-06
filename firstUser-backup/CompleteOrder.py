from selenium.webdriver.common.by import By
import time
from screenshot import ScreenshotTool
class Complete_Order():
    def __init__(self, driver):
        self.driver=driver
        self.Name="firstName"
        self.LastName="lastName"
        self.Code="postal-code"
    def complete_the_order(self):
        firstName = self.driver.find_element(By.NAME,self.Name)
        firstName.click()
        firstName.send_keys("Petar")
        time.sleep(0.5)
        lastName = self.driver.find_element(By.NAME, self.LastName)
        lastName.click()
        lastName.send_keys("Petrovic")
        time.sleep(0.5)
        postalCode = self.driver.find_element(By.ID, self.Code)
        postalCode.click()
        postalCode.send_keys("Petar12")
        time.sleep(0.5)
    # We confirm that the data entered is correct, and completing a purchase.
    def Finish (self):
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, "finish").click()
    # We are checking to see if the order has been successfully completed
    def RunAssertion (self):
        Completed_text=self.driver.find_element(By.CLASS_NAME, "complete-text")
        if Completed_text.text=="Your order has been dispatched, and will arrive just as fast as the pony can get there!":
            print("The order is completed successfully.")
            
        else:
            print("The order is not completed successfully.")
            self.driver.save_screenshot("complete.png")