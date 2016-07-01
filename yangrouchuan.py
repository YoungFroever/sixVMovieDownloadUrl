#-*- coding:utf-8 -*-

import codecs
import requests
from bs4 import BeautifulSoup

def download_page(url):
    return requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}).content

def parse_html(html):
	#soup就相当于一个静态网页中所有的html语句
	soup = BeautifulSoup(html,'lxml')
	a = soup.find('table',attrs={'cellspacing':'1'})
	movieText = []
	movieUrl = []
	final = []
	for movie_tr in a.find_all('tr'):
		text = movie_tr.find('td',attrs={'bgcolor':'#ffffbb'})
		temp = movie_tr.find('a')
		#容错处理
		if movie_tr.find('a'):
			final.append('资源名称:'+movie_tr.get_text()+'下载网址:'+temp['href'])
			#final.append(movie_tr.get_text())
			#final.append(temp['href'])
			pass
	return final



#第二部扩展
def post_php(url):
	return None

	
def main():
	#6v系列
	url = input('输入6v电影下载页的网址:')
	#url = 'http://www.6vhao.com/3D/2016-06-30/27426.html'
	#url = 'http://www.6vhao.com/mj/2015-04-12/BYHZGQLDYX.html'
	#url = targetUrl

	html = download_page(url)
	for item in parse_html(html):
		print(item)

if __name__ == '__main__':
    main()