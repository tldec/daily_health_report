#_*_coding:utf-8_*_
# author    :tldec_(tanlongs4w@gmail.com)
# date      :2020/5/5 15:13
import requests
import time
import json
url = "https://wxxy.csu.edu.cn/ncov/wap/default/save"
# 将获取到的cookie替换'your_cookie'
cookie = "your_cookie"
headers={
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":cookie,
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Host": "wxxy.csu.edu.cn",
    "Origin": "https://wxxy.csu.edu.cn",
    "Referer": "https://wxxy.csu.edu.cn/ncov/wap/default/index",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1"
}
# 将表单数据中的 '&created=1588475919'和'&date=20200503'删掉后替换'your_post_data'
msg = 'your_post_data'
# 更新created 和 date为当前时间
created = (int)(time.time())
date = time.strftime("%Y%m%d",time.localtime(created))
msg = msg +'&date='+date+'&created='+(str)(created)
# post请求
r=requests.post(url,data=msg.encode('utf-8'),headers = headers)
# print(msg)
print('打卡结果:',json.loads(((bytes)(r.content)).decode('utf-8'))['m'])