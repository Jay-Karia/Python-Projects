from fileinput import filename
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
counter = 0

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
    global pass_name

    # print("Enter Password Name to be Identified")
    # pass_name = input()
    pass_name = "sdf"
    # print("\nEnter your name")
    # user_name = input()
    user_name = "gfh"
    # print("\nEnter the Password")
    # password = input()
    password = "90uj"
    # print("\nEnter the Security Key")
    # security_key = input()
    security_key = "567uh"
    # print("\nEnter the Account Name")
    # account_name = input()
    account_name = "-=908ik"

def CreateNewFile(file_name):
    with open(f'{file_name}.json', 'w') as json_file:
        json.dump({"Passwords": [{"Total Passwords": 0}]}, json_file)

def WritingIntoJSON(file):

    with open(f"{file_name}.json", 'r') as json_file:
        file_ = json.load(json_file)
        pass_num = file_[0]['Total Passwords']

    # with open(f'{file_name}.json', 'a+') as json_file:
    #     json.dump([{"Total Passwords": pass_num}, {}], json_file)

    Encode(password, security_key)

    data_dict = {
        # pass_name: {},
        "Password": encoded_password,
        "Message": message,
        "Security Key": encoded_key,
        "Account Name": account_name,
        "Organization": agency
    }

    file = file.replace('.json', '')
    filename = f"{file}.json"

    with open(filename, 'r+') as f:
        data = json.load(f)
        data.update(data_dict)
        data.seek(0)
        json.dump(data, f)

    pass_num = int(pass_num)
    pass_num += 1


    # data[pass_num][pass_name] = {}
    # data[pass_num][pass_name]['Password'] = encoded_password
    # data[pass_num][pass_name]['Message'] = message
    # data[pass_num][pass_name]['Security Key'] = encoded_key
    # data[pass_num][pass_name]['Account Name'] = account_name
    # data[pass_num][pass_name]['Organization'] = agency
    data[0]["Total Passwords"] = pass_num


    with open(filename, 'w') as f:
        json.dump(data, f)

print("1. Get your existing password\n2. Store a new password\n")
# sel = input()
sel = "2"

if sel == "2":
    print("1.Create a new Passsword File\n2.Append Password to existing file")
    # choice = input()
    choice = "1"
    if choice == "1":
        # print("Enter the json file name where all of you passwords would be stored (example: <username>_passwords)")
        # file_name = input()
        file_name = "_passwords"
        GetValueFromUser()
        # CreateNewFile(file_name)
        WritingIntoJSON(file_name)


# TODO: Add automatically comma and a bracket for entering a new password