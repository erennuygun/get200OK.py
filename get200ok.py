#!/usr/bin/env python3
import requests
import argparse
from time import sleep
from threading import Thread

request=requests.session();
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", help="add wordlists")

args = parser.parse_args()

def check_status(url):
        try:
                page=requests.get(url,timeout=2)
                status=page.status_code
        except:
                status='bad'
        if status==200:
                print (url)

if args.wordlist:
        wordlist=args.wordlist

with open(args.wordlist) as f:
        for line in f.read().splitlines():
                thread = Thread(target = check_status,args = (line,))
                thread.start()
