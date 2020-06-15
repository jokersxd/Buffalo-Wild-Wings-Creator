from colorama import Fore, init, Style
import threading
import requests
import random
import ctypes
import string
import time
import os

lock = threading.Lock()
ErrorCounter = 0
Created = 0
os.system('cls')

def Create():
    global ErrorCounter
    global Created
    try:
        session = requests.Session()
        headers = {
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        email = ('').join(random.choices(string.ascii_letters + string.digits, k=random.randrange(7,10))) + '@gmail.com'
        password = ('').join(random.choices(string.ascii_letters + string.digits, k=random.randrange(10, 15)))
        firstname = ('').join(random.choices(string.ascii_letters, k=random.randrange(6, 12)))
        surname = ('').join(random.choices(string.ascii_letters, k=random.randrange(6, 12)))
        years = ['1963', '1999', '1973', '1980', '1998', '1956', '1974', '1983', '1933', '1903', '1905', '1961', '1943', '1995', '1987', '1965']
        dob = '0' + str(random.randint(1, 9)) + '/' + '0' + str(random.randint(1, 9)) + '/' + str(random.choice(years))
        zipcode = ('').join(random.choices(string.digits, k=5))
        phone = ('').join(random.choices(string.digits, k=10))
        data = '{"data":{"email":"' + str(email) + '","password":"' + str(password) + '","firstName":"' + str(firstname) + '","lastName":"' + str(surname) + '","dob":"' + str(dob) + '","zip":' + str(zipcode) + ',"phone":"' + str(phone) + '","platform":"web"}}'
        POST = session.post('https://us-central1-buffalo-united.cloudfunctions.net/signUp', headers=headers, data=data)
        if '"Success":true' in POST.text:
            lock.acquire()
            print(Fore.GREEN + '[CREATED] ' + Fore.WHITE + Style.BRIGHT + str(email) + ':' + str(password))
            with open('Created.txt', 'a') as CreatedFile:
                CreatedFile.write(str(email) + ':' + str(password) + '\n')
            with open('Created - Capture.txt', 'a') as CaptureFile:
                CaptureFile.write('Login: ' + str(email) + ':' + str(password) + '\nFirst name: ' + str(firstname) + '\nLast name: ' + str(surname) + '\nDOB: ' + str(dob) + '\nZipcode: ' + str(zipcode) + '\nPhone: ' + str(phone) + '\n\n')
            Created += 1
            ctypes.windll.kernel32.SetConsoleTitleW('Buffalo Wild Wings Creator | Created: ' + str(Created) + ' | Errors: ' + str(ErrorCounter) + ' | Developed by jokers')
            lock.release()
        else:
            ErrorCounter += 1
            ctypes.windll.kernel32.SetConsoleTitleW('Buffalo Wild Wings Creator | Created: ' + str(Created) + ' | Errors: ' + str(ErrorCounter) + ' | Developed by jokers')
    except Exception as e:
        print(e)

while True:
    try:
        threading.Thread(target=Create, args=()).start()
    except RuntimeError:
        continue
