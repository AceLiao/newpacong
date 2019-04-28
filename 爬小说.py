#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/3/18 13:20

备注：

"""
import requests
from lxml import etree
# from pyquery import PyQuery as pq
# from bs4 import BeautifulSoup
# response =requests.get("http://www.biqugew.com/book/13/")
# response.encoding=('gb18030')
# # print(response.text)
# soup=BeautifulSoup(response.text,'lxml')
# # print(soup.select('a[href]'))
# for item in soup.find_all('a'):
#     if "/book/13" in str(item.get('href')):
#         url="http://www.biqugew.com"+str(item.get('href'))
#         doc=requests.get(url=url)
#         doc.decoding='gb18030'
#         s=BeautifulSoup(doc.text,'lxml')
#         print(s.find_all('h1'))
#         print(s.find_all("div",attrs={"id":'content'}))
#         # print(s.find('br'))
#         # for i in s.find_all('dd'):
#         #     print(i.text)
url = "http://www.biquw.com/book/700/"
#获取各章节的link
def get_urls(url):
    resp = requests.get(url)
    resp.encoding=resp.apparent_encoding
    html = resp.text
    text = etree.HTML(html)
    links = text.xpath('//li/a/@href')
    for i in range(len(links)):
        links[i]=url+links[i]
    return links

def get_articles(links):
    for link in links[0]:
        article = requests.get(link)
        article.encoding = article.apparent_encoding
        html = article.text
        text =etree.HTML(html)
        words = text.xpath('//div[@id="htmlContent"]')
        print(words[0])

if __name__ == '__main__':
    links = get_urls(url)
    get_articles(links)