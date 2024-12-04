import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
class DemoJSALERT():
    def demo_java_script_alert(self):
        driver.get("https://demo.automationtesting.in/Alerts.html")
        driver.maximize_window()
        print(driver.title)
        time.sleep(3.00)
        driver.find_element(By.XPATH, "//a[normalize-space()='Alert with OK & Cancel']").click()
        time.sleep(3.00)
        #Accept Alert
        driver.find_element(By.XPATH,"//button[normalize-space()='click the button to display a confirm box']").click()
        time.sleep(3.00)
        driver.switch_to.alert.accept()
        time.sleep(3.00)
        #Cancel alert
        driver.find_element(By.XPATH, "//button[normalize-space()='click the button to display a confirm box']").click()
        time.sleep(3.00)
        driver.switch_to.alert.dismiss()
        time.sleep(3.00)
        #Text alert
        driver.find_element(By.XPATH, "//a[normalize-space()='Alert with Textbox']").click()
        time.sleep(3.00)
        driver.find_element(By.XPATH, "//button[normalize-space()='click the button to demonstrate the prompt box']").click()
        time.sleep(3.00)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Afrin")
        time.sleep(3.00)
        driver.switch_to.alert.accept()
        time.sleep(3.00)
demojsalert=DemoJSALERT()
demojsalert.demo_java_script_alert()