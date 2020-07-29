# English to hindi dictionary

import requests
from bs4 import BeautifulSoup

print('\t\tEnglish to hindi dictionary\n')

word = input('Enter your word : ')
print()
url = 'https://dict.hinkhoj.com/hindi-dictionary.php?word='+word+'&ie=UTF-8'

try :
	r = requests.get(url)
except :
	print('check your internet connection')
else :
	html = r.text
	soup = BeautifulSoup(html,'html.parser')
	results = soup.find_all('div',class_='row word_meaning_div')

	for i in results[:3]:
		word = i.select('a',class_='eng_dict_span')
		print('word :',word[0].text)
		print('meaning :',word[1].text)
		print()