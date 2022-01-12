from POMProjectDemo.locator.locaters import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains as az
import time
class HomePage():
    def __init__(self,driver):
        self.driver = driver
        driver = self.driver

        self.click_welcome_link = locators.click_welcome_link
        self.click_logout_link = locators.click_logout_link

    def click_welcome(self):
        time.sleep(1)
        l=self.driver.find_element(By.XPATH, self.click_welcome_link)
        az.ActionChains(self.driver).click(l).perform()
        time.sleep(1)

    def click_logout(self):
        p=self.driver.find_element(By.XPATH, self.click_logout_link).click()
        az.ActionChains(self.driver).click(p).perform()


