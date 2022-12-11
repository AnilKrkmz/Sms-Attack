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

from bs4 import BeautifulSoup **
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


def helpage():

    helpage = """



    Commands
    Get Num



    """

    print(helpage)