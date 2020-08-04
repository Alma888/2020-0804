# 定位一组元素
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("file:///D:/比特课件/测试课件/测试管理工具/selenium/selenium2html/checkbox.html")
driver.maximize_window()
inputs=driver.find_elements_by_tag_name("input")
time.sleep(6)
for input in inputs:
    if input.get_attribute('type')=="checkbox":
        input.click()
time.sleep(6)
driver.quit()