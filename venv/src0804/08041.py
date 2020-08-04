#元素定位 +  操作测试对象
#1. 通过id定位
#2. 通过name定位（实践发现，不是每个元素都有name）
#3. 通过class name定位（class在当前页面必须是唯一的，才能定位到唯一的元素，若一个元素有多个class则没有办法成功定位）
#4. 通过link text定位（通过链接内容去定位元素）
#5. 通过partial link text定位(通过部分链接内容去定位元素)
#6. 通过tag name 定位（通过标签名去定位，比如imput标签或div,但又因为一个页面内input属性有太多个，所以不能定位到具体想要的元素）
#7. 通过Xpath定位(可以成功定位)
#8. 通过css selector定位
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)
#通过name定位
#driver.find_element_by_name("wd").send_keys("520")

#通过id定位
#driver.find_element_by_id("su").click()

#通过link text定位
#driver.find_element_by_link_text("高考加油").click()

#通过partial link text定位
#driver.find_element_by_partial_link_text("高考").click()

#通过tag name 定位（通过标签名去定位，比如imput标签或div,但又因为一个页面内input属性有太多个，所以不能定位到具体想要的元素）
#driver.find_element_by_tag_name("input").send_keys("521") 定位失败

#通过Xpath定位
#driver.find_element_by_xpath("//*[@id='kw']").send_keys("521")
#driver.find_element_by_xpath("//*[@id='su']").click()

#通过css selector定位
#driver.find_element_by_css_selector("#kw").send_keys("黄子韬")
#或者是driver.find_element_by_css_selector(".s_ipt").send_keys("黄子韬")
#driver.find_element_by_xpath("//*[@id='su']").click()
#time.sleep(8)
#通过clear可以实现清除操作
#driver.find_element_by_css_selector("#kw").clear()
##time.sleep(8)
#driver.find_element_by_id("kw").send_keys("肖战")
# submit:把“百度一下”的操作从click 换成submit 可以达到相同的效果
#driver.find_element_by_id("su").submit()

time.sleep(8)
#text用于获取元素的文本问题
t=driver.find_element_by_id("s-top-left").text
print(t)
driver.quit()