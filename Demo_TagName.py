import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class FindElementByID():
    def locate_by_id_demo(self):
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        print(driver.title)
        driver.find_element(By.TAG_NAME,"button").click()
        driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys('test@rcvacademy.com')
        driver.find_element(By.ID,"login-continue-btn").click()
        time.sleep(10.00)
findbyid=FindElementByID()
findbyid.locate_by_id_demo()