import time

from POMProjectDemo.locator.locaters import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains as az
class LoginPage():
    def __init__(self ,driver):
        self.driver = driver
        self.input_login_username = locators.input_login_username
        self.input_login_password = locators.input_login_password
        self.click_login_button = locators.click_login_button
        self.check = locators.check

    def enter_username(self, username):

        a=self.driver.find_element(By.XPATH , self.input_login_username)
        az.ActionChains(self.driver).send_keys_to_element(a,username).perform()
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.input_login_password).clear()
        b=self.driver.find_element(By.XPATH , self.input_login_password).send_keys(password)
        #az.ActionChains(self.driver).send_keys_to_element(b,password).perform()

    def checking(self):
        global f
        d=self.driver.find_element(By.XPATH,self.check)
        f=d.text
        print(f)
        return f

    def click_login(self):
        c=self.driver.find_element(By.XPATH , self.click_login_button).click()
        az.ActionChains(self.driver).click(c).perform()
