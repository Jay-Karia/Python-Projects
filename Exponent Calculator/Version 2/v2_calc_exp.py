print("Welcome to Exponent Calculator Developed --  By Jay")
print("For more Information check out the README.md file!")
print("\n1) Table of Exponent\n2) Single Number")

select = input()
if select == "1":
    print("1) Table of Exponent")
    user_exp = 0
    exp = None
    user_num = 0
    num = None

    try:
        num = (input("\nEnter a number: "))
        user_num = int(num)
        print(f"Number: {int(user_num)}\n")
    except ValueError as ve:
        user_num = len(num)
        print(f"Number: {int(user_num)}\n")

    try:
        exp = (input("Enter number of Exponent: "))
        user_exp = int(exp)
        print(f"Exponents: {int(user_exp)}\n")
    except ValueError as ve:
        user_exp = len(exp)
        print(f"Exponents"
              f": {int(user_exp)}\n")
    for i in range(user_exp):
        i = i + 1
        print(f"{user_num} ^ {i} == {user_num ** i}")
elif select == "2":
    print("2) Single Number")
    n = None
    e = None
    user_number = 0
    exp_user = 0
    try:
        print("\nEnter your Number: ", end=" ")
        n = input()
        user_number = int(n)
    except ValueError as ve:
        user_number = len(n)

    try:
        e = input(f"{user_number} ^ ")
        exp_user = int(e)
        print(f"{user_number} ^ {exp_user} == {user_number ** exp_user}")
    except ValueError as ve:
        exp_user = len(e)
        print(f"{user_number} ^ {exp_user} == {user_number ** exp_user}")