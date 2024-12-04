import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class FindElementByID():
    def locate_by_id_demo(self):
        driver.get("https://campus.w3schools.com/en-in")
        driver.maximize_window()
        print(driver.title)
        time.sleep(10.00)
        driver.find_element(By.PARTIAL_LINK_TEXT,"Career Pat").click()
        time.sleep(10.00)
findbyid=FindElementByID()
findbyid.locate_by_id_demo()