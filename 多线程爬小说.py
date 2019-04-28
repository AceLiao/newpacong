#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/3/19 11:25

备注：

"""
import requests
import threading
import re
import time
import os
import sys
from bs4 import BeautifulSoup

req_header={
"Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection':'keep-aliv',
'Cookie': 'Hm_lvt_169609146ffe5972484b0957bd1b46d6=1552971595; BAIDU_SSP_lcr=https://www.baidu.com/link?url=5wBTD7Zb7OKLzBZ8v30QdkgjVODgzye1GkGDSJ9jQlK&wd=&eqid=a1784d9b00084ce6000000055c90774d; UM_distinctid=169945286103ac-0c20f56972b268-5b193413-1fa400-1699452861119b; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1552971656; Hm_lvt_7c0f725475beb22058ccb8be51c96bf6=1552971657; Hm_lpvt_7c0f725475beb22058ccb8be51c96bf6=1552971657',
'Host': 'm.xbiquge.la',
'Referer': 'http://www.xbiquge.la/',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}