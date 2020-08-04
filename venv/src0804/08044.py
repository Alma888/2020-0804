# 鼠标事件
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("乃万")
su1=driver.find_element_by_id("su")
time.sleep(3)
#实现 右击 su1（context_click()）
ActionChains(driver).context_click(su1).perform()
time.sleep(3)
#实现 双击 su1（double_click()）
ActionChains(driver).double_click(su1).perform()
time.sleep(6)
#实现 拖动（drag_and_drop()）
title=driver.find_element_by_id("su")
target=driver.find_element_by_link_text("乃万_百度百科")
#ActionChains(driver).drag_and_drop(title,target).perform()

#实现 移动（move_to_element()）
ActionChains(driver).move_to_element(target).perform()
time.sleep(6)

driver.quit()
