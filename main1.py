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

    request = requests.get("https://www.google.com/search?q=tahmid+rayat", timeout=3)

except (requests.ConnectionError, requests.Timeout) as exception:

    print("[!] No internet connection [!]")

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



\033[96m ________  _____ ______   ________               \033[92m  ________  _________  _________  ________  ________  ___  ___ 
\033[96m |\   ____\|\   _ \  _   \|\   ____\             \033[92m |\   __  \|\___   ___|\___   ___|\   __  \|\   ____\|\  \|\  \   
\033[96m   \_/  \___||_|   |_||_|  |_| \___|\_           \033[92m \ \  \|\  \|___ \  \_\|___ \  \_\ \  \|\  \ \  \___|\ \  \\\  \   
\033[96m  \|____|\  \ \  \    \ \  \|____|\  \           \033[92m  \ \   __  \   \ \  \     \ \  \ \ \   __  \ \  \    \ \   __  \  
\033[96m    ____\_\  \ \__\    \ \__\____\_\  \          \033[92m   \ \  \ \  \   \ \  \     \ \  \ \ \  \ \  \ \  \____\ \  \ \  \ 
\033[96m   |\_________\|__|     \|__|\_________\         \033[92m    \ \__\ \__\   \ \__\     \ \__\ \ \__\ \__\ \_______\ \__\ \__\

\033[96m   \|_________|             \|_________|         \033[92m     \|__|\|__|    \|__|      \|__|  \|__|\|__|\|_______|\|__|\|__|




Choose the service you want to use

\033[0m[1] \033[96mServices

\033[92mType -help into the console to learn commands

                                         """

    print(logo)

    print("\n")



banner()







console1 = input("\033[91m \n\n[*]VerificationNum:\033[0m " )


def helpage():

    helpage_ = """



    Commands

    /attack "Phone Number" "ServiceNumber"



    """

    print(helpage_)

if console1 == "/help":
    hel_page()

