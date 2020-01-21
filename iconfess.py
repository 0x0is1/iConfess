import requests
import random
from bs4 import BeautifulSoup
import os

def mainfun():
    os.system('clear')
    banner()
    rand_page = random.randint(1,52)
    url = 'http://dumb.com/confessions/page/' + str(rand_page)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all(align='left')
    print('')
    print('                                                              ' + result[random.randint(1,18)].text)

def check():
    if requests.get('https://example.com').ok:
        print('You are Online')
    else:
        print("You're Offline")
        exit()

def banner():
    print('                                         ___      _                ____                        ')
    print('                                        |_ _|    / \   _ __ ___   / ___|  ___  _ __ _ __ _   _ ')
    print('                                         | |    / _ \ | |_   _ \  \___ \ / _ \|  __|  __| | | |')
    print('                                         | |   / ___ \| | | | | |  ___) | (_) | |  | |  | |_| |')
    print('                                        |___| /_/   \_\_| |_| |_| |____/ \___/|_|  |_|   \__, |')
    print('                                                                                         |___/ ')
    print('                                                       <Sponsored By: http://dumb.com>         ')
    print('                                                   <Copyright: 0x0is1 (github.com/0x0is1)>     ')
    print('                                                                                               ')
check()
mainfun()
while (True):
    ask = raw_input('Press <Enter> or <q> quit: ')
    if ask  == "":
        mainfun()
    else:
        exit()


