#IMPORTS
import time
import os
from os import system
import random

#Login
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
print(" _       ___    ____  ____  ____  ")
print("| |     /   \  /    ||    ||    \ ")
print("| |    |     ||   __| |  | |  _  |")
print("| |___ |  O  ||  |  | |  | |  |  |")
print("|     ||     ||  |_ | |  | |  |  |")
print("|     ||     ||     | |  | |  |  |")
print("|_____| \___/ |___,_||____||__|__|")
print("                                  ")
print("[1 = Sign in]")
print("[2 = Sign up]")
siorlo = input("Enter:  ")
if siorlo == ("2"):
    _ = system('cls')
    Username1 = input("Username:  ")
    _ = system('cls')
    Password1 = input("Password:  ")
    _ = system('cls')
    print("Login Succesfuly created!")
    time.sleep(2)
    _ = system('cls')
    print("Dont close this tab untill it closes by itselfs else you login won't be safed.")
    time.sleep(2)
    o = open("Login.txt","a+")
    o.write(Username1 + ":" + Password1 + "\n")
elif siorlo == ("1"):
    try:
        _ = system('cls')
        r = open("Login.txt", "r+")
        username = input("Enter your username:  ")
        _ = system('cls')
        password = input("Enter your password:  ")
        logincontent = r.read()
        if username + ":" + password in logincontent:
            _ = system('cls')
            
            print("Succesfully logged in!")
            time.sleep(2)
            _ = system('cls')
            
        else:
            _ = system('cls')
            print("Username or Password not existing! Try again!")
            time.sleep(2)
            _ = system('cls')
    except:
        print("Login not existing!")
        time.sleep(2)
        _ = system('cls')








        
