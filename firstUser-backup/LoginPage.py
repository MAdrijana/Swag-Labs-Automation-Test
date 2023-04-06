from selenium.webdriver.common.by import By
import time

class loginPage():
    def __init__(self, driver):
        self.driver=driver
        self.user_id="user-name"
        self.password_id="password"
        self.login_button_name="login-button"


    def enter_username(self,username):
        self.driver.find_element(By.ID, self.user_id).send_keys(username)
        time.sleep(4)
    def enter_password(self, password):
        self.driver.find_element(By.ID,self.password_id).send_keys(password) 
        time.sleep(2)
    def click_login(self,):
        self.driver.find_element(By.NAME,self.login_button_name).click()
        time.sleep(4)


        
    