from termcolor import colored
from colorama import init
from pyfiglet import figlet_format as form

init()

def color_coverter(message,color):
	return colored(form(message), color)

if __name__ == "main":	
	message = input('What message do you want to print? ')
	color = input('What color? ')

	print(color_coverter(message,color))