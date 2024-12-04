import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class DemoGetText():
    def demo_get_text(self):
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        print(driver.title)
        text=driver.find_element(By.XPATH,"//h6[contains(text(),'Search for exclusive deals on flights and hotels. ')]").text
        print(text)
        time.sleep(10.00)
demotext=DemoGetText()
demotext.demo_get_text()