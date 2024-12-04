import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class DemoWebElementState():
    def demo_element_enableed_disabled(self):
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        print(driver.title)
        state=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(state)
        time.sleep(2.00)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys('testing')
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys('testing343')
        state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state1)
        time.sleep(2.00)
        driver.find_element(By.XPATH, "//input[@id='login_button']").click()
        time.sleep(2.00)
        driver.back()
        time.sleep(2.00)
demostate=DemoWebElementState()
demostate.demo_element_enableed_disabled()