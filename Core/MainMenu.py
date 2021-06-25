import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mAnonymous SMS")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mAbout Utility")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mExit Utility")

op=int(raw_input("An0N-SMs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd anonymousSMS && python3 Core/sms.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd anonymousSMS && bash Core/About.sh")
elif(op==3):
 print("\033[1;31;40mQuiting Utility....")
 time.sleep(0.5)
else:
 print("\033[1;31;40mInvalid input. Quiting Utility") 
 time.sleep(0.5)
 os.system("cd")
 os.system("cd")
