import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random

try:
    import requests
except ImportError:
    print('Error !! : Required dependencies not set!')

yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']

def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def banner():
    clr()
    logo = """
    
███████╗██████╗░███████╗███████╗░░░░░░██████╗███╗░░░███╗░██████╗
██╔════╝██╔══██╗██╔════╝██╔════╝░░░░░░██╔════╝████╗░████║██╔════╝
█████╗░░██████╔╝█████╗░░█████╗░░█████╗╚█████╗░██╔████╔██║╚█████╗░
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░╚════╝░╚═══██╗██║╚██╔╝██║░╚═══██╗
██║░░░░░██║░░██║███████╗███████╗░░░░░░██████╔╝██║░╚═╝░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝░░░░░░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░ """
    print(logo)
    print("\n")
    

def Track() :
  TXTID = input("Enter Text ID to track \n\t -->>")
  os.system(f"curl https://textbelt.com/status/{TXTID}")
  input("\nPress Enter To Exit..")
  exit()


clr()
banner()
    
while True:
	print("\033[0m")
	break
type = 0
try:
	if sys.argv[1] == "track":
		type = 1
except Exception:
	type = 0
if type == 1:
	print("Track The Anonymous Message You Sent Using Tool.")
	print()
	Track()
elif type == 0:
	while True:
		print("With this utility you can send free anonymous messages")
		print("For example: +380 +7 +1  but do not write the number!")
		cc = input("\tWhile Country Code (Without +) : ")
		if '+' in cc:
		        tc = list(cc)
		        tc.remove('+')
		        cc = ''.join(tc)
		        cc = cc.strip()
		if len(cc) >= 4 or len(cc) < 1:
		        print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
		        continue
		pn = input("While Phone Number : +" + cc + " ")
		if len(pn) <= 6:
		        print('\n\nInvalid Phone Number..\n')
		        continue
		numbe = cc + pn
		if not numbe.isdigit():
		            print('\n\nPhone Number Must Consist Of Numbers Only\n')
		            continue
		receiver = '+' + numbe
		text = input("Write message to send : ")
		
		resp = requests.post('https://textbelt.com/text',{
			'phone' : receiver,
			'message' : text ,
			'key' : 'textbelt'
		})
		
		print(resp.json())
		input('\n\n\nBye Bye! Have a nice day\n')
		break
		if '"success" : true ' in resp.text:
		    print("\033[92m Message Sent Succesfully \033[0m")
		    input('\n\t\tPress Enter To Exit...')
		    banner()
		    exit()
		if '"success" : false ' in resp.text:
		    print("\033[91m Error Occured")
		    print("\033[91m Failed to send SMS! ")
		    input('\n\t\tPress Enter To Exit...')
		    banner()
		    exit()
		exit() 
