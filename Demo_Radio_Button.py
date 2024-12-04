import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class DemoRadio():
    def demo_Radio_Button(self):
        driver.get("https://practice.expandtesting.com/radio-buttons")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        driver.find_element(By.XPATH,"//input[@id='red']").click()
        time.sleep(2.00)
        driver.find_element(By.XPATH, "//input[@id='black']").click()
        time.sleep(2.00)
        print(driver.find_element(By.XPATH, "//input[@id='red']").is_selected())
        time.sleep(2.00)
        driver.find_element(By.XPATH, "//input[@id='football']").click()
        time.sleep(2.00)

radiobutton=DemoRadio()
radiobutton.demo_Radio_Button()