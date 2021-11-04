import requests
from random import choice
from color import color_coverter

url = 'https://icanhazdadjoke.com/search'
msg = 'DAD JOKE 1.0'

print(color_coverter(msg,"green"))

user_input = input('Let me tell you a joke! Give me a topic:  ')
num = int(input('how many jokes do you want? '))

response = requests.get(
	url,
	headers={'Accept': 'application/json'},
	params={'term': user_input}
)

data = response.json()

n = 1
while n <= num:
	print("\n" + dict(choice(data['results'])).get('joke') + "\n")
	n += 1






