from selenium.webdriver.common.by import By

class Add_button ():
    def __init__(self, driver):
        self.driver=driver
    def itemOne (self):
        list=["add-to-cart-sauce-labs-backpack","add-to-cart-sauce-labs-bike-light","add-to-cart-sauce-labs-bolt-t-shirt","add-to-cart-sauce-labs-fleece-jacket","add-to-cart-sauce-labs-onesie","add-to-cart-test.allthethings()-t-shirt-(red)"]
        list2=["remove-sauce-labs-backpack","remove-sauce-labs-bike-light","remove-sauce-labs-bolt-t-shirt","remove-sauce-labs-fleece-jacket","remove-sauce-labs-onesie","remove-test.allthethings()-t-shirt-(red)"]
        brojac = 0
        for l in list: 
            item_button=self.driver.find_element(By.ID, l)
            item_button.click()
            try:
                item_button2=self.driver.find_element(By.ID,list2[brojac])
                print("Button {} is clickabile".format(brojac+1))
            except:
                print('Button {} not working'.format(brojac+1))
            brojac = brojac + 1        
