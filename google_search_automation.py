from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome() #put path of chromedriver.exe

driver.get('https://www.google.com/')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'))).send_keys('songs')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]'))).click()



