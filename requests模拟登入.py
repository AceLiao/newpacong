#encoding:utf-8
"""
@project=爬虫
@author=jianya_liao
@creat_time=2019/4/9 13:24

备注：

"""
import requests
headers={
'cookie':'_zap=dc0aa673-d72d-40ac-8a26-4159c0114d50; q_c1=2bafe0d211ff46c68baa7c05790a7dae|1507612896000|1503041076000; d_c0="ABACG4ZgqgyPTmkmk1-lw1G5USKYRvihySo=|1510372240"; __DAYU_PP=vV2zBYvBbNUQqb6aa7IAffffffff8662ee23404f; _ga=GA1.2.153330584.1510372225; _xsrf=eBUy4j8fShD4DRLtF58rRgQg9IkEqKx2; __utmz=51854390.1539048667.3.3.utmcsr=so.com|utmccn=(organic)|utmcmd=organic|utmctr=skit%20learn; __utmv=51854390.000--|2=registration_date=20171111=1^3=entry_date=20170818=1; l_n_c=1; q_c1=2bafe0d211ff46c68baa7c05790a7dae|1554700095000|1503041076000; n_c=1; __utma=51854390.153330584.1510372225.1539048667.1554700099.4; __utmc=51854390; __gads=ID=8bcbca861f77985d:T=1554700129:S=ALNI_MZT9rT9b6qFL1c2A6zepQJrxgSO1A; l_cap_id="NTYwMzRiM2E1NDBlNGI0MjljMDRjN2I1YzdiMzc2ZTI=|1554701065|1af5118c98e89f0184216396418dc520f3c07f60"; r_cap_id="Mzc2NDA4MDcxZWVmNDAzYWI3YTMzMzU4ZDU3ZTg1MDk=|1554701065|fd6f5753e15ac54b59ee73606c07f69faeb3ce15"; cap_id="ZGRhNDhiYjFkMTMyNGY2NWJhMGY5YWEwZDk0ODM0N2Y=|1554701065|a32977a5d965a290f6e259c20be36fc80a45f74f"; capsion_ticket="2|1:0|10:1554770632|14:capsion_ticket|44:ZDk2ZTBhZmU1MzU1NDQ2NmE1MGM3OWJlZDUxODRiN2E=|1f685976f77362dc6e8919f92a5561e6dc6dbdfbb0b91061fea6b2825225e9de"; z_c0="2|1:0|10:1554770644|4:z_c0|92:Mi4xMnBaOEJnQUFBQUFBRUFJYmhtQ3FEQ1lBQUFCZ0FsVk4xRGlaWFFCcTNtZ09KQVl6czRzZ0J6LV9lOTNGU2dwR1BR|45b75965483827feabea381278adb36f8e517e08c4261151040ed61a55ccba23"; tst=r; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# r=requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)

# 会话维持requests.Session()
# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

# SLL验证，使用verify参数
response=requests.get('https://www.12306.cn')
print(response.status_code)
print(response)