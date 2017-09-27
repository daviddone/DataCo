import re
import time
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 15)
index = 1

def get_index():
	try:
		print('进入主页')
		browser.get('https://www.lagou.com/')
		close_window = wait.until(
				EC.element_to_be_clickable((By.CSS_SELECTOR, '#cboxClose'))
			)
		close_window.click()
		time.sleep(2)
		search_place = wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '#search_input'))
			)
		search_button = wait.until(
				EC.element_to_be_clickable((By.CSS_SELECTOR, '#search_button'))
			)
		time.sleep(2)
		search_place.clear() # 清除hint
		WORK = "大数据开发"
		search_place.send_keys(WORK)
		time.sleep(2)
		search_button.click()
	except TimeoutException as e:
		print('连接超时！')
		login()

def get_datas():
	f = open("大数据开发.txt","w",encoding="utf-8")
	for css_num in range(3, 11):
		css_place = '#filterCollapse > li:nth-child(4) > a:nth-child({})'.format(css_num)
		time.sleep(2)
		one_type = browser.find_element_by_css_selector(css_place)
		type_name = one_type.text
		one_type.click()
		all_page = browser.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[last()-1]').text
		print('正在获取', type_name, '第1页的信息')
		get_data(type_name,f)
		time.sleep(2)
		for p in range(2, int(all_page)+1):
			next_page = wait.until(
					EC.element_to_be_clickable((By.XPATH, '//*[@id="s_position_list"]/div[2]/div/span[last()]'))
				)
			next_page.click()
			print('正在获取', type_name, '第{}页的信息'.format(str(p)))
			get_data(type_name,f)
			time.sleep(2)
		browser.refresh()
		time.sleep(2)
		one_type = browser.find_element_by_css_selector(css_place)
		one_type.click()
	f.close()

def get_data(type_name,f):
	global index
	html = browser.page_source
	doc = pq(html)
	items = doc('#s_position_list .item_con_list .con_list_item').items()
	for item in items:
		url = item.find('.p_top .position_link').attr('href')
		all_title = item.find('.p_top').text()
		title = re.findall(r'(.*) \[', all_title)[0]
		address = re.findall(r'.*?\[ (.*) \]', all_title)[0]
		all_tag = item.find('.li_b_l').text().replace('/ ', '').split(' ')
		salary = all_tag[0]
		experience = all_tag[1]
		education = all_tag[2]
		tags = [tag for tag in all_tag[3:]]
		company = item.find('.company_name').text()
		fuli = item.find('.li_b_r').text()
		data = {
			'title': title,
			'url': url,
			'company': company,
			'address': address,
			'salary': salary,
			'experience': experience,
			'education': education,
			#'tags': tags,
			'type': type_name,
			'fuli': fuli,
		}
		reqheaders = {
				"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
				"Accept-Encoding":"gzip, deflate, sdch, br",
				"Accept-Language":"zh-CN,zh;q=0.8",
				"Cache-Control":"max-age=0",
				"Connection":"keep-alive",
				"Host":"www.lagou.com",
				"Upgrade-Insecure-Requests":"1",
				"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
				}
		detail_r = requests.get(url,headers=reqheaders)
		print(url)
		soup = BeautifulSoup(detail_r.content,"html.parser")
		# browser.get(url)
		# detail_html = browser.page_source
		# soup = BeautifulSoup(detail_html,"html.parser")
		try:
			a = soup.select('dd.job_bt')[0]
			#print(str(a.get_text()))
			f.writelines(str(index)+','+company+','+salary+","+address+"###\n"+url+"\n"+str(a.get_text())+"\n")
		except Exception as e:
			f.writelines(str(index)+','+company+','+salary+","+address+"###\n"+url+"\n"+"\n")
			print("详情获取失败")
		# f.write(url+'##'+company+'##'+salary+"\n")
		index = index+1
		print('插入成功')

def main():
	start_time = time.time()
	get_index()
	get_datas()
	browser.close()
	print('爬取完毕')
	print(time.time()-start_time)
if __name__ == '__main__':
	main()