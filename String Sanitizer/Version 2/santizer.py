print("Welcome to Python String Sanitizer -- By Jay")
user_string = input("\nEnter your String: ")
print("\n1) Delete Commas(,)\n2) Delete Colons(:)\n3) Delete Whitespace( )")
select = input()


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


valid = True

while valid:
    if select == "1":
        delete_commas(user_string)
        break
    elif select == "2":
        delete_colons(user_string)
        break
    elif select == "3":
        delete_whitespace(user_string)
        break
    else:
        print("It should be a valid option!")
        valid = False
