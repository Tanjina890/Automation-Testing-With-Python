import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
class DemoJS():
    def demo_java_script(self):
        #driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/courses','_self');")
        driver.maximize_window()
        print(driver.title)
        time.sleep(4.00)
        demo_element=driver.execute_script("return document.getElementsByTagName('p')[0];")
        driver.execute_script("arguments[0].click();",demo_element)
        time.sleep(4.00)
demojs=DemoJS()
demojs.demo_java_script()