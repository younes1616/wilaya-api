if __name__ == '__main__':
	import requests
	import re
	from bs4 import BeautifulSoup
	
	from config import *
	from data.wilaya.wilaya import *
	
	'''
	# for geting the names of the baladiya in Latin
	c = 1

	for wl in wilayaCode:
		html = requests.get(FR_LINK_M.format(wl))
		html = BeautifulSoup(html.text, 'html.parser')

		baladiya_name = html.find_all("table")[-2].find_all("td")[7::6]
		baladiya_id = html.find_all("table")[-2].find_all("td")[6::6]

		fix = lambda x: re.findall(r'<td>(.*)</td>', str(x))[0]

		for item in zip(map(fix, baladiya_id), map(fix, baladiya_name)):
			if c % 10 == 0:
				print()
			print(item, end=", ")
			c+=1
	'''
	
	'''
	# for geting the names of the baladiya in Arabic
	c = 1

	for wl in wilayaCode:
		html = requests.get(AR_LINK_M.format(wl))
		html = BeautifulSoup(html.text, 'html.parser')

		baladiya_name = html.find_all("table")[-2].find_all("td")[7::6]
		baladiya_id = html.find_all("table")[-2].find_all("td")[6::6]

		fix = lambda x: re.findall(r'<td>(.*)</td>', str(x))[0]

		for item in zip(map(fix, baladiya_id), map(fix, baladiya_name)):
			if c % 6 == 0:
				print()
			print(item, end=", ")
			c+=1
	'''