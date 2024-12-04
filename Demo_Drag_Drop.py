import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
class DemoDragDrop():
    def demo_Drag_Drop(self):
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        print(driver.title)
        time.sleep(3.00)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        elm1=driver.find_element(By.ID,"draggable")
        elm2 = driver.find_element(By.ID, "droppable")
        #ActionChains(driver).drag_and_drop(elm1,elm2).perform()
        achains=ActionChains(driver)
        achains.drag_and_drop(elm1,elm2).perform()
        time.sleep(3.00)
        achains.drag_and_drop_by_offset(elm1,50,50).perform()
        time.sleep(3.00)
dd = DemoDragDrop()
dd.demo_Drag_Drop()


