print("Welcome to Python Exponent Finder Developed --  By Jay")
print("For more Information check out the README.md file!")
user_exp = 0
exp = None
user_num = 0
num = None
try:
    exp = (input("\nEnter number of Exponent: "))
    user_exp = int(exp)
    print(f"Exponent: {int(user_exp)}\n")
except ValueError as ve:
    user_exp = len(exp)
    print(f"Exponent: {int(user_exp)}\n")

try:
    num = (input("Enter a number: "))
    user_num = int(num)
    print(f"Number: {int(user_num)}\n")
except ValueError as ve:
    user_num = len(num)
    print(f"Number: {int(user_num)}\n")

for i in range(user_exp):
    if user_exp != 0:
        i = i + 1
        print(f"{user_num}^{i} == {user_num ** i}")
    else:
        pass