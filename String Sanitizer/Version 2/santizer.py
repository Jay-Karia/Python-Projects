print("Welcome to Python String Sanitizer -- By Jay")
user_string = input("\nEnter your String: ")
print("\n1) Delete Commas(,)\n2) Delete Colons(:)\n3) Delete Whitespace( )\n4) Custom Delete")


def delete_commas(string):
    splitter = ','
    final_string = string.replace(splitter, "")
    print("\nFinal String: ", final_string)


def delete_colons(string):
    splitter = ':'
    final_string = string.replace(splitter, "")
    print("\nFinal String: ", final_string)


def delete_whitespace(string):
    splitter = ' '
    final_string = string.replace(splitter, "")
    print("\nFinal String: ", final_string)

def custom_del(string):
    ch = input("\nEnter character to be deleted: ")
    splitter = ch
    final_string = string.replace(splitter, "")
    print("\nFinal String: ", final_string)
    pass


valid = True

while valid == True:
    select = input()

    if select == "1":
        delete_commas(user_string)
        break
    elif select == "2":
        delete_colons(user_string)
        break
    elif select == "3":
        delete_whitespace(user_string)
        break
    elif select == "4":
        custom_del(user_string)
        break
    else:
        print("It should be a valid option!")
        valid = False