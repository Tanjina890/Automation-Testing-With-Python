import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class DemoCheckBoxes():
    def demo_Check_Boxes(self):
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        driver.find_element(By.XPATH,"//input[@value='red']").click()
        time.sleep(2.00)
        driver.find_element(By.CSS_SELECTOR, "input[value='green']").click()
        time.sleep(2.00)
        var1=driver.find_element(By.XPATH, "//input[@value='red']").is_selected()
        print(var1)
        var2=driver.find_element(By.CSS_SELECTOR, "input[value='green']").is_selected()
        print(var2)
        var3=driver.find_element(By.XPATH,"//input[@value='yellow']").is_selected()
        print(var3)
        var4 = driver.find_element(By.XPATH, "//input[@value='blue']").is_selected()
        print(var4)
        var5= driver.find_element(By.XPATH, "//input[@value='orange']").is_selected()
        print(var5)
        var6 = driver.find_element(By.XPATH, "//input[@value='purple']").is_selected()
        print(var6)
        time.sleep(4.00)

checkboxes=DemoCheckBoxes()
checkboxes.demo_Check_Boxes()