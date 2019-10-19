from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get( "http://www.onliner.by" )
assert "Onliner" in driver.title

elem = driver.find_element_by_xpath( "//*[@id='fast-search']/form/input[1]" )
elem.send_keys('Iphone')

time.sleep(3)

driver.switch_to.frame(driver.find_element_by_css_selector(".modal-iframe"))
iphone = driver.find_element_by_xpath("//*[@id='search-page']/div[2]/ul/li[1]/div/div/div[2]/div/a")
iphone.click()

if driver.find_elements_by_css_selector(".button.button_big.button_orange.offers-description__button"):
    print("ДОСТУПЕН ДЛЯ ПОКУПКИ")

time.sleep(5)
driver.close()
