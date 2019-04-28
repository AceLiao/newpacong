#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/4/10 14:12

备注：

"""
import re
content='Hello 123 4567 World_this is a Regex Demo'
print(len(content))

# match() 来匹配
result=re.match("^Hello\s\d\d\d\s\d{4}\s\w{10}",content)

print(result.group())
print(len(result.group()))
print(result.span())
result2=re.match("^Hello\s(\d+)\s(\d+)",content)
print(result2.group(1))
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''
result_html=re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
if result_html:
    print(result_html.group(1),result_html.group(2))

content2='12abc12344ferg2g4k'
content2=re.sub('\d+',"",content2)
print(content2)
html=re.sub('<a.*?>|</a>',"",html)
print(html)