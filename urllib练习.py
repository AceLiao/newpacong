#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/4/2 15:50

备注：

"""
import urllib.request
response=urllib.request.urlopen('https://cuiqingcai.com/5500.html')
# print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheader("Link"))
print('test')