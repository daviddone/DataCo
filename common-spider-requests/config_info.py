import configparser
import pymysql
from elasticsearch import Elasticsearch

conn = None
cur = None 
mysql_enable = ""
es_enable = ""
def init():
    config = configparser.ConfigParser()
    config.read("info.ini",encoding="utf-8")  #中文注释报错
    global es_enable,es_enable,conn,cur,mysql_enable
    
    mysql_enable = config.get("MYSQL","enable")
    es_enable = config.get("ES","enable")
    host = config.get("MYSQL","host")
    port = config.get("MYSQL","port")
    user = config.get("MYSQL","user")
    passwd = config.get("MYSQL","passwd")
    db = config.get("MYSQL","db")
    charset = config.get("MYSQL","charset")
    es_host = config.get("ES","host")

    if mysql_enable == "1":
        conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=db,charset=charset)
        cur = conn.cursor()
        print("config_info init mysql_enable: 1")
    if es_enable == "1":
        print("es_host%s"%es_host)
        es = Elasticsearch("localhost")
        print(" config_info init es_enable: is 1")    