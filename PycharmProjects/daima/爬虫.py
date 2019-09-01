#python --爬虫 pip install requests
#  爬虫：spider，网络蜘蛛    根据自己制定的规则，模拟浏览器批量下载网络中的资源
# 聚焦爬虫：只针对某个网站进行的资源爬取
# 搜索爬虫：针对全网络进行的资源爬取  （百度搜索引擎）
#模拟浏览器的模块： requests urllib2  urllib3  httpclien
#筛选数据： re  bs4  xpath
# 1、有目的的获取网络中的资源    scrapy 爬虫框架
#2、代码请求URL
#    命名html文本，提取想要的数据
#    分类保存文件
#使用到的库requests  re

"""
import requests
import re

qwe={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}

#发送URL请求
#req=requests.get('https://www.fpzw.com/xiaoshuo/88/88413/17355844.html',headers=qwe)
req=requests.get('https://www.fpzw.com/xiaoshuo/88/88413',headers=qwe)
#接收html文本
res=req.content.decode('gbk')
# print(type(res))
print(res)
#s1=re.compile('<title>\s*(.*?)\s*</title>')
# a=re.findall(s1,res)
# print(a)

s3=re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
urs=re.findall(s3,res)  #列表
print(urs)
k={}
for i in urs:
    url=f'https://www.fpzw.com/xiaoshuo/88/88413/{i[0]}.html'
    mu=i[1]
    k[mu]=url
print(k)

req=requests.get(k['第一章 附体'],headers=qwe)
res=req.content.decode('gbk')
print(res)


#获取小说文本内容
# s1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p></div>')
# s2=re.compile('<h2>(.*?)</h2>')
# mulu=re.findall(s2,res)
# neirong =re.findall(s1,res)
# print(mulu)
# print(neirong)
"""

import requests
import re
import random

n=random.randint(0,36)

user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]

print(len(user_agent))
class ZOL(object):
    #请求url
    def get_url(self):
        res = requests.get('http://desk.zol.com.cn/bizhi/7590_94219_2.html', headers={"User_Agent":user_agent[n]})
        #获取html文本
        html=res.content.decode('gb2312')
        s = re.compile('<li class=".*">\s*<a href="/bizhi/7590(.*?)">')
        u = re.findall(s, html)
        j=[]
        for i in u:
            j.append('http://desk.zol.com.cn/showpic/1920x1200'+i)
        # print(i)
        return  j
    # 从html文本中找我们要的
    def get_big_img_url(self):
        a=self.get_url()    #none --html文本
        for i in a:
            res1=requests.get(i,headers={"User_Agent":user_agent[n]})
            # html=res1.text  #编码解析不到 用这个
            # print(html)
        # print(a)
        #匹配大图的正则
            # big=re.compile('<a target="_blank" id="1920x1200" href="(.*?)">')
            # a1 = re.findall(big, html)
            # print(a1)

            # big_msg="https://desk-fd.zol-img.com.cn"+ re.findall(big,html)[0]

            #大图的URL
            # print(big_msg)
            # s=re.compile('<li class=".*">\s*<a href="(.*?)">')
            # u=re.findall(s,html)
            # print(u)
            # l=[]
            # for i in u:
            #     l.append('http://desk.zol.com.cn'+i)
            # print(l)
    def get_big_img(self):
        a1 = self.get_url()
        c=0
        for i in a1:
            res=requests.get(i, headers={"User_Agent":user_agent[n]})
            html = res.content.decode('gb2312')
            s=re.compile('<img src="(.*?)"')
            img_url=re.findall(s,html)
            # print(img_url)

            #下载图片
            res2=requests.get(img_url[0])
            img=res2.content
            #print(img)
            #保存
            c+=1
            with open(f'D:\daima\猫\{c}.jpg','wb') as f:
                f.write(img)


z=ZOL()
#z.get_url()
#z.res()
# z.get_big_img_url()
z.get_big_img()

