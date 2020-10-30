import json
from os import system

def read(key):
	with open('bot/.config.json', 'r') as v:
		x = json.load(v)
	return x[key]
def write(key, val):
	with open('bot/.config.json', 'r') as v:
		x = json.load(v)
	x[key] = val
	with open('bot/.config.json', 'w') as v:
		json.dump(x, v, indent=4)

def config(opersys):
	ch = input("Choose an option (read docs): ")
	if ch == "1":
		if opersys == "win":
			system("py bot/main.py")
		else:
			system("python3 bot/main.py")
	elif ch == "2":
		co1 = input("Please paste your token: ")
		if len(co1) > 0:
			write('token', co1)
			print("OK")
		else:
			print("Skipped")
		co2 = input("Please enter your custom activity type: ")
		if len(co2) > 0:
			if co2 == "game":
				write('acttype', co2)
			elif co2 == "watch":
				write('acttype', co2)
			elif co2 == "listen":
				write('acttype', co2)
			else:
				print("INVALID!")
				return
			print("OK")
		else:
			print("Skipped")
		co3 = input("Please input your activity name: ")
		if len(co3) > 0:
			write('act', co3)
			print("OK")
		else:
			print("Skipped")

def win():
	with open('bot/.config.json', 'r') as v:
		x = json.load(v)
	if x['os'] == 'null':
		x['os'] = 'windows'
		with open('bot/.config.json', 'w') as v:
			json.dump(x, v, indent=4)
	else:
		config("win")

def deb():
	with open('bot/.config.json', 'r') as v:
		x = json.load(v)
	if x['os'] == 'null':
		x['os'] = 'linux'
		with open('bot/.config.json', 'w') as v:
			json.dump(x, v, indent=4)
	else:
		config("deb")


if __name__ == '__main__':
	print("Please use the script to run this.")
