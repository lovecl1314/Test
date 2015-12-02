# -*- encoding: utf-8 -*-
__author__ = 'cyclu'
__Created__ = '2015.10.16'
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://www.baidu.com'

#谷歌浏览器
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# driver.find_element_by_name('wd').send_keys(u'厦门国贸集团股份有限公司') #u'厦门国贸集团股份有限公司'

# 写法1 根据表单元素提交
driver.find_element_by_name('wd').submit()

# 写法2 （调用Keys敲回车）
# elem = driver.find_element_by_name('wd')
# elem.send_keys(Keys.RETURN)
# elem = driver.find_element_by_name('wd')
# elem.send_keys(u'厦门国贸集团股份有限公司',Keys.RETURN)  #Keys.ARROW_DOWN
# # copy content of A
# dr.find_element_by_id('A').send_keys((Keys.CONTROL, 'a'))
# dr.find_element_by_id('A').send_keys((Keys.CONTROL, 'x'))
# sleep(1)
# paste to B
# dr.find_element_by_id('B').send_keys((Keys.CONTROL, 'v'))
# sleep(1)

# 写法3 点击搜索按钮
driver.find_element_by_id("su").click()


print(driver.title)
time.sleep(3)
# driver.quit()

# time.sleep(3)
# print(u"刚才访问的网站是 {0},网站标题是： {1}".format(url.decode('utf-8'),driver.title) )
# search = '厦门国贸集团股份有限公司'
# search2 = search.decode('utf-8')
# time.sleep(3)
# driver.quit()
