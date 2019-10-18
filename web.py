from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get( "http://www.onliner.by" )
assert "Onliner" in driver.title
elem = driver.find_element_by_xpath( "//*[@id='fast-search']/form/input[1]" )
elem.send_keys('Iphone')

#elem = driver.find_element_by_xpath( "//div[@id='search-page']/div[@class='search__bar']//input" )
#elem.send_keys('iPhone 6')

driver.get("https://catalog.onliner.by/mobile/apple/iphone632gbg")
driver.get("https://catalog.onliner.by/mobile/apple/iphone632gbg/prices?town=minsk&order=shop_rating:desc")

#browser = webdriver.Chrome()
#browser.find_elements_by_xpath("//div[@id='search-page']/div[@class='search__bar']//input")


time.sleep(5)
driver.close()
