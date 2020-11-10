import requests
from bs4 import BeautifulSoup

op = open('result.txt', 'w')

keyword = input('Your Keyword: ')
payload = {
	'enter': keyword
}
url = 'https://www.coolgenerator.com/tag-generator'

r = requests.post(url, data=payload)
soup = BeautifulSoup(r.text, 'html.parser')
allKey = soup.findAll('li','col-sm-4')

def loop():
	global op
	for a in allKey:
		keywordNew = a.find('span').text
		print('[+] '+keywordNew)
		op.write(keywordNew+'\n')
	op.close

loop()
