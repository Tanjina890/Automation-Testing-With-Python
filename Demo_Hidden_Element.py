import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class DemoHiddenElementState():
    def demo_is_displayed(self):
         driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
         driver.maximize_window()
         elem=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
         print(elem)
         time.sleep(2)
         driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
         time.sleep(3)
         elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
         print(elem1)
element=DemoHiddenElementState()
element.demo_is_displayed()