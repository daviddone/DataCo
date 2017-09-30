#encoding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import site_info
import datetime
import uuid
import config_info

# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')



def isUTF8(html):
	encode_list = requests.utils.get_encodings_from_content(html.text)
	isUTF8 = True
	if len(encode_list) > 0 and encode_list[0].lower() != "utf-8":
			encode = encode_list[0]
			print(encode)
			isUTF8 = False
			return isUTF8
def save_infos(conn,cur,detail_href,text):
	sql = "SELECT `id` FROM `info` WHERE `detail_href`=%s"
	cur.execute(sql, (detail_href,))
	result = cur.fetchone()
	if result is None:
		# print("可以插入数据")
		#插入mysql
		create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		sql = "INSERT INTO info (id, news_title,detail_href,content,create_time,field) VALUES (%s, %s,%s,%s,%s,%s)"
		cur.execute(sql,(str(uuid.uuid1()),text,detail_href,"content",create_time,""))
		conn.commit()
		#插入es
		doc = {
			'title': str(text),
			'desc': str(text),
			'detail_href':detail_href,
			'dateTime':create_time,
			}
		res = es.index(index="cq", doc_type='info', body=doc)

def get_infos(conn,cur,item):
	site_url = item.site_url
	site_rule = item.site_rule
	site_home = item.site_home
	site_name = item.site_name
	html = requests.get(site_url)
	content = html.content
	if isUTF8(html) is False:
		content = html.content.decode("gb2312","ignore")
	# print(html.content)
	soup = BeautifulSoup(content, "html.parser")
	print("asdf")
	print(site_rule)
	info_list = soup.select(site_rule)
	f_name = "%s.txt"%site_name
	print("文件名称:%s"%f_name)
	f = open(f_name,"w",encoding="utf-8")
	for item in info_list:
		detail_href ="null"
		try:
			detail_href = item.get("href").strip()
		except Exception as e:
			print("无链接")
		text = item.text.strip()
		if detail_href.find("http") == -1 and detail_href != "null":
			detail_href = site_home + "/" +detail_href
		f.writelines("href %s    text %s  \n"%(detail_href,text))
		# print("href %s text %s"%(detail_href,text))
		#save_infos(conn,cur,detail_href,text)
	f.close()

start_time = time.time()
site_lists = site_info.get_sites()
config_info.init() # 初始化配置文件
conn = config_info.conn
cur = config_info.cur
mysql_enable = config_info.mysql_enable
es_enable = config_info.es_enable

print("init es_enable:"+es_enable)
print("init mysql_enable:"+mysql_enable)

for item in site_lists:
	print(item.site_url+item.site_rule)
	try:
		get_infos(conn,cur,item)
		# get_infos("http://www.cq.gov.cn/public-wcms-webapp/content/Content!findContentList.action?wcmsSiteTreeSid=5&pageSize=1000","div.list a")
	except Exception as e:
		print("bad url:" + item.site_url+ str(e))
if mysql_enable == "1":
	cur.close()
	conn.close()
# print("代码执行时间："+str(time.time()-start_time) +"s")

