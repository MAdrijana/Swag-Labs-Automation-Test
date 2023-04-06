from selenium.webdriver.common.by import By
import time

class Login_Page():
    def __init__(self, driver):
        self.driver=driver
        self.user_id="user-name"
        self.password_id="password"
        self.login_button_name="login-button"
    def enter_username(self,username):
        self.driver.find_element(By.ID, self.user_id).send_keys(username)
        time.sleep(0.5)
    def enter_password(self, password):
        self.driver.find_element(By.ID,self.password_id).send_keys(password) 
        time.sleep(0.5)
    def click_login(self,):
        self.driver.find_element(By.NAME,self.login_button_name).click()
        time.sleep(0.5)

        error_text=self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        time.sleep(0.5)
        if error_text.text == " Epic sadface: Sorry, this user has been locked out.":
            assert True   
        else:
            self.driver.save_screenshot("error.png") 
            