from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

HOST = "https://demoqa.com/text-box"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
# chr_options.add_experimental_option('excludeSwitches',["disable-popup-blocking"])
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()

print('Starting test with various locator to use in  find_element() method')

driver.get(HOST)
time.sleep(5)

fullname = driver.find_element(By.ID, 'userName')
fullname.send_keys('John')

# driver.find_element(By.NAME, 'q')



driver.find_element(By.TAG_NAME, 'textarea').send_keys("selenium found texterea on html, this is first element of this type")
element_list = driver.find_elements(By.CLASS_NAME, 'form-control')
print(element_list)
print(f'Number of elements in primary_buttons list: {len(element_list)}')
time.sleep(5)
print("opening the google for link text locator..")

driver.get('https://www.google.com/')
driver.find_element(By.LINK_TEXT, 'Gmail')
driver.find_element(By.PARTIAL_LINK_TEXT, 'mail').click()



time.sleep(5)
driver.quit()
print('Test is complited!!')