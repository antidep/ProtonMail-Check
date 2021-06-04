import requests
from colorama import init, Fore, Back, Style
init(convert=True)

banner = '''
 __   __   __  ___  __           __        ___  __       
|__) |__) /  \  |  /  \ |\ | __ /  ` |__| |__  /  ` |__/ 
|    |  \ \__/  |  \__/ | \|    \__, |  | |___ \__, |  \ 
                                                         
'''

options = ['1','2']

def check_username(email):
    try:
        link = "https://api.protonmail.ch/pks/lookup?op=index&search=" + email + ""
        r = requests.get(link)
        if "info:1:0" in r.text:
            print(Back.GREEN + email + Style.RESET_ALL)
        if "info:1:1" in r.text:
            print(Back.RED + email + Style.RESET_ALL)
    except Timeout:
        print("Request Timeout")

def list():
    file = input('File:')
    files = open("xxx" + file, "r") #Full directory to the folder
    words = files.read().split('\n')
    for i in range(len(words)):
        email = words[i]
        user = email + "@protonmail.com"
        check_username(user)
    main()

def main():
    option = input("M | L [1/2]:")
    while option not in options:
        option = input("M | L [1/2]:")
    if option == '1':
        while True:
            user = input('Email:')
            if "@protonmail.com" not in user:
                email = user + "@protonmail.com"
                check_username(email)
            else:
                check_username(user)
    if option == '2':
        list()

print(banner)

print("\n" + Back.GREEN + " " + Style.RESET_ALL + " Available")
print(Back.RED + " " + Style.RESET_ALL + " Not Available\n")

main()
