from selenium import webdriver
from selenium.webdriver.common.by import By

#copies entire text of a website and exports it in a textfile

#test case
driver = webdriver.Chrome()
driver.get("https://www.randomtextgenerator.com/")

#main code
page_text = driver.find_element(By.TAG_NAME, 'body').text

outfile_file = 'output.txt'
with open(outfile_file, 'w', encoding= 'utf-8') as file:
    file.write(page_text)

driver.quit()


