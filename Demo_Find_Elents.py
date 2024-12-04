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
        lista=driver.find_elements(By.TAG_NAME,"a")
        print(len(lista))
        for x in lista:
            print(x.text)
        listb = driver.find_elements(By.TAG_NAME, "input")
        print(len(listb))
        time.sleep(3.00)
findbyid=FindElementByID()
findbyid.locate_by_id_demo()