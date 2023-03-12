
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")

#url
driver.get("https://letcode.in/dropable")
#action chain function
action=ActionChains(driver)

source=driver.find_element(By.XPATH,"//div[@id='draggable']")
traget=driver.find_element(By.XPATH,"//p[normalize-space()='Drop here']")
action.drag_and_drop(source,traget).perform()