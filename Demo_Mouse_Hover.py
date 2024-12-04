import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
class DemoMouse_Hover():
    def demo_Mouse_Events(self):
        driver.get("https://bssoln.com/")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        about=driver.find_element(By.XPATH,"//span[normalize-space()='About']")
        achains=ActionChains(driver)
        achains.move_to_element(about).perform()
        time.sleep(2.00)
        driver.find_element(By.XPATH,"//a[normalize-space()='Portfolio']").click()
        print(driver.current_url)
        time.sleep(3.00)
        driver.back()
        time.sleep(2.00)
        hire=driver.find_element(By.XPATH,"//a[@class='dropdown-item'][normalize-space()='Hire A Developer']")
        achains.move_to_element(hire).perform()
        time.sleep(2.00)
        resources = driver.find_element(By.XPATH, "//span[normalize-space()='Resources']")
        achains.move_to_element(resources).perform()
        time.sleep(3.00)
mouseaction = DemoMouse_Hover()
mouseaction.demo_Mouse_Events()


