from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from getpass import getpass


def main():
    input1 = input("Enter User: ")
    input2 = getpass("Enter Pass: ")
    input3 = input("Enter Class Name: ")
    
    driver = webdriver.Chrome()
    driver.get("https://services.bc.edu/commoncore/myservices.do")

    username = driver.find_element(By.ID, 'username')
    password = driver.find_element(By.ID, 'password')

    username.send_keys(input1) #type your own username here
    password.send_keys(input2) #type your own password here
    #please don't steal my identity :D
	
    driver.find_element(By.TAG_NAME, "button").click()
    driver.get("https://services.bc.edu/password/external/launcher/generic.do?id=eaPlanningRegistration")

    time.sleep(10)
    
    driver.find_element(By.ID, "mySchedule").click()
    schedule = driver.find_element(By.ID, "seFacetedFiltersViewersearchTextForFilters")
    schedule.send_keys(input3)
    driver.find_element(By.ID, "seFacetedFiltersViewerButtonSearch").click()
    
    time.sleep(10)

    driver.find_element(By.CSS_SELECTOR, ".glyphicon-chevron-right").click()

    time.sleep(15)
main()





