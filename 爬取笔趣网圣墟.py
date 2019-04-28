#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/3/21 14:42

备注：

"""
from bs4 import BeautifulSoup
import requests
response =requests.get("http://www.xbiquge.la/13/13959/")
response.encoding=('utf-8')
# print(response.text)
soup=BeautifulSoup(response.text,'lxml')
##list > dl > dd:nth-child(1) > a
links=soup.select('#list > dl > dd > a ')
# for link in links:
#     print(link['href'])

lk="http://xbiquge.la/"
res=requests.get(lk+links[0]['href'])
res.encoding="utf-8"
print(res.select('a'))