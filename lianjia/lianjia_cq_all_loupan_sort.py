import requests
import sys
import io
from bs4 import BeautifulSoup
import json
import datetime
import operator
class pageObj:  
    key = ''  
    value = 0  

    def __init__(self,key,value):  
        self.key = key  
        self.value= value  

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
page_get_url = 'http://cq.fang.lianjia.com/loupan/'  
reqheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',"Cookie":"lianjia_uuid=16e5fa67-0cc6-4d9b-a821-4546d54684fb; gr_user_id=6899da72-4b10-4f24-9c57-63791572453d; select_city=500000; UM_distinctid=15afa330e4314f-0bbc587b4-4349052c-100200-15afa330e44b5; all-lj=59dc31ee6d382c2bb143f566d268070e; _jzqx=1.1490330278.1490330278.1.jzqsr=captcha%2Elianjia%2Ecom|jzqct=/.-; _jzqckmp=1; logger_session=96ffc0a93c5b375070990ff6c5b7f5ee; _gat=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _smt_uid=57d36f2e.32908cb9; CNZZDATA1255849584=1304221696-1487158954-null%7C1490328318; _qzja=1.591464727.1490330276905.1490330276905.1490330276906.1490330657042.1490330660925.0.0.0.8.1; _qzjb=1.1490330276905.8.0.0.0; _qzjc=1; _qzjto=8.1.0; _jzqa=1.2340256972601522700.1490330278.1490330278.1490330278.1; _jzqc=1; CNZZDATA1254525948=1730503106-1487158336-null%7C1490328280; CNZZDATA1255633284=602302624-1487157298-null%7C1490327260; CNZZDATA1255604082=439266703-1487159435-null%7C1490330398; _jzqb=1.8.10.1490330278.1; _ga=GA1.2.716929921.1473474351; lianjia_ssid=7b4a0522-4774-4054-8382-8754516e0cd4"}
r_page = requests.get(page_get_url,headers=reqheaders)
# print(r_page.content)
page_soup = BeautifulSoup(r_page.content,"html.parser")
page_no_text = page_soup.select('div.page-box.house-lst-page-box')[0].get("page-data")
print("####"+page_no_text)
page_no = json.loads(page_no_text).get("totalPage")
print("####"+str(page_no))
create_time = datetime.datetime.now().strftime('%Y-%m-%d')
index = 0
file = open("重庆新房楼盘排序"+create_time+".txt","w",encoding= 'utf-8')
avg_price_list = []
all_price_list = []
for page_no in range(1,(page_no+1)):
	site_url ='http://cq.fang.lianjia.com/loupan/pg'+str(page_no)
	r = requests.get(site_url,headers=reqheaders)
	lianjia_txt = r.content.decode('utf-8')
	print(lianjia_txt)
	soup = BeautifulSoup(r.content,"html.parser")
	house_list = soup.select("div.con-box div.list-wrap ul.house-lst li")
	print(str(page_no)+"###")	
	for item in house_list:
		# print(str(item))
		try:
			house_name = item.select(".info-panel h2 a")[0].get_text()
			house_price = item.select(".info-panel div.col-2 div.price div.average span.num")[0].get_text().strip()
			house_style = item.select(".info-panel div.area ")[0].get_text().strip().replace(" ","").replace("-","")
			house_address = item.select(".info-panel div.where span.region")[0].get_text().strip()
			if int(house_price)<4000:
				house_price_str="总价"+house_price+"万元"
				info =str(house_name)+","+str(house_price_str)+","+str(house_style)+","+house_address
				all_price_list.append(pageObj(info,int(house_price)))
			else:
				house_price_str="均价"+house_price+"元"	
				info =str(house_name)+","+str(house_price_str)+","+str(house_style)+","+house_address
				avg_price_list.append(pageObj(info,int(house_price)))
			print(str(house_name)+","+str(house_price)+","+str(house_style)+","+house_address)
		except Exception:
			print("此条数据不完整，请查阅数据源")
cmpfun = operator.attrgetter('value') 
avg_price_list.sort(key = cmpfun) 
all_price_list.sort(key = cmpfun)
for item in avg_price_list:
	index = index+1
	file.writelines(str(index)+item.key+"\n" +"\n")
for item in all_price_list:
	index = index+1
	file.writelines(str(index)+item.key+"\n" +"\n")
print(index)
file.close()	 


