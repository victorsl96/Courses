import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all(class_='quote')

for q in quotes:
	q_tag = q.find(class_='text')
	quote = q_tag.get_text()
	a_tag = q.find(class_='author')
	author = a_tag.get_text()
	url = q.find('a').attrs['href']
	quote_bank = 