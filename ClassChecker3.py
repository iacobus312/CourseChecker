from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://eaen.bc.edu/student-registration/#/")

search = driver.find_element(By.CLASS_NAME, value="searchTextForFilters")

input_class = input("Enter Class Name: ")
search.send_keys(input_class)
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit
