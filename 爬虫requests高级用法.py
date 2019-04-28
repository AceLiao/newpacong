#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/4/8 14:54

备注：

"""
#上传文件
import requests
files={"file":open('favicon.ico','rb')}
r=requests.post("http://httpbin.org/post", files=files)
print(r.text)
#cookies
rr=requests.get("https://www.baidu.com")
print(rr.cookies)
for key,value in rr.cookies.items():
    print(key,"=",value)