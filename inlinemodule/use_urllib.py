#!/usr/local/bin python3

# -*- coding: utf-8 -*-

# 对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：
from urllib import request

def get_request(url):
	with request.urlopen(url) as f:
		data = f.read()
		print('Status:', f.status, f.reason)
		for key, value in f.getheaders():
			print('%s : %s' % (key, value))
		print('Data:', data.decode('utf-8'))

get_request('https://api.douban.com/v2/book/2129650')

# Post
# 模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式
# 以username=xxx&password=xxx的编码传入：
from urllib import request, parse
print('Login to weibo.cn...')
email = input('Email:')
passwd = input('Password:')
login_data = parse.urlencode([
	('username', email),
	('password', passwd),
	('entry', 'mweibo'),
	('client_id', ''),
	('savestate', '1'),
	('ec', ''),
	('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
	])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
	print('Status:', f.status, f.reason)
	for key, value in f.getheaders():
		print('%s : %s' % (key, value))
	print('Data:', f.read().decode('utf-8')) 




# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，
# 我们需要利用ProxyHandler来处理，示例代码如下：

proxy_header = urllib.request.ProxyHandler({'http' : 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib,request.build_opener(proxy_header, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
	pass



