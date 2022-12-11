#!/usr/bin/env python

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

    os.system('pip2 install requests')


try:

    request = requests.get("https://github.com/AnilKrkmz/SmsAttach", timeout=3)

except (requests.ConnectionError, requests.Timeout) as exception:

    print("[!] Internet Baglantı Sorunu [!]")

    sys.exit()

import requests

from bs4 import BeautifulSoup




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


\033[96m|\   ____\|\   _ \  _   \|\   ____\      \033[92m |\   __  \|\___   ___\\___   ___\\   __  \|\   ____\|\  \|\  \    
\033[96m\ \  \___|\ \  \\\__\ \  \ \  \___|_     \033[92m \ \  \|\  \|___ \  \_\|___ \  \_\ \  \|\  \ \  \___|\ \  \\\  \   
\033[96m \ \_____  \ \  \\|__| \  \ \_____  \    \033[92m  \ \   __  \   \ \  \     \ \  \ \ \   __  \ \  \    \ \   __  \  
\033[96m  \|____|\  \ \  \    \ \  \|____|\  \   \033[92m   \ \  \ \  \   \ \  \     \ \  \ \ \  \ \  \ \  \____\ \  \ \  \ 
\033[96m   \____\_\  \ \__\    \ \__\____\_\  \   \033[92m    \ \__\ \__\   \ \__\     \ \__\ \ \__\ \__\ \_______\ \__\ \__\
\033[96m   |\_________\|__|     \|__|\_________\ \033[92m     \|__|\|__|    \|__|      \|__|  \|__|\|__|\|_______|\|__|\|__|
                                                                
                                                   



Kullanmak Istediginiz Servisi Secin



\033[0m[1] \033[96mhttps://sms-online.co/receive-free-sms/



\033[92mType -help komutları ogrenmek icin 

                                         """

    print(logo)

    print("\n")



banner()





console1 = input("\033[91m \n\n[*]Atak yapilacak numara: \033[0m " )

if console1 == "/help":
    helpage()

