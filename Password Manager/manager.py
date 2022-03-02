from tkinter import *
import random
import json

# Globals
password = ""
message = ""
security_key = ""
account_name = ""
agency = ""

encoded_password = ""
encoded_key = ""
decoded_password = ""
decoded_key = ""

user_name = ""

code_words = ['@#', '(', '\'', 'GH&^', '%', '!', '**', '%$#', '?>', '+', '.', ',', '---', '*///*', '*8', '^', '*&', '[]', ']]', 'gb', '<>', '===', ':', ';', '\"', '{', '||', '~', '`',
 ',,', '__', '-', '#@', '/*', ')(', '^^^']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', 
'9', '0']


def Encode(password, security_key):
    global encoded_password
    global encoded_key
    try:
        password = password.lower()
        for i in range(0, len(alphabets)):
            password = password.replace(alphabets[i], code_words[i])
            security_key = security_key.replace(alphabets[i], code_words[i])
            encoded_password = password
            encoded_key = security_key
    except:
        pass

def Decode(password, security_key):
    global decoded_password
    global decoded_key
    try:
        password = password.lower()
        for i in range(0, len(alphabets)):
            password = password.replace(code_words[i], alphabets[i])
            security_key = security_key.replace(code_words[i], alphabets[i])
            decoded_password = password
            decoded_key = security_key
    except:
        pass

def GetValueFromUser():
    global user_name
    global message
    global security_key
    global account_name
    global agency
    global password

    print("Enter your name")
    user_name = input()
    print("\nEnter the Password")
    password = input()
    print("\nEnter the Message")
    message = input()
    print("\nEnter the Security Key")
    security_key = input()
    print("\nEnter the Account Name")
    account_name = input()
    print("\nEnter the agency or organization")
    agency = input()
    
def WritingIntoJSON(file):

    counter = 0

    with open(f"{file_name}.json", 'w') as json_file:
        json.dump({"Passwords": [{}]}, json_file)

    Encode(password, security_key)

    file = file.replace('.json', '')
    filename = f"{file}.json"

    with open(filename, 'r') as f:
        data = json.load(f)

    data["Passwords"][counter]['Password'] = encoded_password
    data["Passwords"][counter]['Message'] = message
    data["Passwords"][counter]['Security Key'] = encoded_key
    data["Passwords"][counter]['Account Name'] = account_name
    data["Passwords"][counter]['Organization'] = agency

    with open(filename, 'w') as f:
        json.dump(data, f)

print("1. Get your existing password\n2. Store a new password\n")
# sel = input()
sel = "2"

if sel == "2":
    # print("Enter the json file name where all of you passwords would be stored (example: <username>_passwords)")
    # file_name = input()
    # file_name = f"{user_name}_passwords"
    file_name = f"_passwords"
    GetValueFromUser()
    WritingIntoJSON(file_name)
