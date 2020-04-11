import requests
import random
from bs4 import BeautifulSoup
import os
import sys 
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
    print('                                                           ____                        ')
    print('                                                          / ___|  ___  _ __ _ __ _   _ ')
    print('                                                          \___ \ / _ \|  __|  __| | | |')
    print('                                                           ___) | (_) | |  | |  | |_| |')
    print('                                                          | ___/ \___/|_|  |_|   \__, |')
    print('                                                                                 |___/ ')
    print('                                                       <Sponsored By: http://dumb.com>         ')
    print('                                                   <Copyright: 0x0is1 (github.com/0x0is1)>     ')
    print('                                                                                               ')

check()

if __name__ == "__main__":
    try: 
        if sys.argv[1] == "-v":
            print("iConfess v0.3")
    except:
        while (True):
            ask = input('Press <Enter> or <q> quit: ')
            if ask  != "":
                exit()
                break
            else:
                mainfun()


