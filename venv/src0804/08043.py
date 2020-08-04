#键盘事件

#键盘按键用法（TAB 键 和 ENTER键的使用）——————————————————————————————————————————————————————
#from selenium import webdriver
#import time
#from selenium.webdriver.common.keys import Keys #需要引入keys 包

#登录老师的禅道
#driver=webdriver.Chrome()
#driver.get("https://127.0.0.1:88/biz/user-login.html")
#driver.implicitly_wait(10)
#driver.find_element_by_id("account").send_keys("admin")
#driver.find_element_by_id("account").send_keys(Keys.TAB)
#time.sleep(3)
#driver.find_element_by_name("password").send_keys("huiwen890830")
#time.sleep(6)
#driver.find_element_by_name("password").send_keys(Keys.ENTER)
#time.sleep(6)
#driver.quit()

#组合键的使用（复制粘贴键的使用）——————————————————————————————————————————————————————
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #需要引入keys 包

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("端午节")
driver.find_element_by_id("su").click()
driver.implicitly_wait(10)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(5)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(5)

driver.find_element_by_id("kw").send_keys("龙舟")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.quit()
