import requests
import random
from bs4 import BeautifulSoup
import os
import sys 
def main(index):
    def mainfun():
        rand_page = random.randint(1,52)
        url = 'http://dumb.com/confessions/page/' + str(rand_page)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find_all(align='left')
        print('')
        return '                                                              ' + result[random.randint(1,18)].text

    def mainfun2():

        headers = {
            'Host': 'boredhumans.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'closeContent-Length: 58',
            'Content-Length': '32',
        }

        data = 'Upgrade-Insecure-Requests: 1\\x0d\\x0a\\x0d\\x0a'

        response = requests.post('https://boredhumans.com/confessions.php', headers=headers, data=data)
        soup = BeautifulSoup(response.content, 'html.parser')
        filter_ = soup.find_all('center')[1].find_all('center')[random.randint(0,2)]
        return filter_.text 
    if index == 1:
        return mainfun()
    elif index == 2:
        try:
            return mainfun2()
        except:
            pass
    else:
        return "Not proper index supplied"

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
            print("iConfess v0.4")
    except:
        while (True):
            ask = input('Press <Enter> or <q> quit: ')
            if ask  != "":
                exit()
                break
            else:
                os.system('clear')
                banner()
                print(main(random.randint(1,2)))



