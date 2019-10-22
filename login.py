from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../chromedriver.exe')


driver = webdriver.Chrome(filename)
driver.set_window_size(1600,900)
driver.get("https://hygger.io/")

loginbtn = driver.find_element_by_xpath("//*[@id='header']/div/div/div/div[2]/a")
loginbtn.click()

confirmloginbtn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/ng-component/account-form/div/div/form/button")))

email = driver.find_element_by_xpath("//*[@id='mail']")
email.send_keys('testwetanos@gmail.com')

password = driver.find_element_by_xpath("//*[@id='pass']")
password.send_keys('wetanostest')

confirmloginbtn.click()

stayfree = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/app/atlaz-bnp/paywall-layout/div/div/pricing-plans-v3/div[2]/div[1]/div[2]/div[2]")))
stayfree.click()