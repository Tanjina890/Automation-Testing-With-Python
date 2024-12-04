from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
class DemoImplicitWait():
    def demo_implicit_wait(self):
        driver.implicitly_wait(10.00)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.maximize_window()
        print(driver.title)
        driver.find_element(By.ID,"username").send_keys("RCV Academy")
        driver.find_element(By.ID, "password").send_keys("RCV Academy")
implwait = DemoImplicitWait()
implwait.demo_implicit_wait()
