# _*_ coding: utf-8 _*_

"""
python_spider.py by wangxin
"""

import urllib.error
import urllib.parse
import urllib.request
import http.cookiejar
import json

# POST请求示例
url = "http://localhost:8080/bbk-web/user/showUserList"
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "auth-token": "EIXYOsPmovDwDj7Koz/2Z6r4b4PunISsFpyR+1+SryX2dkZVfIEcFGzN1s4w6iP5Juh+0fixeNB7BnaaUZ1nGtPG+FF4nxRtk/jXhRf2YND2sMcDqtSCZ3COh8p0m/D515bDljlurMh0WQlg/ugSF6Je52jmfXiNJximLlRdsO7w2htgEWZ+lRLpyoRkNfhOCTVeaLcvsTLOvBRLYQAPyY2SfBraOJ19Q0ioEQrUSnJLjJOqtrWX2JFLn9qJHt1oDTiKKvzYA5/hjsROPgU6tXRgB0Xc4cUPO2twVgBgBrsDLt9dfZQBfNf467m0Z9mD7/e6+R7NCeFBn6TtGfk1zVLJ4bwnZAo0ScQBOOoRSnx2b6UXbKOZXBH3MqO59UJ/lHG6t5Zi7AbingNRlsKRCNs1hU0TvwkPPRGlSewj/pJ0Er3dP8OmDLMjGhyB3Wt32xjGbckg+95NsZnb+QB0o82dGiluZ3Vyoq+gSajvFMykq7l/thvsT/11lf21MZ5S1xCCw3U1DdtmQPi+s5eOINPnYEXIHxY2RBdDQy/DlDIw5cRcif62Oy10XEh6dStcKCjybP05AjgOx0CSiGYmwpq2OTyfqi0/do2NbxIfe547CzlUIjSMpswDn8V8VtKMKLUAaC3Zax8aLnozMoCiy5UgJU7cC1gqIr4nHlm5IQB4desmCRImST5nIU5m08PBClA03+eo24kHJLyrPTeS6nShu2UeaTelW5Ic3kw2NUjbGsCHB41KVWjKS+VtM8yTjFQD72A6ycfDkWLM+dVGi/licerrUyRWW7Z+W+4tpx1vffFD9pTLvNC3qPLukNkc"
}

data = {"pageNum": 1,"pageSize": 10,"userState": "0","userName": "lizhentan","organizationId": None}
# 之所以进行转换，因为 Content-Type 为 application/json
data = json.dumps(data)
# 不进行转换，会报错 TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
data = bytes(data, 'utf8')

request = urllib.request.Request(url, headers=headers, method='POST')
response = urllib.request.urlopen(request, data=data, timeout=10)
html = response.read().decode("utf-8")
print(html)

print("===============================")

# GET请求示例
url = "https://api.shensz.cn/api/1/paperBuilder/teacher_get_paper_questions?paper=002c5b63-9585-417b-8725-1ad6c73df67c&no_block=true"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Cookie": "aliyungf_tc=AQAAADMEt1+XJw0AWwlvcT5hKz57yoa9; username=%E4%B9%90%E5%B0%8F%E7%B1%B3; school=564204; username_pinyin=lexiaomi; phone=18825125400; uid=98226; role=1; sszservice.connect.sid=s%3AcONQ9uCUFWesVoxBTFbR5Oc178QloZ_j.YrvxxguJ3849BbVu%2BN52mLLrVVkWoHAgGHWZA15GZBA; Hm_lvt_027462e29e1dbce3fcb2a6b8b5a08280=1489735345; Hm_lpvt_027462e29e1dbce3fcb2a6b8b5a08280=1489735377"
}
request = urllib.request.Request(url, headers=headers, method='GET')

response = urllib.request.urlopen(request, timeout=100)
html = response.read().decode("utf-8")
print(html)


# # 首先定义下边可能需要的变量
# url = "https://www.baidu.com"
# headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
#
# # 最简单的网页抓取方式
# response = urllib.request.urlopen(url, timeout=10)
# html = response.read().decode("utf-8")
#
#
# # 使用Request实例代替url
# request = urllib.request.Request(url, data=None, headers={})
# response = urllib.request.urlopen(request, timeout=10)
#
#
# # 发送数据，即在Request()中添加data参数
# data = urllib.parse.urlencode({"act": "login", "email": "xianhu@qq.com", "password": "123456"})
# request1 = urllib.request.Request(url, data=data)           # POST方法
# request2 = urllib.request.Request(url+"?%s" % data)         # GET方法
# response = urllib.request.urlopen(request, timeout=10)
#
#
# # 发送Header，即在Request()中添加headers参数
# request = urllib.request.Request(url, data=data, headers=headers)   # 参数中添加header参数
# request.add_header("Referer", "http://www.baidu.com")               # 另一种添加header的方式,添加Referer是为了应对"反盗链"
# response = urllib.request.urlopen(request, timeout=10)
#
#
# # 网页抓取引发异常：urllib.error.HTTPError, urllib.error.URLError, 两者存在继承关系
# try:
#     urllib.request.urlopen(request, timeout=10)
# except urllib.error.HTTPError as e:
#     print(e.code, e.reason)
# except urllib.error.URLError as e:
#     print(e.errno, e.reason)
#
#
# # 使用代理，以防止IP被封或IP次数受限：
# proxy_handler = urllib.request.ProxyHandler(proxies={"http": "111.123.76.12:8080"})
#
# opener = urllib.request.build_opener(proxy_handler)     # 利用代理创建opener实例
# response = opener.open(url)                             # 直接利用opener实例打开url
#
# urllib.request.install_opener(opener)                   # 安装全局opener，然后利用urlopen打开url
# response = urllib.request.urlopen(url)
#
#
# # 使用cookie和cookiejar,应对服务器检查
# cookie_jar = http.cookiejar.CookieJar()
# cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
# opener = urllib.request.build_opener(cookie_jar_handler)
# response = opener.open(url)
#
#
# # 发送在浏览器中获取的cookie,两种方式:
# # (1)直接放到headers里
# headers = {
#     "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
#     "Cookie": "PHPSESSID=btqkg9amjrtoeev8coq0m78396; USERINFO=n6nxTHTY%2BJA39z6CpNB4eKN8f0KsYLjAQTwPe%2BhLHLruEbjaeh4ulhWAS5RysUM%2B; "
# }
# request = urllib.request.Request(url, headers=headers)
#
# # (2)构建cookie,添加到cookiejar中
# cookie = http.cookiejar.Cookie(name="xx", value="xx", domain="xx", ...)
# cookie_jar.set_cookie(cookie)
# response = opener.open(url)
#
#
# # 同时使用代理和cookiejar
# opener = urllib.request.build_opener(cookie_jar_handler)
# opener.add_handler(proxy_handler)
# response = opener.open("https://www.baidu.com/")
#
#
# # 抓取网页中的图片：同样适用于抓取网络上的文件。右击鼠标，找到图片属性中的地址，然后进行保存。
# response = urllib.request.urlopen("http://ww3.sinaimg.cn/large/7d742c99tw1ee7dac2766j204q04qmxq.jpg", timeout=120)
# with open("test.jpg", "wb") as file_img:
#     file_img.write(response.read())
#
#
# # HTTP认证：即HTTP身份验证
# password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()     # 创建一个PasswordMgr
# password_mgr.add_password(realm=None, uri=url, user='username', passwd='password')   # 添加用户名和密码
# handler = urllib.request.HTTPBasicAuthHandler(password_mgr)         # 创建HTTPBasicAuthHandler
# opener = urllib.request.build_opener(handler)                       # 创建opner
# response = opener.open(url, timeout=10)                             # 获取数据
