import sys

from selenium import webdriver
import unittest
import  sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains as az
import time
from POMProjectDemo.Pages.loginPage import LoginPage as lg
from POMProjectDemo.Pages.homePage import HomePage as hp
import HtmlTestRunner

# from selenium.webdriver.common import action_chains as az

class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        # login object

        login = lg(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.checking()
        login.click_login()
        # logout object
        homepage = hp(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()

        print("Test completed")


''' self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input").send_keys("Admin")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input").send_keys(
            "admin123")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/a[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[9]/ul/li[3]/a').click()
'''
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/97798/Desktop/.idea"))