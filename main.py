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

    request = requests.get("https://www.google.com/search?q=sms+intcontrol", timeout=3)

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



\033[96m\ \   / /___  _ __ (_) / _|(_)  ___  __ _ | |_ (_)  ___   _ __  \033[92m| \ | | _

\033[96m \ \ / // _ \| '__|| || |_ | | / __|/ _` || __|| | / _ \ | '_ \ \033[92m|  \| || | | || '_ ` _ \



\033[96m  \ V /|  __/| |   | ||  _|| || (__| (_| || |_ | || (_) || | | |\033[92m| |\  || |_| || | | | | |

\033[96m   \_/  \___||_|   |_||_|  |_| \___|\__,_| \__||_| \___/ |_| |_|\033[92m|_| \_| \__,_||_| |_| |_|



Choose the service you want to use



\033[0m[1] \033[96mhttps://sms-online.co/receive-free-sms/



\033[92mType -help into the console to learn commands

                                         """

    print(logo)

    print("\n")



banner()