from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# created the object for chromdriver that talks to Chrom Browser
driver = webdriver.Chrome()
print('maximizing the browser window')
driver.maximize_window()
#driver = webdriver.Firefox()

driver.get("https://www.google.com/")
time.sleep(8)


result = driver.find_element(By.ID, "result-stats")
print(f'Search is done and result text is : {result.text}')

print('closing the browser after test')
driver.quit()
print('test completed')