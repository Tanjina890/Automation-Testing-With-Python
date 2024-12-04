import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class FindElementByID():
    def locate_by_id_demo(self):
        driver.get("https://www.w3schools.com/")
        driver.maximize_window()
        print(driver.title)
        time.sleep(6.00)
        driver.find_element(By.LINK_TEXT,"Get Certified").click()
        time.sleep(10.00)
findbyid=FindElementByID()
findbyid.locate_by_id_demo()