import requests
import time
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
print(Fore.GREEN + "XSS DETECTOR" + Fore.RED + "By Deep Nandre" + Style.RESET_ALL)
time.sleep(2)
print()
pog = input("POST or GET ? (p/g) : ")
if pog == "g":
    try:
        site = input("Website to test? (with parameters) : ")
        r = requests.post(site, headers=header)
        time.sleep(1)
        print()
        print(Fore.GREEN + "The site respond!" + Style.RESET_ALL)
    except:
        print()
        print("does the script respond...")
        time.sleep(3)
        print()
        print(Fore.RED + "The website doesn't respond, try again. (with https:// or http:// ...)" + Style.RESET_ALL)
        sys.exit(0)
    print()
    try:
            repertoirepayload = input(" wordlist.txt directory: ")
            reper = open(repertoirepayload, "r")
    except FileNotFoundError:
        print()
        print("The File" + Fore.RED + repertoirepayload + Style.RESET_ALL + "doesn't exist, try again!")
        sys.exit(0)
    print()
    print(Fore.GREEN + "Testing in process... \n")
    time.sleep(2)
    f = open(repertoirepayload, "r")
    1 = 1
    for line in f:
        print()
        print(Fore.GREEN + "I test the payload" + str(1))
        if line in requests.get(site + line, headers=header).text:
            print(Fore.RED + "XSS FOUND HERE : \n" + Style.RESET_ALL)
            print(requests.get(site + line, headers=header).url)
        else:
            print(Fore.RED + "The Payload" + str(1) + "does not trigger the XSS Filter." - Style.RESET_ALL)
            print()
            1 += 1
elif pog == "p"
    try:
        site = input("URL to test : ")
        data = input("Post DATA : ")
        r = requests.post(site, headers=header)
        time.sleep(1)
        print()
        print(Fore.GREEN + "The site respond!" + Style.RESET_ALL)
    except:
        print()
        print("does the script respond...")
        time.sleep(3)
        print()
        print(Fore.RED + "The website doesn't respond, try again. (with https:// or http:// ...)" + Style.RESET_ALL)
        sys.exit(0)
    print()
    try:
            repertoirepayload = input(" wordlist.txt directory: ")
            reper = open(repertoirepayload, "r")
    except FileNotFoundError:
        print()
        print("The File" + Fore.RED + repertoirepayload + Style.RESET_ALL + "doesn't exist, try again!")
        sys.exit(0)
    print()
    print(Fore.GREEN + "Testing in process... \n")
    time.sleep(2)
    f = open(repertoirepayload, "r")
    1 = 1
    for line in f:
        print()
        print(Fore.GREEN + "I test the payload" + str(1))
        if line in requests.get(site + line, headers=header).text:
            print(Fore.RED + "XSS FOUND HERE : \n" + Style.RESET_ALL)
            print(requests.get(site + line, headers=header).url)
        else:
            print(Fore.RED + "The Payload" + str(1) + "does not trigger the XSS Filter." - Style.RESET_ALL)
            print()
            1 += 1
else:
        print("Unknown answer.")
        sys.exit()

