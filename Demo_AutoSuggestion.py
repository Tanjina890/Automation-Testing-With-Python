import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
class DemoAutoSuggestion():
    def demo_autosuggest_dropdown(self):
        driver.get("https://medium.com/explore-topics")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        search=driver.find_element(By.XPATH,"//input[@placeholder='Search all topics']")
        search.click()
        time.sleep(2.00)
        search.send_keys("Children")
        time.sleep(4.00)
        search.send_keys(Keys.ENTER)
        time.sleep(2.00)
        driver.close()

dauto=DemoAutoSuggestion()
dauto.demo_autosuggest_dropdown()