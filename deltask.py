from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

exec(open("login.py").read())

hamburger = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/app/atlaz-bnp/app-header/div[1]/div/div[1]/div")))
hamburger.click()

project = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/app/atlaz-bnp/left-menu/div/div/left-menu-body/div/div[3]/div[3]/left-project-item/left-board-list/ul/li/a")))
project.click()

time.sleep(5)

task = driver.find_element_by_xpath('//*[contains(text(), "PYTHON TEST TITLE")]').click()

dotsicon = driver.find_element_by_xpath("/html/body/app/atlaz-bnp/task-detail-page/div/div/div/task-permission-pages/task-expanded/div/div[1]/content-menu/div")
dotsicon.click()

delbtn = driver.find_element_by_xpath("/html/body/app/atlaz-bnp/task-detail-page/div/div/div/task-permission-pages/task-expanded/div/div[1]/content-menu/div/div[1]/div/p[10]")
delbtn.click()

delwarn = driver.find_element_by_xpath("/html/body/app/atlaz-bnp/task-detail-page/div/div/div/task-permission-pages/task-expanded/div/div[1]/content-menu/div[2]/a-context-container/div/div/div[2]")
delwarn.click()

# пока работаю над этим if not driver.find_element_by_xpath('//*[contains(text(), "PYTHON TEST TITLE")]'): print("TASK WAS DELETED") 
driver.close()