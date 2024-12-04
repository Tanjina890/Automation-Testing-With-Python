import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class DemoSeleniumLearning():
    def demo_browser_methods(self):
        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        time.sleep(3.00)
        driver.refresh()
        time.sleep(2.00)
        driver.find_element(By.LINK_TEXT,"ALL COURSES").click()
        time.sleep(3.00)
        driver.back()
        time.sleep(3.00)
        driver.forward()
        time.sleep(3.00)
        driver.minimize_window()
        time.sleep(5.00)
        driver.quit()
demobrowser=DemoSeleniumLearning()
demobrowser.demo_browser_methods()