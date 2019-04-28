#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/4/3 9:07

备注：

"""
import socket
import urllib.request
import urllib.error

try:
    response=urllib.request.urlopen('http://google.com',timeout=1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('time out')
