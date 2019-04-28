#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/4/8 13:18

备注：

"""
import requests
import re

#  抓取知乎 最热话题
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r=requests.get("https://www.zhihu.com/explore",headers=headers)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
title=re.findall(pattern,r.text)
for item in title:
    print(item,end='')

# 有些网站没有headers，不会报错，但是爬取不到数据
# rr=requests.get("https://www.zhihu.com/explore")
# print(rr.text)

# 抓取二进制数据
r = requests.get("https://github.com/favicon.ico")
# print(r.text)
# print(r.content)

# 保存图片,图片不太清晰，是什么原因？
# with open('favicon.jpg','wb') as f:
#     f.write(r.content)

#post()请求
data={'name':'germy','age':22}
r=requests.post("http://httpbin.org/post",data=data)
print(r.text)