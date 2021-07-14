# Snake Water Gun Game in Python
import random
print("Welcome to Snake Water Gun Game Developed -- By Jay")
print("\nYou will only get 10 chances, go and try to beat the computer!!\n")
selection = [
    "Snake",
    "Water",
    "Gun"
]
i = 0
comp_points = 0
user_points = 0

while i in range(10):
    i = i+1
    comp_choice = random.choice(selection)
    user_sel = input(f"Computer has selected, it's your turn now! {i}: ")
    print(comp_choice)
    if comp_choice == "Snake" and user_sel == "Snake":
        print("Tie!!\n")
    elif comp_choice == "Snake" and user_sel == "Water":
        print("Computer's Point!!\n")
        comp_points = comp_points + 1
    elif comp_choice == "Snake" and user_sel == "Gun":
        print("Your Point!!\n")
        user_points = user_points + 1
    elif comp_choice == "Water" and user_sel == "Water":
        print("Tie!!\n")
    elif comp_choice == "Water" and user_sel == "Gun":
        print("Computer's Point!!\n")
        comp_points = comp_points + 1
    elif comp_choice == "Water" and user_sel == "Snake":
        print("Your Point!!\n")
        user_points = user_points + 1
    elif comp_choice == "Gun" and user_sel == "Gun":
        print("Tie!!\n")
    elif comp_choice == "Gun" and user_sel == "Snake":
        print("Computer's Point!!\n")
        comp_points = comp_points + 1
    elif comp_choice == "Gun" and user_sel == "Water":
        print("Your Point!!\n")
        user_points = user_points + 1


print("\nComputer Points: ", comp_points)
print("Your Points: ", user_points)
if comp_points > user_points:
    print("Computer Won!!\n")
elif comp_points < user_points:
    print("You Won!!")
else:
    print("Tie!!")
