from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('../driver/chromedriver.exe')

time.sleep(5)
driver.quit()