import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
class DemoRightDoubleClick():
    def demo_Right_Double(self):
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        print(driver.title)
        time.sleep(3.00)
        #Right Click
        achains=ActionChains(driver)
        rightclick=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        achains.context_click(rightclick).perform()
        time.sleep(3.00)
        element1=driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
        element1.click()
        time.sleep(3.00)
        driver.switch_to.alert.accept()
        time.sleep(3.00)
        #Double Click
        element2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(element2).perform()
        time.sleep(3.00)
        driver.switch_to.alert.accept()
        time.sleep(3.00)
click = DemoRightDoubleClick()
click.demo_Right_Double()


