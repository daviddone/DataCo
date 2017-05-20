import requests
import sys
import io
from bs4 import BeautifulSoup
import json
import time
import threading
import datetime

index = 1
lock = threading.Lock()
def get_data(pn):
	global index
	print(pn)
	site_url ='https://www.lagou.com/jobs/positionAjax.json?px=default&yx=10k-25k&city=北京&needAddtionalResult=false'
	reqheaders = {'Host':'www.lagou.com','Referer':'https://www.lagou.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1','Cookie':'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1483778453; _ga=GA1.2.749536111.1467962246; user_trace_token=20160708151800-1a36b115-44dc-11e6-a49e-5254005c3644; LGUID=20160708151800-1a36b57a-44dc-11e6-a49e-5254005c3644; JSESSIONID=44A08BFEEAE6D0BEEC6C0CC9882AC208; SEARCH_ID=dfdd6e3d352c400695d9f94caa3051b6; LGSID=20170107164041-f8d8fefe-d4b4-11e6-9bab-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Android%3Fgj%3D3%25E5%25B9%25B4%25E5%258F%258A%25E4%25BB%25A5%25E4%25B8%258B%26px%3Ddefault%26yx%3D10k-15k%26city%3D%25E5%258C%2597%25E4%25BA%25AC; LGRID=20170107170335-2b907f10-d4b8-11e6-9bad-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1483779826; index_location_city=%E5%8C%97%E4%BA%AC; _gat=1; TG-TRACK-CODE=index_search'}
	infos = {'first':'false','pn':pn,'kd':'大数据开发'}  # 传递参数
	r = requests.post(site_url,data=infos,headers=reqheaders)
	lagou_txt = r.content.decode('utf-8')
	print(lagou_txt)
	lagou_json = json.loads(lagou_txt)
	job_list = lagou_json['content']['positionResult']['result']
	
	for item in job_list:
		print(item['companyFullName']+str(index) +','+item['salary']+str(item['positionId']))
		lock.acquire()
		try:
			title = str(index) +','+item['companyFullName']+','+item['salary']
			job_detail = 'https://www.lagou.com/jobs/'+str(item['positionId'])+".html"
			print(job_detail)
			detail_r = requests.get(job_detail)
			soup = BeautifulSoup(detail_r.content,"html.parser")
			a = soup.select('dd.job_bt')[0]
			print(str(a.get_text()))
			file.writelines(title+"###"+str(a.get_text()))
			index = index+1
		finally:
			lock.release()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
try:
	create_time = datetime.datetime.now().strftime('%Y-%m-%d')
	file = open("大数据开发10页"+create_time+".txt","w",encoding= 'utf-8')
	t = time.time()

	# th = threading.Thread(target=get_data,args=('1',),name="1")
	ths = []
	for item in range(1,10):
		th = threading.Thread(target=get_data,args=(str(item),),name=str(item))
		ths.append(th)
	for th in ths:
		th.start()
	for th in ths:
		th.join()
finally:
	file.close() 
print(time.time()-t)

# list = soup.select(".con_list_item") 
# for item in list:
# 	print(item)

