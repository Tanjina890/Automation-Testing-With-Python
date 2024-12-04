import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
class DemoSliders():
    def demo_Sliders(self):
        driver.get("https://www.globalsqa.com/demo-site/sliders/#Range")
        driver.maximize_window()
        print(driver.title)
        time.sleep(2.00)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']"))
        ele1=driver.find_element(By.XPATH,"//span[1]")
        ele2 = driver.find_element(By.XPATH, "//span[2]")
        ActionChains(driver).drag_and_drop_by_offset(ele1,20,0).perform()
        time.sleep(3.00)
        ActionChains(driver).drag_and_drop_by_offset(ele2, -40, 0).perform()
        time.sleep(3.00)
        #Another way
        #ActionChains(driver).click_and_hold(ele2).pause(2).move_by_offset(-40,0).perform()
        #time.sleep(3.00)
        driver.close()

sliders = DemoSliders()
sliders.demo_Sliders()


