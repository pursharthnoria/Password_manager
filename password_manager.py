import backend
import hashlib
import random
import time
import sys
from getpass import getpass
from os import system

def rand_pass():
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    passw = ''
    for i in range(8):
        passw = passw+random.choice(alphabets)
    return passw

def hashed_pass():
    passwd = rand_pass()
    hashed_pass = hashlib.sha256(passwd.encode('utf-8')).hexdigest().upper()
    return hashed_pass[:15]

def check_master():
    backend.connect_master()
    rows = backend.view_master()
    if len(rows)<1:
        name = input('Please enter your name: ')
        password = getpass('Please enter a master password: ')
        backend.insert_master(name,password)
    else:
        password = getpass('Enter your master password: ')
        if password != backend.view_master()[0][1]:
            return 0
    return 1

if check_master()==0:
    print('Hey! You are not the master.')
else:
    backend.connect()
    print("*********************************")
    print('Hey! Welcome to password manager.')
    print("*********************************")
    while (True):
        print("\n*******************************")
        choice = int(input('1. Make a new entry.\n2. View all entries\n3. delete an entry\n4. Exit\nEnter your choice: '))
        print("*******************************\n")
        if choice == 1:
            web = input('Enter the service name: ')
            rows = backend.view()
            services = []
            for row in rows:
                services.append(row[0])
            if web in services:
                response = input('\nThe services already exists in database. Do you want to see the password instead? (y/n): ')
                if response == 'y':
                    print('The password is: '+backend.search(web)[0][0])
                    time.sleep(3)
                    continue
                else:
                    continue
            else:
                passw = hashed_pass()
                backend.insert(web,passw)
                print('The new password is '+passw+"\n\n")
                continue

        elif choice == 2:
            rows = backend.view()
            if len(rows)>0:
                print("\n")
                for row in rows:
                    print ("The password for {} is {}".format(row[0],row[1]))
            else:
                print('You have not generated any passwords yet.')
            print("**************************************************\n\n")

        elif choice == 3:
            web = input("Enter the service you want to delete: ")
            rows = backend.view()
            services=[]
            for row in rows:
                services.append(row[0])
            if web in services:
                backend.delete(web)
                print("The password has been deleted Successfully.")
            else:
                print("There is no such password in our database.")
            print("*********************************************")       

        elif choice == 4:
            system('cls') 
            sys.exit()

        else:
            print("Enter a valid choice please.")
            continue