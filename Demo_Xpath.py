import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class FindElementByDEMO():
    def locate_by_demo(self):
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        print(driver.title)
        driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys('test@test.com')
        time.sleep(10.00)
findbyxpath=FindElementByDEMO()
findbyxpath.locate_by_demo()