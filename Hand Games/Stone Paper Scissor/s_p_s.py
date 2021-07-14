# Stone Paper Scissor Game in Python
import random
print("Welcome to Stone Paper Scissor Game Developed -- By Jay")
print("\nYou will only get 10 chances, go and try to beat the computer!!\n")
selection = [
    "Stone",
    "Paper",
    "Scissor"
]
i = 0
comp_points = 0
user_points = 0

while i in range(10):
    i = i+1
    comp_choice = random.choice(selection)
    user_sel = input(f"Computer has selected, it's your turn now! {i}: ")
    print(comp_choice)
    if comp_choice == "Stone" and user_sel == "Stone":
        print("Tie!!\n")
    elif comp_choice == "Stone" and user_sel == "Paper":
        print("Your Point!!\n")
        user_points = comp_points + 1
    elif comp_choice == "Stone" and user_sel == "Scissor":
        print("Computer's Point!!\n")
        comp_points = user_points + 1
    elif comp_choice == "Paper" and user_sel == "Paper":
        print("Tie!!\n")
    elif comp_choice == "Paper" and user_sel == "Scissor":
        print("Your Point!!\n")
        user_points = comp_points + 1
    elif comp_choice == "Paper" and user_sel == "Stone":
        print("Computer's Point!!\n")
        comp_points = user_points + 1
    elif comp_choice == "Scissor" and user_sel == "Scissor":
        print("Tie!!\n")
    elif comp_choice == "Scissor" and user_sel == "Stone":
        print("Your Point!!\n")
        user_points = comp_points + 1
    elif comp_choice == "Scissor" and user_sel == "Paper":
        print("Computer's Point!!\n")
        comp_points = user_points + 1


print("\nComputer Points: ", comp_points)
print("Your Points: ", user_points)
if comp_points > user_points:
    print("Computer Won!!\n")
elif comp_points < user_points:
    print("You Won!!")
else:
    print("Tie!!")
