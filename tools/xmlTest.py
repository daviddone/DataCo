import xml.etree.ElementTree as ET
import json
str ="<xml><ToUserName><![CDATA[gh_4f7b30f975ab]]></ToUserName><FromUserName>1unsubscribe</FromUserName></xml>"
root = ET.fromstring(str)
fromUser = root.findtext(".//FromUserName")
print(fromUser)
print(fromUser.find("12unsubscribe") )
if (fromUser.find("subscribe") == 1 and fromUser.find("unsubscribe") == -1):
    print("subscribe")

json_str = r'{"openid":"ofyeiwg26bF5kVpskNy5B_WQcxPg","scope":"snsapi_base"}'
myjson = json.loads(json_str)
print(myjson["openid"])