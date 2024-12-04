import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
class DemoDropDown():
    def demo_Drop_Down(self):
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        dropdown=driver.find_element(By.NAME,"UserTitle")
        dd=Select(dropdown)
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)
        dd.select_by_value("CxO_General_Manager_ANZ")
        time.sleep(3)
Dropdown=DemoDropDown()
Dropdown.demo_Drop_Down()