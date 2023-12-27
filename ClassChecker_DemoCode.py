from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from getpass import getpass


def courseChecker(input1,input2,input3):
    driver = webdriver.Chrome()
    driver.get("https://services.bc.edu/commoncore/myservices.do")

    username = driver.find_element(By.ID, 'username')
    password = driver.find_element(By.ID, 'password')

    username.send_keys(input1) #type your own username here
    password.send_keys(input2) #type your own password here
    #please don't steal my identity :D
	
    driver.find_element(By.TAG_NAME, "button").click()
    driver.get("https://services.bc.edu/password/external/launcher/generic.do?id=eaPlanningRegistration")

    time.sleep(7)
    
    driver.find_element(By.ID, "mySchedule").click()
    schedule = driver.find_element(By.ID, "seFacetedFiltersViewersearchTextForFilters")
    schedule.send_keys(input3)
    driver.find_element(By.ID, "seFacetedFiltersViewerButtonSearch").click()
    
    time.sleep(7)

    driver.find_element(By.CSS_SELECTOR, ".glyphicon-chevron-right").click()

    time.sleep(7)

    page_text = driver.find_element(By.TAG_NAME, 'body').text

    outfile_file = 'output.txt'
    with open(outfile_file, 'w', encoding= 'utf-8') as file:
        file.write(page_text)
    output_creation()
    driver.quit()

def filetolist(input_file, delimiter = ' '):
    two_d_list = []
    with open(input_file, 'r', encoding = 'utf-8') as file:
        for line in file:
            row = line.strip().split(delimiter)
            two_d_list.append(row)
    return two_d_list

def output_creation():
    returnvalue = filetolist('output.txt')
    for row in returnvalue:
        for i in range(len(row)):
            try:
                row[i] = int(row[i])
            except ValueError:
                pass
                    
        if len(row) == 3 and isinstance(row[0], int) and isinstance(row[1], str) and isinstance(row[2], int):
            print(row)
        else:
            returnvalue.remove(row)
def main():
    input1 = input("Enter User: ")
    input2 = getpass("Enter Pass: ")
    input3 = input("Enter Class Name: ")
    courseChecker(input1,input2,input3)
    hello = input("Enter Another Class: ")
    courseChecker(input1,input2,hello)
main()




