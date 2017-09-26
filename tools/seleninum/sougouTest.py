from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("http://weixin.sogou.com/")
print("visiting")
browser.find_element_by_css_selector('#query').send_keys("中国日报双语新闻")
browser.find_element_by_css_selector(".swz").click()
item_list = browser.find_elements_by_css_selector('ul.news-list h3')

browser.find_element_by_css_selector(".swz2").click()
passage_list = browser.find_elements_by_css_selector('ul.news-list h3')

for item in item_list:
	print(item.text)
for item in passage_list:
	print(item.text)

	
