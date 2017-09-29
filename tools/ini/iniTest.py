# coding=utf-8
import configparser
config = configparser.ConfigParser()
config.read("info.ini",encoding="utf-8")  #中文注释报错
mysql_enable = config.get("MYSQL","enable")
print("mysql_enable: %s" %mysql_enable)