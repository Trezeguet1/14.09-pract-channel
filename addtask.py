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

addtaskbtn = driver.find_element_by_xpath("/html/body/app/atlaz-bnp/app-body/ng-component/page-with-permissions-wrapper/div/div[2]/board-detail/div/list-board-details/list-board-content/div/section/div/list-board-add-task[1]/div/a")
addtaskbtn.click()

tasktitle = driver.find_element_by_xpath("/html/body/app/atlaz-bnp/app-body/ng-component/page-with-permissions-wrapper/div/div[2]/board-detail/div/list-board-details/list-board-content/div/section/div/list-board-add-task[1]/list-board-add-task-form/form/div[1]/textarea")
tasktitle.send_keys('PYTHON TEST TITLE')

description = driver.find_element_by_xpath("//*[@id='due-date']/input").click()
datepicker = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/table/tbody/tr[4]/td[6]").click()tas
dateOK = driver.find_element_by_xpath("/html/body/div[4]/div[4]/a[3]").click()

description = driver.find_element_by_xpath("/html//textarea[@id='description']")
description.send_keys('PYTHON TEST DESCRIPTION')
confirmaddtask = driver.find_element_by_xpath('/html/body/app/atlaz-bnp/app-body/ng-component/page-with-permissions-wrapper/div/div[2]/board-detail/div/list-board-details/list-board-content/div/section/div/list-board-add-task[1]/list-board-add-task-form/form/div[3]/button[1]').click()

time.sleep(6)

if driver.find_element_by_xpath('//*[contains(text(), "PYTHON TEST TITLE")]'): 
	print("TASK WAS CREATED")
driver.close()