import requests
import sys
import io
from bs4 import BeautifulSoup
import json
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
page_get_url = 'http://www.ufoer.com/'
reqheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
r_page = requests.get(page_get_url,headers=reqheaders)
page_soup = BeautifulSoup(r_page.content,"html.parser")
page_no_text = page_soup.select('li.ng-scope')[-2].select("a")[0].get_text()
print("####"+str(page_no_text))
page_no = int(page_no_text)
create_time = datetime.datetime.now().strftime('%Y-%m-%d')
file = open("王通营销列表"+create_time+".txt","w",encoding= 'utf-8')
file_detail = open("王通营销详情"+create_time+".txt","w",encoding= 'utf-8')
index = 1 
for page_no in range(1,(page_no+1)):
	site_url ='http://www.ufoer.com/page/'+str(page_no)
	r = requests.get(site_url,headers=reqheaders)
	soup = BeautifulSoup(r.content,"html.parser")
	info_list = soup.select("article.excerpt.ias_excerpt")
	print(len(info_list))
	for item in info_list:
		info_title = item.select("div.desc a.title.info_flow_news_title")[0].get_text()
		info_detail_href = item.select("div.desc a")[0].get("href")
		info_time = item.select("div.author time.timeago")[0].get_text()
		file.writelines(index + "," +info_title+ "," +info_time+"\n" +"\n")
		print(title)
		r_detail = requests.get(info_detail_href,headers=reqheaders)
		soup_detail = BeautifulSoup(r_detail.content,"html.parser")
		try:
			detail_txt = soup_detail.select("section.article")[0].get_text()
		except Exception:
			print(str(info_detail_href)+"此条数据不完整")
		file_detail.writelines(index + "," +info_title+ "," +info_time+","+info_detail_href+","+detail_txt+"\n" +"\n")
		index = index+1
file.close()	 
file_detail.close()

