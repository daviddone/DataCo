#coding=utf-8
import requests
import json
# 自定义菜单 access_token需调用接口获取
access_token = "mFkOVsLuGc0Wg808S-jsxg-CM4nJoFvyMm5iacxdK05gdmhoXjRSQJogp5jqu7inC88DQKI9PecCGb_JsQvaTqpZkGguBJI1FBUs02iz40CCy21piH_wDP9GGqrCVnOlRXWdAEAZFE"
body = {
     "button":[
     {
          "type":"view",
          "name":"菜单测试",
          "url":"http://nc17545142.iok.la/money/"
      }]
 }
url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token="+access_token
data = json.dumps(body,ensure_ascii=False).encode('utf-8')
r = requests.post(url, data)
print(r.content)