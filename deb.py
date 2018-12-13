#coding=utf-8

import time
from selenium import  webdriver

# url='D:\chrome\ChromePortable\ChromePortable.exe'
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)


driver.get('https://www.baidu.com')
# 输入账号
driver.find_element_by_name("wd").send_keys("youruser")
# 输入密码
driver.find_element_by_id("su").click()
print('百度搜索完成')
driver.quit()