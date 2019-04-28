#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/4/15 13:56

备注：

"""
import requests
import re

def get_one_page(url):
    response=requests.get(url)
    if response.status_code==200:
        return response.text
    return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src=".*?".*?name.*?title="(.*?)".*?star.*?>(.*?)</p>',re.S)
    print(re.findall(pattern,html))
def main():
    url='http://maoyan.com/board/4'
    html=get_one_page(url)
    parse_one_page(html)
    # print(html)

main()