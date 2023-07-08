"""
 _____  _____           _____  _____ 
(  __ )(  __ \|\     /|(  __ \(  __ )
| (    )|| (    \/| )   ( || (    \/| (    )|
| (__)|| (_    | |   | || (_    | (__)|
|     _)|  _)   ( (   ) )|  _)   |     _)
| (\ (   | (       \ \_/ / | (      | (\ (   
| ) \ \__| (___/\  \   /  | (____/\| ) \ \_
|/   \__/(_______/   \_/   (_______/|/   \__/
          Tool By Shadow Sentinel Force          
"""


import requests
import os
import time
import re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Style, init

init(autoreset=True)

def reverse_ipdomain(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        x = requests.get('https://api.reverseipdomain.com/?ip='+url, headers=headers, timeout=30).content
        if 'Domain Name' in x:
            regex = re.findall('<a href="/domain/(.*?)">', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name
                print("OK: {}".format(website_url))
                open('SUCCESS.txt', 'a').write(website_url + '\n')
        else:
            print("BAD IPS : " + url)
    except:
        pass


def rapid_dns(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        x = requests.get('https://rapiddns.io/s/'+url+'?full=1&down=1#result/', headers=headers, timeout=30).content
        if '<th scope="row ">' in x:
            regex = re.findall('<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name.replace('<td>', '').replace('</td>', '').replace('ftp.', '').replace('images.', '').replace('cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.', '').replace('webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
                print("OK: {}".format(website_url))
                open('SUCCESS.txt', 'a').write(website_url + '\n')
        else:
            print("BAD IPS : " + url)
    except:
        pass


def reverse_ip_lookup(url):
    try:
        rapid_dns(url)
        reverse_ipdomain(url)
    except:
        pass


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        ip_list = raw_input("Your List IPS : ")
        urls = open(ip_list, 'r').read().splitlines()
        num_threads = raw_input("THREAD : ")
        pool = ThreadPool(int(num_threads))
        pool.map(reverse_ip_lookup, urls)
    except:
        pass


if _name_ == '_main_':
    main()
