import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
class DemoIFrame():
    def demo_frames(self):
        driver.get("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_element_iframe")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        #Switch with iFrame Locator
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        # Switch with iFrame index
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH,"//iframe[@id='myFrame']").click()
        time.sleep(4.00)

dIFrame = DemoIFrame()
dIFrame.demo_frames()