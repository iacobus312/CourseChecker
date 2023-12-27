
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



def main():
	driver = webdriver.Chrome()
	driver.get("https://services.bc.edu/commoncore/myservices.do")

	username = driver.find_element(By.ID, 'username')
	password = driver.find_element(By.ID, 'password')

	username.send_keys("username") #type your own username here
	password.send_keys("password") #type your own password here
	#please don't steal my identity :D
	
	driver.find_element(By.TAG_NAME, "button").click()

	#driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div[1]/div[2]/ul/li[8]').click()
	driver.get("https://services.bc.edu/password/external/launcher/generic.do?id=eaPlanningRegistration")

main()
