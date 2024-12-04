import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
class DemoMultiListDropDown():
    def demo_multi_items(self):
        driver.get("https://demoqa.com/select-menu")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        dd_demo=driver.find_element(By.NAME,"cars")
        dd_multi=Select(dd_demo)
        dd_multi.select_by_index(0)
        dd_multi.select_by_visible_text("Opel")
        dd_multi.select_by_value("audi")
        time.sleep(4.00)
        dd_multi.deselect_by_index(0)
        dd_multi.deselect_by_value("audi")
        dd_multi.select_by_visible_text("Opel")
        time.sleep(4.00)
        dd_multi.select_by_visible_text("Saab")
        time.sleep(4.00)
        dd_multi.deselect_all()
        time.sleep(4.00)

dropdown= DemoMultiListDropDown()
dropdown.demo_multi_items()