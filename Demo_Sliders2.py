import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
class DemoSliders():
    def demo_Sliders(self):
        driver.get("https://www.snapdeal.com/products/mens-footwear-sports-shoes?sort=plrty&q=Price%3A301%2C11975%7C")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        ele1 = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        ele2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")
        ActionChains(driver).move_to_element(ele1).pause(1).click_and_hold(ele1).move_by_offset(40,0).release().perform()
        ActionChains(driver).move_to_element(ele2).pause(1).click_and_hold(ele2).move_by_offset(-40,0).release().perform()
        time.sleep(4.00)
sliders = DemoSliders()
sliders.demo_Sliders()


