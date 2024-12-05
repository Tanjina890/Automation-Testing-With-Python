import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class FindElementByID():
    def locate_by_id_demo(self):
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        print(driver.title)
        driver.find_element(By.ID,"login-input").send_keys('test@test.com')
        time.sleep(4.00)
        driver.find_element(By.XPATH, "//button[@id='login-continue-btn']").click()
        time.sleep(4.00)
        driver.back()
        time.sleep(4.00)
findbyid=FindElementByID()
findbyid.locate_by_id_demo()
