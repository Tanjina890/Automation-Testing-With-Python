import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
class DemoScreenshot():
    def demo_screen_capture(self):
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        time.sleep(2.00)
        continuedemo=driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuedemo.click()
        time.sleep(2.00)
        #continuedemo.screenshot(".\\test.png")
        driver.save_screenshot(".\\test.png")
        time.sleep(2.00)
        driver.get_screenshot_as_file("E:\\AUTOMATION\\error.png")
        driver.save_screenshot(".\\test1.png")
        time.sleep(1.00)
        driver.refresh()
        time.sleep(2.00)
sc = DemoScreenshot()
sc.demo_screen_capture()