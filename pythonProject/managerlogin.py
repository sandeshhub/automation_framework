
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains as az
import time

valid_email="nabingyawali.298@allpasal.test"
valid_password='123456'







s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://testpasal.com/')
# driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')
time.sleep(3)
loginbtn=driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div/header/div/div/div[4]/button')

#az.ActionChains(driver).move_to_element(loginbtn).click(loginbtn).perform()

az.ActionChains(driver).click(loginbtn).perform()
time.sleep(2)
loginbtn1=driver.find_element(By.XPATH,value='/html/body/div[1]/div[2]/div/a[3]/div/span')
az.ActionChains(driver).click(loginbtn1).perform()
time.sleep(2)
emailinput=driver.find_element(By.XPATH,value='/html/body/div[1]/div[1]/div/main/div/div[2]/div/div/div/form/div/div[2]/div/div/div[1]/div[2]/input')
emailinput.send_keys(valid_email)
passwordinput=driver.find_element(By.XPATH,value='/html/body/div[1]/div[1]/div/main/div/div[2]/div/div/div/form/div/div[3]/div/div/div[1]/div[2]/input')
passwordinput.send_keys(valid_password)
storelogin=driver.find_element(By.XPATH,value= '/html/body/div[1]/div[1]/div/main/div/div[2]/div/div/div/form/div/div[4]/button/span')
az.ActionChains(driver).click(storelogin).perform()

'''time.sleep(2)
dashboard=driver.find_element(By.XPATH,value='/html/body/div[1]/div[1]/div/header/div/div/div[5]/button')
az.ActionChains(driver).click(dashboard).perform()

dashboardclick=driver.find_element(By.XPATH,value='/html/body/div[1]/div[2]/div/div/div/span')
az.ActionChains(driver).click(dashboardclick).perform()'''
time.sleep(3)
loggeduser=driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/nav/div[1]/div/div[1]/div[2]/div[2]').text

if (valid_email==loggeduser):
    print ("User logged in successfully with valid username and valid password ")
    print("Passed the test")
else:
    print("Didn,t logged in successfully")






