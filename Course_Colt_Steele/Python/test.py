import requests
user_input = input("topic: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(url,headers={})