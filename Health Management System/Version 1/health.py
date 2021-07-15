print("Welcome to Health Management System -- By Jay")
print("\nEnter a name:\n1) Jay\n2) John\n3) Rohan\n")
def get_info(Name):
    if Name == "Jay":
        print("\nType:\n1) Exercises\n2) Diet\n")
        select = input()
        if select == "1":
            with open("jay_exercise", "r") as data:
                print("Jay's Exercises:\n")
                print(data.read())
        elif select == "2":
            with open("jay_diet") as data:
                print("Jay's Diet:\n")
                print(data.read())
        else:
            print("No such Type found!")
    elif Name == "John":
        print("\nType:\n1) Exercises\n2) Diet\n")
        select = input()
        if select == "1":
            with open("john_exercise", "r") as data:
                print("John's Exercises:\n")
                print(data.read())
        elif select == "2":
            with open("john_diet") as data:
                print("John's Diet:\n")
                print(data.read())
        else:
            print("No such Type found!")
    elif Name == "Rohan":
        print("\nType:\n1) Exercises\n2) Diet\n")
        select = input()
        if select == "1":
            with open("rohan_excercise", "r") as data:
                print("Rohan's Exercises:\n")
                print(data.read())
        elif select == "2":
            with open("rohan_diet") as data:
                print("Rohan's Diet:\n")
                print(data.read())
        else:
            print("No such Type found")

name = input()

if name == "1":
    get_info("Jay")
elif name == "2":
    get_info("Rohan")
elif name == "3":
    get_info("John")
else:
    print("No Name found!!")