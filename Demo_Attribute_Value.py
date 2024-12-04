import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class DemoGetAttributeValue():
    def demo_get_attribute(self):
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        print(driver.title)
        text=driver.find_element(By.XPATH,"//p[@class='MuiTypography-root MuiTypography-body1 css-1r4xs6e']").get_attribute("class")
        print(text)
        time.sleep(4.00)
attributevalue=DemoGetAttributeValue()
attributevalue.demo_get_attribute()