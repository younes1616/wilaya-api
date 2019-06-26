if __name__ == '__main__':
	import requests
	import re
	from bs4 import BeautifulSoup
	
	from config import *
	from data.wilaya.wilaya import *
	
	# for containig all the elements
	AR = dict()
	FR = dict()
	
	# for geting the names of the baladiya in Latin

	for wl in wilayaCode:
		html = requests.get(FR_LINK_M.format(wl))
		html = BeautifulSoup(html.text, 'html.parser')

		baladiya_name = html.find_all("table")[-2].find_all("td")[7::6]
		baladiya_id = html.find_all("table")[-2].find_all("td")[6::6]

		fix = lambda x: re.findall(r'<td>(.*)</td>', str(x))[0]

		for item in zip(map(fix, baladiya_id), map(fix, baladiya_name)):
			FR[item[0]] = item[1]
	

	# for geting the names of the baladiya in Arabic

	for wl in wilayaCode:
		html = requests.get(AR_LINK_M.format(wl))
		html = BeautifulSoup(html.text, 'html.parser')

		baladiya_name = html.find_all("table")[-2].find_all("td")[7::6]
		baladiya_id = html.find_all("table")[-2].find_all("td")[6::6]

		fix = lambda x: re.findall(r'<td>(.*)</td>', str(x))[0]

		for item in zip(map(fix, baladiya_id), map(fix, baladiya_name)):
			AR[item[0]] = item[1]


	for item in FR.keys():
		if len(item) == 3:
			wilaya_code = item[0]
		if len(item) == 4:
			wilaya_code = item[0:2]
			
		print("\"",item,"\":", "{", end="")
		print("\"code\":\"{}\", \"nameAr\":\"{}\", \"nameFr\":\"{}\", \"nameEn\":\"{}\","
		      " \"wilayaCode\":\"{}\"".format(item, AR[item], FR[item], FR[item], wilaya_code), end="")
		print("}")