if __name__ == '__main__':
	# execute each part alone, or all of them at one
	# as you like.
	
	
	#  for Arabic wilaya
	"""
	import requests
	import re
	from config import *
	
	html = requests.get(AR_LINK)
	#  in case you want to see the html page
	print(html.text)
	html = html.text
	print(re.findall(r'<option.*>(.*)</option>', html)[1:])
	"""
	
	#  for French wilaya
	"""
	html = requests.get(FR_LINK)
	#  in case you want to see the html page
	print(html.text)
	html = html.text
	print(re.findall(r'<option.*>(.*)</option>', html)[1:])
	"""
	
	#  for number wilaya
	"""
	print([i for i in range(1, 49)])
	"""
	
	
	# combine all the data
	"""
	from data.wilaya.wilaya import *
	import managedata as md
	
	wilaya = {}
	
	for code in wilayaCode:
		wilaya[code] = {}
	
		wilaya[code]["code"] = code
		wilaya[code]["nameAr"] = wilayaAr.json[int(code) - 1]
		wilaya[code]["nameFr"] = wilayaFr[int(code) - 1]
		wilaya[code]["nameEn"] = wilayaFr[int(code) - 1]
		wilaya[code]["codePost"] = wilayaCodePost[int(code) - 1]
		wilaya[code]["codeTel"] = wilayaCodeTel[int(code) - 1]
	
	
	print(wilaya)
	md.dumpData("./wilaya.json", wilaya)
	"""