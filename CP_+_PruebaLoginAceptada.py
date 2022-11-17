from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PATH= "C:\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get('https://magento.softwaretestingboard.com/')
title=driver.title

time.sleep(5)
element=driver.find_element(By.LINK_TEXT,'Sign In')
element.click()
form2=driver.find_element(By.ID,'email')
form2.send_keys('roni_cost@example.com')
form1=driver.find_element(By.ID,'pass')
form1.send_keys('roni_cost3@example.com')
form1.send_keys(Keys.RETURN)



