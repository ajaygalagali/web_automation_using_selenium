from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()#put path of chromedriver.exe
driver.get('https://web.whatsapp.com/')

msges = ['Hello','Good morning','How are you?','Have a nice day','These messages are sent by python program']
flag = True
while flag:
    name = input("Enter Contact Name :") #type exit to end program
    if name == "exit":
        flag = False
    else:
        for i in range(len(msges)):
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]'))).click()
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]'))).send_keys(name)
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]'))).send_keys(Keys.RETURN)
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))).send_keys(msges[i])
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))).send_keys(Keys.RETURN)


