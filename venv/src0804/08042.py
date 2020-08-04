# 1、演示 固定等待 and 智能等待
# 2、演示 打印标题
# 3、演示 打印url
# 4、演示 浏览器操作：浏览器最大化 /最小化 / 设置浏览器的宽和高 /浏览器的前进和后退
#                    控制浏览器的滚动条

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 4、演示 浏览器操作：浏览器最大化 /最小化 / 设置浏览器的宽和高 /浏览器的前进和后退
#                    控制浏览器的滚动条

#time.sleep(5)
#driver.maximize_window()            浏览器最大化
#time.sleep(5)
#driver.minimize_window()            浏览器最小化
#time.sleep(3)
#driver.set_window_size(400,800)     设置浏览器的宽和高
driver.find_element_by_id("kw").send_keys("罗志祥")
driver.find_element_by_id("su").click()
driver.maximize_window()
time.sleep(3)
#浏览器的后退
#driver.back()                        # 浏览器的后退
#time.sleep(5)
#浏览器的前进
#driver.forward()                     # 浏览器的前进

#浏览器的滚动条拖到最低端（这个操作）  # 控制浏览器的滚动条
# 需要通过js代码去操作
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js) # 执行js代码
time.sleep(6)

#浏览器的滚动条拖到最顶端
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(6)

js="var q=document.documentElement.scrollRight=10000"
driver.execute_script(js)


# 1、演示 固定等待 and 智能等待
#driver.find_element_by_id("kw").send_keys("黄子韬")
#driver.find_element_by_id("su").submit()
#time.sleep(10) 固定等待 10秒
#driver.implicitly_wait(10) #智能等待 10秒
#driver.find_element_by_link_text("黄子韬_百度百科").click()

# 2、演示 打印标题
#title=driver.title
#print(title)

# 3、演示 打印url
#url=driver.current_url
#print(url)

time.sleep(5)
driver.quit()