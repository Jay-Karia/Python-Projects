# Python String Sanitizer
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    elif ',' in time_string:
        splitter = ','
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + " " + secs


print("Enter your name")
name = input()
print("\nWelcome " + name + " to Python String Sanitizer -- By Jay\n")
print("Enter a String")
user_string = input()
print("String: " + user_string)
print("\nSanitizing...")
print("\nSanitized!!!")
print(sanitize(user_string))
# print("\nEnter a Operation on your String")
# print("1) Delete Commas\n2) Delete Full Stops\n3) Trim half of the String\n")
# op = input()
# for operation in op:
#     if '1' in operation:
#          print("\nDelete Commas: ")
#         # (one, two) = user_string.split(',')
#         # print(one + " " + two)
#     elif '2' in operation:
#         print("\nDelete Full Stops")
#     elif '3' in operation:
#         print("\nTrim Half of the String")
