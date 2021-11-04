import requests
import pyfiglet
from random import choice
from color import color_coverter

msg = "DAD JOKE 3000"
print(color_coverter(msg,"magenta"))
user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
	url,
	headers={"accept": "application/json"},
	params={"term":user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
	print(choice(results)["joke"])
elif num_jokes == 1: 
	print(f"I found one joke about {user_input}. Here it is:")
	print(results[0]["joke"])
else:
	print(f"Sorry, couldn't find any jokes with your term: {user_input}")