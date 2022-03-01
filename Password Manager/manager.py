from tkinter import *
import random
import json

# Globals
password = "09Jan197#"
message = "My google account password"
security_key = "908&*^"
account_name = "jay.sanjay.karia@gmail.com"
agency = "Google"

encoded_password = ""
encoded_key = ""
decoded_password = ""
decoded_key = ""

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

def WritingIntoJSON(file):
    counter = 0
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

    random.shuffle(code_words)
    random.shuffle(alphabets)

    Encode(password, security_key)

    counter+=1
    file = file.replace('.json', '')
    filename = f"{file}.json"

    entry = { f"Password {counter}": {
            "Password": encoded_password,
            "Message": message,
            "Security Key": encoded_key,
            "Account Name": account_name,
            "Organization": agency
        }
    }

    with open(filename, 'r') as file:
        data = json.load(file)

    data[f"Password {counter}"] = {}
    data[f"Password {counter}"]['Password'] = encoded_password
    data[f"Password {counter}"]['Message'] = message
    data[f"Password {counter}"]['Security Key'] = encoded_key
    data[f"Password {counter}"]['Account Name'] = account_name
    data[f"Password {counter}"]['Organization'] = agency

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

print("1. Get your existing password\n2. Store a new password\n")
# sel = input()
sel = "2"

if sel == "2":
    # print("Enter the json file name where all of you passwords would be stored (example: <username>_passwords)")
    # file_name = input()
    file_name = "jay_passwords"
    WritingIntoJSON(file_name)
