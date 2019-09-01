"""
import requests
import re
qwe={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
req=requests.get('https://www.fpzw.com/xiaoshuo/88/88413',headers=qwe)
res=req.content.decode('gbk')
#print(res)
s1=re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
urs=re.findall(s1,res)  #列表
#print(urs)
k={}
for i in urs:
    url=f'https://www.fpzw.com/xiaoshuo/88/88413/{i[0]}.html'
    mu=i[1]
    k[mu]=url
    #print(k)
    req=requests.get(k[mu],headers=qwe)
    res=req.content.decode('gbk')
    #print(res)
    s1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p></div>')
    s2=re.compile('<h2>(.*?)</h2>')
    mulu=re.findall(s2,res)
    neirong =re.findall(s1,res)
    a=neirong[0]
    a1=a.replace('&nbsp;&nbsp;&nbsp;&nbsp;','')
    a2=a1.replace('<br /><br />','\n')
    with open('d.txt','a',encoding='utf-8') as fb:
        fb.write(f"{mulu[0]}\n")
        fb.write(a2)
        fb.write('\n')
"""
"""
import requests
import re
qwe={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
req=requests.get('https://www.fpzw.com/xiaoshuo/88/88413',headers=qwe)
res=req.content.decode('gbk')
#print(res)
s1=re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
urs=re.findall(s1,res)  #列表
#print(urs)
for i in urs:
    url=f'https://www.fpzw.com/xiaoshuo/88/88413/{i[0]}.html'
    mu=i[1]
    #print(k)
    req=requests.get(url,headers=qwe)
    res=req.content.decode('gbk')
    #print(res)
    s1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p></div>')
    neirong =re.findall(s1,res)
    a=neirong[0]
    a1=a.replace('&nbsp;&nbsp;&nbsp;&nbsp;','')
    a2=a1.replace('<br /><br />','\n')
    with open('f.txt','a',encoding='utf-8') as fb:
        fb.write(f"{mu}\n")
        fb.write(a2)
        fb.write('\n')
        
"""
"""
import requests
import re

class add(object):
    def qwe(self,inter,name):
        qwe = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
        req = requests.get(inter, headers=qwe)
        res = req.content.decode('gbk')
        # print(res)
        s1 = re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
        urs = re.findall(s1, res)  # 列表
        # print(urs)
        for i in urs:
            url = f'{inter}{i[0]}.html'
            mu = i[1]
            # print(k)
            req = requests.get(url, headers=qwe)
            res = req.content.decode('gbk')
            # print(res)
            s1 = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p></div>')
            neirong = re.findall(s1, res)
            a = neirong[0]
            a1 = a.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '')
            a2 = a1.replace('<br /><br />', '\n')
            with open(name, 'a', encoding='utf-8') as fb:
                fb.write(f"{mu}\n")
                fb.write(a2)
                fb.write('\n')
l=add()
l.qwe('https://www.fpzw.com/xiaoshuo/88/88413/','qi.txt')

"""
"""
import re
import requests
import random

n = random.randint(0, 36)
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

res1 = requests.get('http://desk.zol.com.cn/bizhi/7590_94219_2.html', headers={"User-Agent": user_agent[n]})

html1 = res1.text
s = re.compile('<li class=".*">\s*<a href="(.*?)">')
u = re.findall(s, html1)
#print(u)
urls=[]
for i in u:
    xiao_tu_url = 'http://desk.zol.com.cn' + i
    urls.append( xiao_tu_url)
#print(urls)
urls1=[]
#大图URL 文本html
for i in urls:
    res2=requests.get(i)
    html2=res2.content.decode('gb2312')
    big = re.compile(' <a target="_blank" id=".*?" href="(.*?)">.*?</a>')
    s = re.findall(big, html2)
    #print(html2)
    #print(s)
    if len(s):
        uls = requests.get("http://desk.zol.com.cn" +s[0])
        urls1.append(uls)
        #html3 ='urls1.text'
       # print(html3)
c=0
for i in urls1:
    res3 = requests.get("http://desk.zol.com.cn" + s[0])
    html3 = res3.text
    #print(html3)
    x = re.compile('<img src="(.*?)">')
    g = re.findall(x, html3)
    #print(g)
#保存
    res4 = requests.get(g[0])
    img = res4.content
    c+=1
    with open(f'D:/daima/{c}.jpg', 'wb') as f:
        f.write(img)
"""

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
        #print(u)
        j=[]
        for i in u:
            j.append('http://desk.zol.com.cn/bizhi/7590'+i)
        #print(j)
        return  j
    # 从html文本中找我们要的
    def get_big_img_url(self):
        a=self.get_url()    #none --html文本
        for i in a:
            res1=requests.get(i,headers={"User_Agent":user_agent[n]})
            html=res1.text  #编码解析不到 用这个
            #print(html)
        #print(a)
            #匹配大图的正则
            big=re.compile(' <a target="_blank" id=".*?" href="(.*?)">')
            a1 = re.findall(big, html)
            #print(a1)

            big_msg="https://desk-fd.zol-img.com.cn"+ re.findall(big,html)[0]

            #大图的URL
            print(big_msg)
            s=re.compile('<li class=".*">\s*<a href="(.*?)">')
            u=re.findall(s,html)
            #print(u)
            l=[]
            for i in u:
                l.append('http://desk.zol.com.cn'+i)
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
#z.get_big_img_url()
z.get_big_img()
"""


"""
import requests,re
class Douban(object):
    def print_res(self,page):
        url=f'https://movie.douban.com/top250?start={page}&filter='
        head={'User-Aengt':"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
        res=requests.get(url=url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,html):
        patt=re.compile(r'<div class="hd">(.*?)</span>',re.S)
        items=re.findall(patt,html)
        title, lianjie = [],[]
        for i in items:
            cc=re.compile('<span class="title">(.*)',re.S)
            ww=re.findall(cc,i)
            title.append(ww[0])
            # print(len(items))
            # print(title)
        tupian1=re.compile('<div class="pic">(.*?)</a>',re.S)
        bbb=tupian1.findall(html)
        #print(bbb)
        for j in bbb:
            tupian=re.compile('src="https://(.*).jpg"',re.S)
            qqq=tupian.findall(j)
            #print(qqq)
            ccc='https://'+qqq[0]+'.jpg'
            #print(ccc)
            lianjie.append(ccc)
        return title,lianjie
    def saves(self,ziyuan):
        for k,p in enumerate(ziyuan[1]):
            res=requests.get(p)
            hhh=res.content
            with open(f'E:\电影\{ziyuan[0][k]}.jpg','wb') as f:
                f.write(hhh)
#if __name__=='__main__':
dou=Douban()
for i in range(0,101,25):
    h=dou.print_res(i)
   # print(htm)
    z=dou.guolv(h)
    dou.saves(z)

    #print(dou.print_res())

"""
"""
import requests,re,random,xlrd

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
#<div class="job-title">测试工程师</div>\s*?< span class ="red" > 11-22K < / span >\s*?


from xlutils.copy import copy
qwe=user_agent[n]
for i in range(1,6):
    req = requests.get(f'https://www.zhipin.com/c101010100/?query=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page={i}&ka=page-{i}', headers={"User-Agent": qwe})
    #req=requests.get(f'https://www.zhipin.com/c101010100-p100301/?page={i}&ka=page-{i}',headers={"User-Agent":qwe})
    res = req.content.decode("utf-8")
    # print(res)
    s=re.compile('<div class="job-title">(.*?)</div>\s*?<span class="red">(.*?)</span>\s*?<div class="info-detail"></div>\s*?</a>\s*?</h3>\s*?<p>(.*?)<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>\s*?</div>\s*?<div class="info-company">\s*?<div class="company-text">\s*?<h3 class="name"><a href=".*?" ka=".*?" target="_blank">(.*?)</a></h3>\s*?<p>(.*?)<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>')
    s1=re.findall(s,res)
    f=xlrd.open_workbook("73.xls")
    new=copy(f)
    table=new.add_sheet('12')
    k=len(table.rows)
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            table.write(k,j,s1[i][j])
        k+=1
    new.save('73.xls')
    """
"""
import requests,re, random, xlrd,json

n = random.randint(0, 36)

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



from xlutils.copy import copy

qwe = user_agent[n]
class qw(object):
    def add(self):
        req = requests.get(r'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.48498904&x-zp-page-request-id=5d3adb3d803a48978ee33ed373e60afd-1562671210360-559078&x-zp-client-id=2b6969d6-4354-4ead-8150-5d0dc8a4ddb8', headers={"User-Agent": qwe})
        res = req.text
        # a1 = json.loads(res)
        # a2 = a1['data']['results']
        # a3 = 0
        # for i in a2:
        #     a3 += 1
        #     print(i)
        print(res)

        s = re.compile(r'"jobName":"(.*?)".*?company":{"name":"(.*?)".*?display":"(.*?)".*?salary":"(.*?)".*?eduLevel":{"name":"(.*?)".*?workingExp":{"name":"(.*?)"',re.S)

        s1= re.findall(s,res)
       # print(len(s1))
        return s1
    def awk(self):
        w=self.add()
        f = xlrd.open_workbook("73.xls")
        new = copy(f)
        table = new.add_sheet('3')
        for i in range(len(w)):
            for j in range(len(w[i])):
                table.write(i, j,w[i][j])

        new.save('73.xls')
a=qw()
a.awk()
a.add()
"""
"""
#写入数据库
import pymysql,requests,re
class add(object):

    def qwe(self):
        
        req = requests.get(
            r'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.48498904&x-zp-page-request-id=5d3adb3d803a48978ee33ed373e60afd-1562671210360-559078&x-zp-client-id=2b6969d6-4354-4ead-8150-5d0dc8a4ddb8',
            headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"})
        res = req.text
        s = re.compile(r'"jobName":"(.*?)".*?company":{"name":"(.*?)".*?display":"(.*?)".*?salary":"(.*?)".*?eduLevel":{"name":"(.*?)".*?workingExp":{"name":"(.*?)"',re.S)
        s1 = re.findall(s, res)
        #print(s1)
        return s1
    def foo(self):
        al=self.qwe()
       # print(al)
        connect=pymysql.connect(
            host="192.168.10.8",
            port=3306,
            user="root",
            password="123456",
            charset="utf8")
            #database="stu1993"
        cu=connect.cursor()
        sql = "create database stu1995 default charset utf8 collate utf8_general_ci"
        cu.execute(sql)
        sql1 = "use stu1995"
        sql2 = "create table tongji(zhiwei char(25),gs char(25),dq char(10),xz char(10),xl char(15),nianx char(15))"
        cu.execute(sql1)
        cu.execute(sql2)

        for i in al:
            asd=f"insert into tongji values {i}"
            cu.execute(asd)
        connect.commit()

a=add()
a.qwe()
a.foo()

"""
"""
#   python 发送电子邮件   使用到的模块    smtplib   email
import  smtplib
from email.mime.text  import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#设置服务器所需要的信息
mail_host = "smtp.163.com"                                      #  邮件服务器地址
mail_user = "z199405156336@163.com"                            #  用户名
mail_pass = "z17792759651"                                   #客户端授权码或者密码
mail_port = 465                                                    #设置服务器端口号
sender = "z199405156336@163.com"                                           #  邮件发送方的地址
receviers = ["13592386651@163.com" ]                                    #  邮件接收方的地址

#  设置邮件信息如下
a = "python测试邮件"                   #  设置邮件主题
a1 = "这是我使用python发送的邮件"       # 设置邮件正文
s = MIMEText(a1,'plain','utf-8')       #三个参数：第一个为文本内容，第二个设置文本格式，第三个设置编码方式

#  发送邮件是填写收件人，发件人，主题
# header（）： 填写邮件头部
s['From'] = Header(sender)                              #  发送方信息
s["To"] = Header(str(";".join(receviers)))       # 接收方信息
s["Subject"] = Header(a)                         #  主题绑定

#  登录并发送邮箱
try:
    # 第一步，登录到自己的邮箱   #  一种是不使用授权密码
    s1 = smtplib.SMTP_SSL(host=mail_host,port=mail_port)
    # 第二步，输密码登录邮箱
    s1.login(user=mail_user,password=mail_pass)
    # 第三步,发送邮件，as_string()    以字符串的形式发送出去
    s1.sendmail(sender,receviers,s.as_string())
    #  第四步，发送邮件之后退出邮箱
    s1.quit()
    print("发送成功，退出邮箱")
except smtplib.SMTPException as e :
    print("登录失败")                    #   错误类
"""
# import requests,re
# req = requests.get(
#             r'http://desk.zol.com.cn/bizhi/7605_94433_2.html',
#             headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"})
# res = req.text
# #print(res)
# s=re.compile('class="(.*?)"\s.*<a href="(.*?)">\s.*<img src="(.*?)">.*</a>\s.*<i><em>1</em>.*</i>\s.*<i><em>1</em>')
#
#
#
