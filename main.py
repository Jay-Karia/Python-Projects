print("Welcome to Python Average Generator -- By Jay")
print("\nEnter a first number")

valid = None
while not valid:
    try:
        num1 = int(input())
        print("Number One: ", num1)
        break
    except ValueError as ve:
        print("It should be a number")
        valid = False

print("\nEnter Number Two")
new_valid = None
while not new_valid:
    try:
        num2 = int(input())
        print("Number Two: ", num2)
        break
    except ValueError as v:
        print("It should be a number")
        new_valid = False
def get_avg(number1, number2):
    average = (number1 + number2) / 2
    print("\nAverage: ", average)

get_avg(num1, num2)