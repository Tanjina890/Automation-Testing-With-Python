import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
class DemoCalenderSelect():
    def demo_calender(self):
        driver.get("https://demo.automationtesting.in/Datepicker.html")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        date_picker1=driver.find_element(By.XPATH,"//input[@id='datepicker1']")
        date_picker1.click()
        time.sleep(3.00)
        driver.find_element(By.XPATH,"//a[normalize-space()='27']").click()
        time.sleep(4.00)
        date_picker2 = driver.find_element(By.XPATH, "//input[@id='datepicker2']")
        date_picker2.click()
        time.sleep(3.00)
        driver.find_element(By.XPATH, "//a[@title='Select Saturday, Nov 30, 2024']").click()
        time.sleep(4.00)
        all_dates=driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']")

calender=DemoCalenderSelect()
calender.demo_calender()