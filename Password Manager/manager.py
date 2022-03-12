from email import message
from fileinput import filename
from tkinter import *
import random
import json

# Globals

password = ""
security_key = ""
account_name = ""

encoded_password = ""
encoded_key = ""
decoded_password = ""
decoded_key = ""

user_name = ""
counter = 0

code_words = ['@#', '(', '\'', '&^', '%', '!', '**', '%$#', '?>', '+', '.', ',', '--', '/*', '*8', '^', '*&', '[]', ']]', 'gb', '<>', '==', ':', ';', '\"', '{', '||', '~', '`',
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
    global security_key
    global account_name
    global password

    print("\nEnter the Password")
    password = input()
    print("\nEnter the Security Key")
    security_key = input()
    print("\nEnter the Account Name")
    account_name = input()

def CreateNewFile(file_name):
    with open(f'{file_name}.json', 'w') as json_file:
        json.dump({"Total Passwords": 0,"Passwords": []}, json_file)

def WritingIntoJSON(file):

    with open(f"{file_name}.json", 'r') as json_file:
        file_ = json.load(json_file)
        pass_num = file_['Total Passwords']

    Encode(password, security_key)

    data_dict = {
        "Password": encoded_password,
        "Security Key": encoded_key,
        "Account Name": account_name,
    }

    pass_num = int(pass_num)
    pass_num += 1


    with open(f'{file_name}.json','r+') as file:
        file_data = json.load(file)
        file_data["Passwords"].append(data_dict)
        file_data["Total Passwords"] = pass_num
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def GetPassword(file):
    # print("Enter security key")
    # key = input()
    key = "0901"

    file_name = f"{file}.json"
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)

        Encode("", key)

        for i in range(0, len(data["Passwords"])):
            if data["Passwords"][i]["Security Key"] == encoded_key:
                json_pass = data["Passwords"][i]["Password"]
                json_key = data["Passwords"][i]["Security Key"]
                json_account_name = data["Passwords"][i]["Account Name"]
                Decode(json_pass, json_key)
                print(decoded_password)
                break
            else:
                print("Invalid Security Key")

# print("1. Get your existing password\n2. Store a new password\n3. Delete a Password file or a password")
# sel = input()
sel = "1"

if sel == "2":
    print("1.Create a new Passsword File\n2.Append Password to existing file")
    choice = input()
    if choice == "1":
        print("Enter the json file name where all of you passwords would be stored")
        file_name = input()
        CreateNewFile(file_name)
        GetValueFromUser()
        WritingIntoJSON(file_name)
    elif choice == "2":
        print("Enter the password file name")
        file_name = input()
        GetValueFromUser()
        WritingIntoJSON(file_name)

elif sel == "1":
    print("Enter the password file")
    # file_name = input()
    file_name = "jay_passwords"
    GetPassword(file_name)
