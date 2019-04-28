#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/3/18 16:27

备注：

"""
from bs4 import BeautifulSoup
import requests
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')
# print(soup.prettify())
print(soup.a)
print(soup.a.string)
print(soup.a['class'])
print(soup.a['href'])
print(soup.a.attrs)
print()
print(type(soup.head))
print(type(soup.title))
print(type(soup.a.string))
print(type(soup.p.string))
print(type(soup))
print()
print(soup.a.contents)
print(soup.head.contents)
print(soup.title.contents)
print("strings:*******************")

# for string in soup.stripped_strings:
#     print(string)

# print(soup.body.children) #返回的是一个列表序列
# for child in soup.head.children:
#     print(child)
# print("decendants:")
# for decendant in soup.head.descendants:
#     print(decendant)
# # print(soup.find_all('a'))

# response=requests.get("http://www.biqugew.com/book/13/")
# response.encoding='gb18030'
# # print(response.text)
# soup=BeautifulSoup(response.text,'lxml')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# for i in soup.body.children:
#     print(i)

#parents 父节点
content=soup.title.string
print("content:",content)
for parent in content.parents:
    print("父节点名字：",parent.name)

for i in soup.find_all(re.compile("^b")):
    print(i.name)